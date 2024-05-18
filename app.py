from flask import Flask, render_template, Response
from ultralytics import YOLO
import cv2
import supervision as sv
import numpy as np

app = Flask(__name__)

# Initialize the YOLO model with the custom weight file
bbox_model = YOLO('yolov8s-world.pt')

# Define custom classes for earthquake and warzone scenarios
custom_classes = [
    "person", "car", "bus", "truck", "motorcycle", "bicycle", "ambulance",
    "fire truck", "police car", "building", "rubble", "debris", "bridge",
    "road", "traffic light", "stop sign", "fire hydrant", "first aid kit",
    "fire extinguisher", "backpack", "suitcase",
    "cell phone", "mouse", "water bottle", "watch"
]
bbox_model.set_classes(custom_classes)

# Initialize annotators
label_annotator = sv.LabelAnnotator()

# Mode: "person" for person detection, "heat_map" for heat map
mode = "person"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/set_mode/<new_mode>')
def set_mode(new_mode):
    global mode
    mode = new_mode
    print(f"Mode set to: {mode}")  # Debug print
    return "Mode set to " + new_mode


def generate_frames():
    global mode
    # 0 is typically the built-in webcam; change if using an external webcam
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Perform object detection
        bbox_result = bbox_model.predict(frame)[0]
        bbox_detections = sv.Detections.from_ultralytics(bbox_result)

        # Annotate the frame with bounding boxes and labels
        annotated_bbox_frame = label_annotator.annotate(
            scene=frame.copy(),
            detections=bbox_detections
        )

        if mode == "heat_map":
            # Create a heat map based on the confidence levels
            heat_map = np.zeros(
                (frame.shape[0], frame.shape[1]), dtype=np.float32)
            for detection in bbox_detections:
                bbox = detection[0]
                confidence = detection[2]
                x1, y1, x2, y2 = map(int, bbox)
                heat_map[y1:y2, x1:x2] += confidence

            # Normalize the heat map and apply color map
            heat_map = np.clip(heat_map, 0, 1)
            heat_map = np.uint8(255 * heat_map)
            heat_map_colored = cv2.applyColorMap(heat_map, cv2.COLORMAP_JET)

            # Overlay the heat map on the annotated frame
            annotated_bbox_frame = cv2.addWeighted(
                annotated_bbox_frame, 0.6, heat_map_colored, 0.4, 0)

        # Check for cell phone detection and add warning message if detected
        for detection in bbox_detections:
            class_id = int(detection[3])
            if custom_classes[class_id] == 'cell phone':
                cv2.putText(
                    annotated_bbox_frame, 'Warning: Cell Phone Detected!',
                    (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA
                )
                break

        ret, buffer = cv2.imencode('.jpg', annotated_bbox_frame)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__":
    app.run(debug=True)
