import base64
import cv2
import numpy as np
from ultralytics import YOLO

# Load the YOLO model only once
model = YOLO("yolov8n.pt")


def detect_objects(image_data):

    # Remove the data:image/jpeg;base64, part
    image_data = image_data.split(",")[1]

    # Decode Base64 to bytes
    image_bytes = base64.b64decode(image_data)

    # Convert bytes to numpy array
    np_arr = np.frombuffer(image_bytes, np.uint8)

    # Decode image
    image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

    # Run YOLO
    results = model(image)

    detected_objects = []

    for result in results:
        for box in result.boxes:

            class_id = int(box.cls[0])

            class_name = model.names[class_id]

            detected_objects.append(class_name)

    return detected_objects