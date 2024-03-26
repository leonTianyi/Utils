import torch
import cv2

class Track2D:
    def __init__(self, track_id, bbox, score, class_id):
        self.track_id = track_id
        self.bbox = bbox  # (x1, y1, x2, y2)
        self.score = score
        self.class_id = class_id

    def __repr__(self):
        return f"Track2D(id={self.track_id}, bbox={self.bbox}, score={self.score}, class={self.class_id})"



########################
multitracker = cv2.MultiTracker_create()

# Load YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

# Object detection and tracking loop
while True:
    # Get frame (e.g., from a video stream)
    frame = ...

    # Run YOLOv5 object detection
    detections = model(frame)

    # Convert detections to OpenCV format
    boxes = []
    for detection in detections:
        x1, y1, x2, y2 = [int(val) for val in detection[:4]]
        boxes.append((x1, y1, x2 - x1, y2 - y1))

    # Initialize the multitracker with new detections
    if multitracker.empty():
        for box in boxes:
            multitracker.add(cv2.TrackerMedianFlow_create(), frame, box)
    else:
        multitracker.clear()
        for box in boxes:
            multitracker.add(cv2.TrackerMedianFlow_create(), frame, box)

    # Update the multitracker
    success, tracked_boxes = multitracker.update(frame)

    # Draw bounding boxes and track IDs on the frame
    for i, tracked_box in enumerate(tracked_boxes):
        x, y, w, h = [int(val) for val in tracked_box]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, f"ID: {i}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (36, 255, 12), 2)

    # Display or process the frame with tracked objects
    ...

#### Making track into specific datatype
tracks = []
for track in tracker.tracks:
    x1, y1, x2, y2 = [int(i) for i in track.box]
    bbox = (x1, y1, x2, y2)
    track_id = int(track.id)
    score = track.score
    class_id = int(track.class_id)
    tracks.append(Track2D(track_id, bbox, score, class_id))
