"""
Author: Chin-Yu Morris Chuang
Date: 2023-10-16

Homework 3
1. Suppose that a digital image is subjected to histogram equalization.
   Show that a second pass of histogram equalization (on the histogram-equalized image)
   will produce exactly the same result as the first pass.
2. Write a program for histogram equalization, and test it with your own selfie took
   in a relatively dark environment so that we can clearly see the effect of histogram equalization in image enhancement.
   Please show the histograms of your selfie before and after histogram equalization and explain your results.
   (Note: You only have to work on the gray scale image.)

檔案格式
* 學號字母小寫，圖片檔案可接受 jpg、jpeg 和 png。
Report 內容
* 學號姓名、手寫題答案、程式執行的環境、使用的套件。 （若使用 Python 請註明版本）

Reference
* https://blog.csdn.net/qq_37385726/article/details/82313799
* https://docs.opencv.org/4.x/d5/daf/tutorial_py_histogram_equalization.html
* https://ithelp.ithome.com.tw/articles/10256203
* https://docs.opencv.org/3.4/d4/d1b/tutorial_histogram_equalization.html
"""

import os
import cv2
import matplotlib.pyplot as plt
from pathlib import Path

# 得到作業所在目錄路徑 (取得 d12922014 資料夾路徑)
HOMEWORK_DIR_PATH = Path(os.path.dirname(os.path.realpath(__file__))).parent
# 設定存放圖片結果資料夾路徑 (取得 results 資料夾路徑)
RESULTS_DIR_PATH = HOMEWORK_DIR_PATH.joinpath("results")
# 設定原始圖片檔案路徑 (取得 origin.jpg 檔案路徑)
ORIGIN_JPG_PATH = HOMEWORK_DIR_PATH.joinpath("origin.jpg")

# 程式碼進入點
if __name__ == "__main__":
    # 以灰階形式讀取「原始圖片」
    src = cv2.imread(os.path.abspath(ORIGIN_JPG_PATH), cv2.IMREAD_GRAYSCALE)
    # 以 png 格式儲存「處理前」圖片，以供後續對比
    cv2.imwrite(os.path.abspath(Path(RESULTS_DIR_PATH, "before.png")), src)
    # 繪製、儲存並顯示「處理前」histogram
    fig, ax = plt.subplots()
    ax.hist(src.ravel(), 256, [0, 256],color='r')
    plt.savefig(os.path.abspath(Path(RESULTS_DIR_PATH, "before_histogram.png")))
    plt.show()

    # 對「原始圖片」進行 histogram equalization 處理
    dst = cv2.equalizeHist(src)
    # 以 png 格式儲存「處理後」圖片，以供後續對比
    cv2.imwrite(os.path.abspath(Path(RESULTS_DIR_PATH, "after.png")), dst)
    # 繪製、儲存並顯示「處理後」histogram
    fig, ax = plt.subplots()
    ax.hist(dst.ravel(), 256, [0, 256],color='r')
    plt.savefig(os.path.abspath(Path(RESULTS_DIR_PATH, "after_histogram.png")))
    plt.show()

    # 對「處理後」圖片再次進行 histogram equalization
    dst2 = cv2.equalizeHist(dst)
    # 以 png 格式儲存「二次處理後」圖片，以供後續對比
    cv2.imwrite(os.path.abspath(Path(RESULTS_DIR_PATH, "twice_after.png")), dst2)
    # 繪製、儲存並顯示「二次處理後」histogram
    fig, ax = plt.subplots()
    ax.hist(dst2.ravel(), 256, [0, 256],color='r')
    plt.savefig(os.path.abspath(Path(RESULTS_DIR_PATH, "twice_after_histogram.png")))
    plt.show()