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

。 For requirements 1 & 2, you need to show
    -- which function you use or implement
    -- how does your program work
    -- how to use your program
。 For requirements 3 & 4, you need to provide
    -- Resulted images for comparison
    -- Explanation

1. 檔案格式
    -- 學號字母小寫，圖片檔案可接受 jpg、jpeg 和 png。
    -- https://cool.ntu.edu.tw/courses/29754/files/4405070/preview?random=273415303282373675683051764904840924813&
2. Report 內容：除了投影片裡的要求之外，需包含學號姓名、程式執行的環境、使用的套件。 （若使用 Python 請註明版本）

Reference
。 https://www.twblogs.net/a/5eec83c8411a0ed3151d8be4
。 https://shengyu7697.github.io/python-opencv-resize/
。 https://docs.opencv.org/2.4/modules/imgproc/doc/geometric_transformations.html#cv2.resize
"""

import os
import cv2
from pathlib import Path

# 得到作業所在目錄路徑。換言之，取得 d12922014 資料夾路徑
HOMEWORK_DIR_PATH = Path(os.path.dirname(os.path.realpath(__file__))).parent
# 設定存放圖片結果資料夾路徑。換言之，為 d12922014 資料夾底下的 results
RESULTS_DIR_PATH = HOMEWORK_DIR_PATH.joinpath("results")
# 設定原始圖片檔案路徑。換言之，為 d12922014 資料夾底下的 origin.jpg
ORIGIN_JPG_PATH = HOMEWORK_DIR_PATH.joinpath("origin.jpg")

# 依所選擇的方法 (bilinear or bicubis)，將圖片縮放 0.2x、5x、32x 倍
def scale_by_method(image, method):
    RESULTS_DIR_PATH.mkdir(exist_ok=True)
    prefix = "bilinear" if method == cv2.INTER_LINEAR else "bicubic"
    # 0.2x
    image_shrinked = cv2.resize(image, None, fx=0.2, fy=0.2, interpolation=method)
    path_shrinked = RESULTS_DIR_PATH.joinpath(f"{prefix}_0.2x.jpg")
    cv2.imwrite(os.path.abspath(path_shrinked), image_shrinked)
    # 5x
    image_5_times = cv2.resize(image, None, fx=5, fy=5, interpolation=method)
    path_5_times = RESULTS_DIR_PATH.joinpath(f"{prefix}_5x.jpg")
    cv2.imwrite(os.path.abspath(path_5_times), image_5_times)
    # 32x
    image_32_times = cv2.resize(image, None, fx=32, fy=32, interpolation=method)
    path_32_times = RESULTS_DIR_PATH.joinpath(f"{prefix}_32x.jpg")
    cv2.imwrite(os.path.abspath(path_32_times), image_32_times)

# 程式碼進入點
if __name__ == "__main__":
    # 讀取原始圖片
    image = cv2.imread(os.path.abspath(ORIGIN_JPG_PATH))
    # 用 bilinear 的方式，將圖片縮放 0.2x、5x、32x 倍
    scale_by_method(image, cv2.INTER_LINEAR)
    # 用 bicubic 的方式，將圖片縮放 0.2x、5x、32x 倍
    scale_by_method(image, cv2.INTER_CUBIC)
