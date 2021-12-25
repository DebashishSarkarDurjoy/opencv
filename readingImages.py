import cv2

cap = cv2.VideoCapture("Resources/test_video.mp4")
cap.set(3, 340)
cap.set(4, 560)

while True:
    success, img = cap.read()
    cv2.imshow("Reading Video", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
