# scripts/main.py
import cv2
from detector import Detector
from tracker import Tracker

def format_detections(detections):
    formatted_detections = []
    for det in detections:
        if len(det) >= 4:
            # Extract bounding box coordinates
            bbox = [float(det[0]), float(det[1]), float(det[2]), float(det[3])]
            formatted_detections.append(bbox)
    print("Formatted detections for DeepSort:", formatted_detections)  # Print for debugging
    return formatted_detections

def process_video(input_video_path, output_video_path):
    # Initialize detector and tracker
    detector = Detector()
    tracker = Tracker()

    # Open video file
    cap = cv2.VideoCapture(input_video_path)
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    out = cv2.VideoWriter(output_video_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (frame_width, frame_height))

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Detect persons
        detections = detector.detect(frame)

        # Update tracker
        formatted_detections = format_detections(detections)
        tracks = tracker.update(formatted_detections, frame)

        # Draw bounding boxes and IDs
        for track in tracks:
            bbox = track.to_tlbr()
            track_id = track.track_id
            color = (0, 255, 0)  # Green for tracking
            cv2.rectangle(frame, (int(bbox[0]), int(bbox[1])), (int(bbox[2]), int(bbox[3])), color, 2)
            cv2.putText(frame, f'ID: {track_id}', (int(bbox[0]), int(bbox[1]) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

        # Write frame to output video
        out.write(frame)

        # Display the resulting frame (optional)
        cv2.imshow('Frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release resources
    cap.release()
    out.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    input_video_path = 'C:/Users/ASUS/THERAPIST CHILD DETECTION PROJECT/data/videos/videoplayback.mp4' #replace your video titles here
    output_video_path = 'C:/Users/ASUS/THERAPIST CHILD DETECTION PROJECT/data/outputs/output.mp4'
    process_video(input_video_path, output_video_path)
