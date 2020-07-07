# Personally Identifiable Information (PII) Blur

## In one sentence

Command line Python script that 1) takes an image or directory of images, 2) identifies faces and number plates, 3) blurs identified content using a Gaussian blur, and 4) writes modified images to specified directory.

## Why we built this

Whilst many of our 360 images are shot in less trafficked areas (remote paths, riverways, etc.) they do, on occasion capture Personally Identifiable Information.

Morally we believe it is right to protect the privacy of people captured or identifiable from the information in our photos.

Legally, GDPR laws make privacy a legal requirement for those dealing with private information.

Therefore, we wanted to detect and blur faces (people) and license plates (cars) in our images. The goal is to blur all identifiable faces and license plates.

Personally Identifiable Information is the result of that goal.

## How it works

### Overview

1. You define a single photo or directory of photos
2. The script creates various versions of each photo in an attempt to identify people and cars
3. If any information has been identified the script applies a smooth Gaussian blur
4. And finally writes out new blurred image into output directory
5. Any photos where no blurring required will remain unmodified but be copied into output directory.

## Requirements

### OS Requirements

Works on Windows, Linux and MacOS.

### Software Requirements / Installation

We have tested this script on Python version 3.7.6-amd64.

The following modules are required

* `pip install opencv-python`
* `pip install tensorflow==1.15`
* `pip install keras==2.3.1`
* `pip install imageai`

You must also download the model file [resnet50_coco_best_v2.0.1.h5](https://github.com/OlafenwaMoses/ImageAI/releases/tag/1.0) and place in the `models` directory in this repository.

## Usage

There are two scripts `pii-blur-fast.py` and `pii-blur-slow.py`.

`pii-blur-fast.py` is faster, but identified fewer objects. If clear cars and people in your images (e.g. full outline of car / person visible) is generally best to use this script (or at least check results) before using the `pii-blur-slow.py` version.

```
python pii-blur.py [INPUT_DIR] [OUTPUT_DIR]
```

Where `[INPUT]` is a directory of image files you want to blur and `[OUTPUT_DIR]` is where you want blur photos to be placed.

## Other useful reads

* [Mapillary image blurring](https://blog.mapillary.com/update/2018/04/19/accurate-privacy-blurring-at-scale.html)
* https://dev.to/codetricity/360-image-database-for-face-object-detection-4mgm

## Support 

We offer community support for all our software on our Campfire forum. [Ask a question or make a suggestion here](https://campfire.trekview.org/c/support/8).

## License

Personally Identifiable Information (PII) Blur is licensed under a [GNU AGPLv3 License](/LICENSE.txt).