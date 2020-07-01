# Personally Identifiable Information (PII) Blur

## In one sentence

Command line Python script that 1) takes an image or directory of images, 2) identifies faces and number plates, 3) blurs identified content using a Gaussian blur, and 4) writes modified images to specified directory.

## Why we built this

Whilst many of our 360 images are shot in less trafficed areas (remote paths, riverways, etc.) they do, on occassion capture Personally Identifiable Information.

Morally we believe it is right to protect the privacy of people captured or identifiable from the information in our photos.

Legally, GDPR laws make privacy a legal requirement for those dealing with private information.

Therefore, we wanted to detect and blur faces and license plates in our images. The goal is to blur all identifiable faces and license plates.

Personally Identifiable Information is the result of that goal.

## How it works

### Overview

1. You define a single photo or directory of photos
2. The script creates various versions of each photo in an attempt to identify faces and licnesce plates
3. If any information has been identified the script applies a smooth Gaussian blur
4. And finally writes out new blurred image into output directory
5. Any photos where no blurring required will remain unmodified but be copied into output directory.

## Requirements

### OS Requirements

Works on Windows, Linux and MacOS.

### Software Requirements / Installation



## Other useful reads

* [Mapillary image blurring](https://blog.mapillary.com/update/2018/04/19/accurate-privacy-blurring-at-scale.html)

## Support 

We offer community support for all our software on our Campfire forum. [Ask a question or make a suggestion here](https://campfire.trekview.org/c/support/8).

## License

Personally Identifiable Information (PII) Blur is licensed under a [GNU AGPLv3 License](/LICENSE.txt).