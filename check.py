from ultralytics import YOLO

# Load your custom-trained YOLOv8n model
model = YOLO('id_card_model/yolo_id_detector2/weights/best.pt')

import cv2

# Initialize the webcam
cap = cv2.VideoCapture(0)
cap.set(3, 640)  # Set width
cap.set(4, 480)  # Set height

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Perform inference on the frame
    results = model(frame)

    # Render results on the frame
    annotated_frame = results[0].plot()

    # Display the annotated frame
    cv2.imshow('ID Card Detection', annotated_frame)

    # Exit the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()