import os
from ultralytics import YOLO
import cv2
import torch


# Check if CUDA is available
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")

# Step 1: Define Paths
dataset_path = "id_dataset"  # Change this to your dataset folder
data_yaml = "id_dataset/data.yaml"  # YOLO dataset config file

# Step 2: Load YOLOv8 Model (Pretrained)
model = YOLO("yolov8n.pt")  # You can also use 'yolov8m.pt' or 'yolov8l.pt'

# Step 3: Train Model
model.train(
    data=data_yaml,   # Dataset YAML file
    epochs=50,        # Training epochs
    imgsz=640,        # Image size
    batch=8,          # Batch size
    device=device,    # Use GPU if available
    workers=4,        # Parallel processing
    project="id_card_model",  # Save trained model in this folder
    name="yolo_id_detector"   # Model run name
)

# Step 4: Test the Model on a New Image
# test_image = "test_images/id_test.jpg"  # Change this to your test image path
# results = model(test_image, save=True, conf=0.5)

# # Display the detected result
# for result in results:
#     img = cv2.imread(test_image)
#     for box in result.boxes:
#         x1, y1, x2, y2 = map(int, box.xyxy[0])  # Bounding box coordinates
#         confidence = box.conf[0].item()  # Confidence score
#         cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
#         cv2.putText(img, f"ID Card {confidence:.2f}", (x1, y1 - 10), 
#                     cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    
#     cv2.imshow("Detected ID Card", img)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

# Step 5: Export the Model for Deployment
model.export(format="onnx")  # Convert model to ONNX format
model.export(format="torchscript")  # Convert model to TorchScript
