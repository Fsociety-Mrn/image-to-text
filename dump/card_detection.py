import easyocr
import cv2
import time

def video_stream_with_ocr(refresh_rate=5):
    # Initialize the EasyOCR reader
    reader = easyocr.Reader(['en'], gpu=False)

    # Open the default camera (use a file path instead of 0 to stream a video file)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Unable to access the camera.")
        return

    print("Press 'q' to quit the video stream.")

    last_ocr_time = time.time()  # Track the last time OCR was performed
    ocr_results = []  # Store the results of the last OCR run

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        if not ret:
            print("Error: Unable to read frame.")
            break

        # Get the current time
        current_time = time.time()

        # Perform OCR every 5 seconds
        if current_time - last_ocr_time >= refresh_rate:
            ocr_results = reader.readtext(frame)
            last_ocr_time = current_time

        # Iterate through the OCR results and annotate the frame
        for (bbox, text, score) in ocr_results:
            # Unpack the bounding box coordinates
            (top_left, top_right, bottom_right, bottom_left) = bbox
            top_left = tuple(map(int, top_left))
            bottom_right = tuple(map(int, bottom_right))

            # Draw a rectangle around the detected text
            cv2.rectangle(frame, top_left, bottom_right, (0, 255, 0), 1)

            # Put the detected text on the frame
            cv2.putText(frame, text, (top_left[0], top_left[1] - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

        # Display the frame
        cv2.imshow("Video Stream with OCR", frame)

        # Exit the stream when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture object and close display windows
    cap.release()
    cv2.destroyAllWindows()

# Run the video streaming with OCR and a 5-second refresh rate
video_stream_with_ocr(refresh_rate=5)
 