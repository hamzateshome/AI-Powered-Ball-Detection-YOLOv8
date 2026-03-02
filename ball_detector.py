from ultralytics import YOLO
import cv2

# 1. Load a pre-trained YOLOv8 model (Nano version is best for Robotics)
model = YOLO('yolov8n.pt')

def run_detection(source=0): # 0 is your webcam
    # 2. Run inference on the source
    # 'conf=0.5' means only show results with >50% certainty
    results = model.predict(source=source, show=True, conf=0.5, classes=[32]) 
    
    # Class 32 in the COCO dataset is 'sports ball'
    print("Detection Active. Searching for balls...")

if __name__ == "__main__":
    run_detection()
