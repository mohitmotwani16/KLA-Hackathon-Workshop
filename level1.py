from cv2 import cv2
import pandas as pd
import numpy as np
import csv

img1 = cv2.imread("wafer_image_1.png")
img2 = cv2.imread("wafer_image_2.png")
img3 = cv2.imread("wafer_image_3.png")
img4 = cv2.imread("wafer_image_4.png")
img5 = cv2.imread("wafer_image_5.png")

images = []

img1_gray = cv2.cvtColor(img1, cv2.COLOR_RGB2GRAY)
img2_gray = cv2.cvtColor(img2, cv2.COLOR_RGB2GRAY)
img3_gray = cv2.cvtColor(img3, cv2.COLOR_RGB2GRAY)
img4_gray = cv2.cvtColor(img4, cv2.COLOR_RGB2GRAY)
img5_gray = cv2.cvtColor(img5, cv2.COLOR_RGB2GRAY)
images.append(img1_gray)
images.append(img2_gray)
images.append(img3_gray)
images.append(img4_gray)
images.append(img5_gray)

l = []



df = pd.DataFrame(l)
df.to_csv('res.csv',header=False,index=False)

def main():
    k = 1
    for img in images:
        for i in range(1,len(img)):
            for j in range(1,len(img[0]) - 1):
                if(img[i][j] != img[i][j-1] and img[i][j] != img[i][j+1]):
                    l.append([k, j, 599-i])
        k += 1
    
    df = pd.DataFrame(l)
    df.to_csv('res.csv',header=False,index=False)


if __name__ == "__main__":
    main()
