import torch
import cv2

# Load YOLOv5 model using torch.hub
model = torch.hub.load('ultralytics/yolov7', 'yolov7s', pretrained=True)

# Set a confidence threshold (adjust as needed)
CONFIDENCE_THRESHOLD = 0

# Open webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break  # Stop if no frame is captured
    frame = cv2.flip(frame, 1)

    # Convert frame to RGB (YOLO expects RGB format)
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Perform inference
    results = model(img)

    # Process results
    for det in results.xyxy[0]:  # xyxy format (x1, y1, x2, y2, confidence, class)
        x1, y1, x2, y2, conf, cls = map(int, det[:6])
        
        if model.names[cls] in ['book', 'cell phone', 'bottles' , 'cup']:
            label = f"{model.names[int(cls)]} {conf:.3f}"

            # Draw bounding box for similar objects
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Show frame with detections

    cv2.imshow("YOLOv5 Real-Time Detection", frame)

    # Exit with 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
