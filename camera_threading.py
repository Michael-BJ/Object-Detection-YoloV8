import cv2
import time

start_time = time.time()
display_time = 2
fc = 0
FPS = 0

cap = cv2.VideoCapture(0)

while True:
    fc+=1
    TIME = time.time() - start_time
    if (TIME) >= display_time :
        FPS = fc / (TIME)
        fc = 0
        start_time = time.time()
        
    fps_disp = "FPS: "+str(FPS)[:5]

    _, frame = cap.read()
    image = cv2.putText(frame, fps_disp, (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    
    cv2.imshow("TEST", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()