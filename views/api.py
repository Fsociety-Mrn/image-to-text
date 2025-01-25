import easyocr
import cv2
import numpy as np

from flask import Blueprint,request,jsonify,json,Response

api = Blueprint('api', __name__)
reader = easyocr.Reader(['en'], gpu=False)


def easy_ocr(image):
    results = reader.readtext(image)
    return (
        [{"row": i + 1, "text": text} for i, (_, text, _) in enumerate(results)] 
    )
    
    
@api.route('/api/receive-image', methods=['POST'])
def receive_image():
    
    file = request.files.get('file')
    
    if not file:
        return jsonify({"error": "No file provided"}), 400
    
    try:

        file_bytes = file.read()
        np_array = np.frombuffer(file_bytes, np.uint8)
        image = cv2.imdecode(np_array, cv2.IMREAD_COLOR)
        
        if image is None:
            return jsonify({"error": "Failed to decode image"}), 400

        result = easy_ocr(image)
        if result is None:
            return jsonify(
                {
                    "data": "No text detected in the image",
                    "error": True
                }
            ), 200
        
        return jsonify(
            { 
                "data":result,
                "error": False
            }
        ), 200

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500



@api.route('/video-feed')
def video_feed():
    camera = cv2.VideoCapture(0)  # Set height to 1080p
    return Response(generate_video(camera), mimetype='multipart/x-mixed-replace; boundary=frame')


def generate_video(camera):
    while True:
        # Capture video frame-by-frame
        success, frame = camera.read()
        if not success:
            break
        else:
            # Encode the frame into JPEG format
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            # Yield the frame data in byte format
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')