"""
Author: Chin-Yu Morris Chuang
Date: 2023-09-24

Homework 1
# https://predoc.dlc.ntu.edu.tw/viewer?embedded=true&url=https%3A%2F%2Fcool.ntu.edu.tw%2Fcourses%2F29754%2Ffiles%2F4403693%2Fdownload%3Fverifier%3DkA1PXlhMBGn0UNVk2nJN2WHCPoEXxiIZew6B3fYs

Four Requirements
1. Write a program for non-integer scaling of an image with two interpolation methods:
   -- Bilinear interpolation
   -- Bicubic interpolation
2. Take a selfie of yourself, and apply the above image scaling program on your selfie
   (or part of your selfie, e.g., your right eye) with the scaling factors of 0.2, 5, and 32.
3. Compare the quality of the images obtained with bilinear interpolation and with bicubic interpolation.
4. Explain the method of bicubic interpolation, and compare its computational complexity with that of bilinear interpolation.

For requirements 1 & 2, you need to show
。 which function you use or implement
    -- how does your program work
    -- how to use your program
。 For requirements 3 & 4, you need to provide
    -- Resulted images for comparison
    -- Explanation


Reference
。 https://www.twblogs.net/a/5eec83c8411a0ed3151d8be4
。 https://shengyu7697.github.io/python-opencv-resize/
。 https://docs.opencv.org/2.4/modules/imgproc/doc/geometric_transformations.html#cv2.resize
"""

import os
import cv2
from pathlib import Path

PATH_DIR = Path(os.path.dirname(os.path.realpath(__file__)))

def scale(image, method):
    # 0.2
    image_shrinked = cv2.resize(image, None, fx=0.2, fy=0.2, interpolation=method)
    path_shrinked = path_dir.joinpath("shrinked selfie.jpg")
    cv2.imwrite(os.path.abspath(path_shrinked), image_shrinked)
    # 5
    image_5_times = cv2.resize(image, None, fx=5, fy=5, interpolation=method)
    path_5_times = path_dir.joinpath("5-times selfie.jpg")
    cv2.imwrite(os.path.abspath(path_5_times), image_5_times)
    # 32
    image_32_times = cv2.resize(image, None, fx=32, fy=32, interpolation=method)
    path_32_times = path_dir.joinpath("32-times selfie.jpg")
    cv2.imwrite(os.path.abspath(path_32_times), image_32_times)


if __name__ == "__main__":
    path = PATH_DIR.joinpath("selfie.jpg")
    image = cv2.imread(os.path.abspath(path))

    path_dir = PATH_DIR.joinpath("bilinear")
    path_dir.mkdir(exist_ok=True)
    scale(image, cv2.INTER_LINEAR)

    path_dir = PATH_DIR.joinpath("bicubic")
    path_dir.mkdir(exist_ok=True)
    scale(image, cv2.INTER_CUBIC)
