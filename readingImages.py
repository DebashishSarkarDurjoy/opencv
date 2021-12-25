import cv2

path = "Resources/kiara.png"

kiara = cv2.imread(path)
cv2.imshow("Naked Kiara", kiara)

cv2.waitKey(0)
