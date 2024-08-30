from deep_sort_realtime.deepsort_tracker import DeepSort

class Tracker:
    def __init__(self):
        self.tracker = DeepSort()

    def update(self, detections, frame):
        print("Raw detections:", detections)

        # Convert detections to the required format: only bbox coordinates
        formatted_detections = self.format_detections(detections)
        print("Formatted detections:", formatted_detections)
        
        # Pass the correctly formatted detections to the tracker
        tracks = self.tracker.update_tracks(formatted_detections, frame=frame)
        return tracks

    def format_detections(self, detections):
        formatted_detections = []
        for det in detections:
            if len(det) >= 4:
                # Ensure bbox values are in the correct format
                bbox = [float(det[0]), float(det[1]), float(det[2]), float(det[3])]
                formatted_detections.append(bbox)
        print("Formatted detections:", formatted_detections)  # Debug output
        return formatted_detections
