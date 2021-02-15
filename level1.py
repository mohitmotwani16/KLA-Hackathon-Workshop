from cv2 import cv2

img1 = cv2.imread("wafer_image_1.png")
img2 = cv2.imread("wafer_image_2.png")
img1_gray = cv2.cvtColor(img1, cv2.COLOR_RGB2GRAY)
img2_gray = cv2.cvtColor(img2, cv2.COLOR_RGB2GRAY)
img_bwx = cv2.bitwise_xor(img1_gray,img2_gray)
#cv2.imshow("Result", img_bwx)
#cv2.waitKey(0)
L = [] # x and y cooridinates where xor is not 0
for i in range(0,len(img_bwx)):
    for j in range(0,len(img_bwx[0])):
        if(img_bwx[i][j] != 0):
            L.append([i,j])

print(L)
print(len(L))