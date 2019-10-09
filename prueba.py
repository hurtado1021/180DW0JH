import cv2

cap = cv2.Videocapture(0)
while True:
        ret,frame = cap.read()
        cv2.imwrite('hola.jpg', frame)
        cap.release()
        break
