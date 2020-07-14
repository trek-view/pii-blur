import os
from os import listdir
from os.path import isfile,isdir, join
import numpy as np
import cv2
import time
import sys
from imageai.Detection import ObjectDetection
from exiftool_custom import exiftool

def alphaBlend(img1, img2, mask):
    # print(mask)
    if mask.ndim==3 and mask.shape[-1] == 3:
        alpha = mask/255.0
    else:
        alpha = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)/255.0
    # print('alpha: ', alpha)
    blended = cv2.convertScaleAbs(img1*(1-alpha) + img2*alpha)
    return blended

def blurImageWithCircle(originalimg, circles):
    img = originalimg
    H,W = img.shape[:2]
    for circle in circles:
        mask = np.zeros((H,W), np.uint8)
        cv2.ellipse(mask, circle[0], circle[1], 0, 0, 360, (255,255,255), -1, cv2.LINE_AA)
        mask = cv2.GaussianBlur(mask, (21,21),11 )

        blured = cv2.GaussianBlur(img, (21,21), 11)
        img = alphaBlend(img, blured, mask)
    return img

def drawRectangle(blurimg, rectangles):
    img = blurimg
    for rect in rectangles:
        img = cv2.rectangle(img, (rect[0], rect[1]), (rect[2], rect[3]), (255,255,0), 2)
    return img

def blurFile(detector, inputfile, outputfile, twicefile, percentage = 25):
    detections = detector.detectObjectsFromImage(input_image=inputfile, output_image_path='temp.jpg', minimum_percentage_probability=percentage)
    rectangles = []
    for eachObject in detections:
        # print(eachObject["name"] , " : " , eachObject["percentage_probability"] )
        # print(eachObject['box_points'])
        if eachObject["name"] == 'person':
            rectangles.append(eachObject['box_points'])
        if eachObject["name"] == 'car':
            rectangles.append(eachObject['box_points'])
        if eachObject["name"] == 'truck':
            rectangles.append(eachObject['box_points'])
    print(rectangles)
    img = cv2.imread(inputfile)
    circles = []
    for rect in rectangles:
        center = (int((rect[0] + rect[2])/2), int((rect[1] + rect[3])/2) )
        axesLength = (int((rect[2] - rect[0])/2*1.2), int((rect[3] - rect[1])/2*1.2))
        circles.append([center, axesLength])
 
    blurimg = blurImageWithCircle(img, circles)
    
    # reimg = drawRectangle(blurimg, rectangles)
    
    cv2.imwrite(outputfile, blurimg)
    
    
    with exiftool.ExifTool() as et:
        et.copy_tags(inputfile, outputfile)    
 
def main(argv):
    execution_path = os.getcwd()

    detector = ObjectDetection()
    detector.setModelTypeAsRetinaNet()
    detector.setModelPath( os.path.join(execution_path , "models/resnet50_coco_best_v2.0.1.h5"))
    detector.loadModel()
    inputdir = argv[0]
    outputdir = argv[1]
    try:
        percentage = int(argv[2])
    except:
        print('incorrect command')
    if isdir(outputdir):
        pass
    else:
        os.mkdir(outputdir)
    inputfiles = [f for f in listdir(inputdir) if isfile(join(inputdir, f))]
    # print(inputdir, outputdir, inputfiles)
    for inputfile in inputfiles:
        infile = inputdir + '/' + inputfile
        outfile = outputdir + '/' + 'blur_' + inputfile
        twicefile = outputdir + '/' + 'twice_' + inputfile
        blurFile(detector, infile,outfile, twicefile, percentage)
    os.remove('temp.jpg')    
    # testin = 'testimages/Untitled.jpg'
    # testout = 'output.jpg'
    # blurFile(face_cascade, testin,testout)        
 
if __name__ == "__main__":
   main(sys.argv[1:])