from ultralytics import YOLO
import cv2
import cvzone
import math

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

model = YOLO("../yolo_weights/yolov8n.pt")

classNames = open("utils/coco.txt", "r")
data = classNames.read()
class_list = data.split("\n")
classNames.close()

# print(class_list)


while True:
    success, img = cap.read()
    results = model(img, stream=True)

    for r in results:
        boxes = r.boxes
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            #cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

            w, h = x2-x1, y2-y1

            cvzone.cornerRect(img, (x1, y1, w, h))

            conf = math.ceil((box.conf[0]*100))/100


            #classNames
            cls = int(box.cls[0])
            cvzone.putTextRect(img, f'{class_list[cls]} {conf}', (max(0, x1), max(35, y1)), scale=0.7, thickness=1)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
