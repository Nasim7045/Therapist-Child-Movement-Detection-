Child Detection Project
Overview
This project uses computer vision and machine learning to detect and track children in video footage. It integrates the YOLOv5 object detection model and the DeepSort tracking algorithm to identify and track individuals across frames. The system processes video files and outputs a new video with bounding boxes and IDs overlaid on the detected individuals.

Components
YOLOv5 (You Only Look Once Version 5): A state-of-the-art object detection model used to detect objects (in this case, children) in each frame of the video.
DeepSort (Deep Learning-based SORT): An advanced tracking algorithm that associates detections across frames and assigns unique IDs to tracked objects.
Project Structure
scripts/

main.py: The main script to process videos. It handles video input/output, calls the detection and tracking functions, and saves the processed video.
tracker.py: Contains the Tracker class, which initializes and uses DeepSort to track objects across frames.
detector.py: Contains the Detector class, which uses YOLOv5 to detect objects in frames.
data/

videos/: Directory for input video files.
outputs/: Directory for output video files.
requirements.txt: List of Python dependencies required for the project.

Installation
Clone the Repository

bash
Copy code
git clone <repository-url>
cd <repository-directory>
Create and Activate a Virtual Environment

bash
Copy code
python -m venv myenv
source myenv/bin/activate  # On Windows, use `myenv\Scripts\activate`
Install Dependencies

bash
Copy code
pip install -r requirements.txt
Usage
Prepare Your Video

Place your input video file in the data/videos/ directory. Make sure the filename and path in main.py match your video file's location.

Run the Script

Execute the main script to process the video:

bash
Copy code
python scripts/main.py
This will read the video from data/videos/, detect and track objects, and save the output video to data/outputs/.

View Results

After processing, find the output video in the data/outputs/ directory. The video will include bounding boxes and IDs overlaid on detected individuals.

Logic Behind the Project
Detection: YOLOv5 is used to detect objects in each frame of the video. YOLOv5 outputs bounding boxes and confidence scores for detected objects.

Tracking: DeepSort is used to track the detected objects across frames. It associates detections with previously tracked objects and assigns unique IDs to each tracked object.

Integration:

The main script (main.py) reads frames from the video and uses the Detector class to obtain detections.
The Tracker class then updates tracking information based on these detections.
The processed frames, with bounding boxes and IDs, are saved to a new video file.
Troubleshooting
Empty Detections: Ensure that YOLOv5 is properly loaded and the detection model is correctly configured.
Format Errors: Check that the bounding boxes are formatted correctly before passing them to DeepSort. Ensure that all bounding box coordinates are float values.
Video Issues: Ensure the video file path is correct and the video format is supported.