import cv2

img = cv2.imread("kiara.png")

print(img.shape)

imgResize = cv2.resize(img, (700, 350))
imgCropped = img[0:650, 150:250]

cv2.imshow("Original", img)
cv2.imshow("Resized", imgResize)
cv2.imshow("Cropped", imgCropped)

cv2.waitKey(0)
