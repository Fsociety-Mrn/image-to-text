import easyocr
import cv2

# Initialize the EasyOCR reader
reader = easyocr.Reader(['en'], gpu=False)

# Read the image
image_path = 'image/back.jpeg'
image = cv2.imread(image_path)

# Perform OCR
results = reader.readtext(image_path)

# Define a confidence threshold
confidence_threshold = 0.3  # Adjust this value as needed

# Iterate through the OCR results
for (bbox, text, score) in results:
    
    print(score)
    if score >= confidence_threshold:  # Only consider results above the threshold
        # Unpack the bounding box coordinates
        (top_left, top_right, bottom_right, bottom_left) = bbox
        top_left = tuple(map(int, top_left))
        bottom_right = tuple(map(int, bottom_right))

        # Draw a rectangle around the detected text
        cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 1)
        
        # Put the detected text on the image
        cv2.putText(image, text, (top_left[0], top_left[1] + 20), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

# Display the output
cv2.imshow('annotated', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
