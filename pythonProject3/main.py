import cv2
file = "1.mp4" # путь к файлу с картинкой
cap = cv2.VideoCapture(file)
out = cv2.VideoWriter('captured.jpg',-1, 20.0, (640,480))
while(cap.isOpened()):
    ret,frame = cap.read()
    out.write(frame)
    frame_re = cv2.rotate(frame , cv2.ROTATE_180)
    cv2.imshow('frame',frame_re)
    if cv2.waitKey(33) & 0xFF == ord('q'):
        break
cap.release()
out.release()
cv2.destroyAllWindows()