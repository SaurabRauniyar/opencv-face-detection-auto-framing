# Real-Time Face Detection, Tracking & Auto-Framing

**A Python and OpenCV computer vision project**

A real-time computer vision prototype that detects faces from a webcam, smooths bounding box movement, and automatically adjusts digital camera framing based on a person's position.

The project explores fundamental concepts used in intelligent video conferencing systems, including face detection, temporal smoothing, region-of-interest selection, and camera framing.

## Project Overview

Modern video collaboration systems use computer vision to enhance meeting experiences by detecting participants and adjusting the camera view.

This project implements a simplified version of these capabilities using Python and OpenCV.

The development follows four incremental stages:

| Module | Description |
|---|---|
| `camera.py` | Captures and displays live webcam video |
| `face_detection.py` | Detects faces and draws bounding boxes |
| `face_tracking.py` | Reduces bounding box jitter using exponential smoothing |
| `auto_framing.py` | Dynamically adjusts the displayed video crop based on face position |

## Key Features

**1. Real-Time Webcam Capture**

Captures and displays live video frames using OpenCV's `VideoCapture` interface.

**2. Face Detection**

Uses a pretrained Haar Cascade classifier to identify frontal faces in video frames and draw bounding boxes around detected faces.

**3. Smoothed Face Tracking**

Uses exponential smoothing to reduce sudden changes in bounding box position and size.

The smoothed position is calculated as:

`Smoothed = α × Current Detection + (1 − α) × Previous Smoothed Position`

A lower smoothing factor provides steadier movement but increases response delay.

**4. Automatic Camera Framing**

Implements software-based camera framing by:

1. Detecting the largest visible face.
2. Calculating its center position.
3. Applying smoothing to camera movement.
4. Using a dead zone to prevent unnecessary adjustments.
5. Cropping and resizing the video to follow the person's position.

This simulates camera movement without physically rotating the webcam.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| OpenCV | Video capture, face detection and image processing |
| Haar Cascade | Pretrained frontal-face detection |
| Exponential smoothing | Stabilizing face bounding boxes and crop movement |
| NumPy | Array processing dependency |

## Project Structure

```text
opencv-face-detection-auto-framing/
│
├── camera.py
├── face_detection.py
├── face_tracking.py
├── auto_framing.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Getting Started

**1. Clone the repository**

```bash
git clone https://github.com/SaurabRauniyar/opencv-face-detection-auto-framing.git
cd opencv-face-detection-auto-framing
```

**2. Create a virtual environment**

```bash
python3 -m venv venv
source venv/bin/activate
```

**3. Install dependencies**

```bash
python3 -m pip install -r requirements.txt
```

**4. Run the modules**

Basic webcam:

```bash
python3 camera.py
```

Face detection:

```bash
python3 face_detection.py
```

Smoothed face tracking:

```bash
python3 face_tracking.py
```

Automatic framing:

```bash
python3 auto_framing.py
```

Press **Q** while the OpenCV camera window is active to exit.

A working webcam and camera access permission are required.

## Computer Vision Pipeline

```text
           Webcam Input
                |
                v
         Capture Video Frame
                |
                v
       Convert Frame to Grayscale
                |
                v
       Haar Cascade Face Detection
                |
                v
       Extract Face Bounding Box
                |
                v
        Temporal Smoothing
                |
                v
       Calculate Face Position
                |
                v
       Apply Camera Framing Logic
                |
                v
         Crop and Resize Frame
                |
                v
           Video Output
```

This illustrates the combined processing concepts. Each Python file is independently executable.

## Technical Concepts Explored

**Video Processing:** Working with live camera frames and OpenCV image operations.

**Object Detection:** Locating frontal faces and obtaining their bounding box coordinates.

**Temporal Smoothing:** Reducing frame-to-frame variations in detected face positions.

**Region of Interest (ROI):** Selecting and cropping a specific region within an image.

**Camera Framing:** Adjusting the digital camera view based on the detected subject position.

**Real-Time Processing:** Continuously processing and displaying incoming webcam frames.

## Current Limitations

This project is an experimental prototype rather than a production-ready intelligent camera system.

The Haar Cascade classifier may struggle with extreme head angles, occlusion, or challenging lighting.

The tracking implementation uses detection and temporal smoothing rather than a dedicated multi-object tracking algorithm.

Auto-framing uses a fixed zoom factor and digital cropping, so its movement is limited by the original webcam field of view.

The current implementation prioritizes the largest detected face and does not identify individual people or active speakers.

## Future Improvements

Potential extensions include:

1. Multi-face tracking with persistent tracking IDs.
2. Face landmark detection.
3. Deep learning-based face detection.
4. Adaptive zoom based on subject size and movement.
5. Active-speaker-aware camera selection using audio and visual signals.
6. Performance benchmarking using frame rate, latency, and tracking stability.

## Project Motivation

I developed this project to strengthen my practical understanding of computer vision and real-time video processing.

My goal was to progress from basic webcam integration to a working face detection and digital auto-framing prototype, while exploring the engineering challenges associated with detection stability, subject movement, and responsive camera behavior.

The project provides a foundation for further experimentation with intelligent video collaboration systems.

## Author

**Saurab Rauniyar**

[GitHub Profile](https://github.com/SaurabRauniyar)