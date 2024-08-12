from ultralytics import YOLO
import cv2

model = YOLO('../yolo_weights/yolov8l.pt')
results = model('assets/images/img10.jpg', show=True)
cv2.waitKey(0)