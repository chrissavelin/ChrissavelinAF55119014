import cv2

img = cv2.imread("F55119014.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Before", img)
cv2.imshow("After", gray)

cv2.waitKey(0)
cv2.destroyAllWindows()
