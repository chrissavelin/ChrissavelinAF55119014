import cv2

img = cv2.imread("F55119014.png")
img1 = 255 - img

cv2.imshow("Before", img)
cv2.imshow("After", img1)

cv2.waitKey(0)
cv2.destroyAllWindows()
