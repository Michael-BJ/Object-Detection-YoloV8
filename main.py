import cv2
from PIL import Image
from ultralytics import YOLO
import time


start_time = time.time()
display_time = 2
fc = 0
FPS = 0

status = 0


# Load a pretrained YOLOv8n model
model = YOLO('best.pt')

# open a video file or start a video stream
cap = cv2.VideoCapture(0)  # replace with 0 for webcam

while cap.isOpened():

    fc+=1
    TIME = time.time() - start_time
    if (TIME) >= display_time :
        FPS = fc / (TIME)
        fc = 0
        start_time = time.time()
        
    fps_disp = "FPS: "+str(FPS)[:5]

    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        break

    # flip the image
    # frame = cv2.flip(frame, -1) 

    # Run inference on the current frame
    results = model(frame, conf=0.60)[0]  # results list

    if len(results.boxes) >0:
        status = 1
    else :
        status = 0
    

    for r in results:
        frame = r.plot()

    image = cv2.putText(frame, fps_disp, (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    # Display the resulting frame
    cv2.imshow('frame', frame)
    
    print("Status:", status)

    # Press 'q' on keyboard to  exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the cap object and destroy all windows
cap.release()
cv2.destroyAllWindows()