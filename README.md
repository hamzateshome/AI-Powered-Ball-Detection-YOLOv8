AI-Powered Ball Detection for Robotics
This project transitions from traditional CV (color-masking) to Deep Learning-based Object Detection.

🚀 Key Features:
Model: YOLOv8 (Nano) for high-speed inference.

Robustness: Unlike HSV masking, this ML model handles shadows, reflections, and partial occlusions.

Hardware Ready: Designed to be deployed on Edge AI hardware like NVIDIA Jetson Nano or Raspberry Pi 5.

🔧 Mechatronics Logic:
The output of this detection (X, Y coordinates) is designed to be fed into a PID Controller to command servo motors for real-time tracking.
