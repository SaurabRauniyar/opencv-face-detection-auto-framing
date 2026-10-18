<div align="center">
  <img src="assets/project-banner.png" alt="Illustrated banner for the face detection and auto-framing project" width="100%" />
  <br /><br />
  <img src="https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.9+" />
  <img src="https://img.shields.io/badge/OpenCV-4.10-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white" alt="OpenCV 4.10" />
  <img src="https://img.shields.io/badge/Computer%20Vision-Real%20Time-00A86B?style=for-the-badge" alt="Real-time computer vision" />
  <br /><br />
  <b>From webcam capture to face-aware digital framing — four small, runnable Python demos.</b>
  <br />
  <sub>Built to learn real-time computer vision step by step.</sub>
  <br /><br />
  <a href="#-quick-start">🚀 Quick Start</a> &nbsp;•&nbsp;
  <a href="#-explore-the-four-demos">🎬 Demos</a> &nbsp;•&nbsp;
  <a href="#-how-it-works">🧠 How It Works</a> &nbsp;•&nbsp;
  <a href="#-roadmap">🔭 Roadmap</a>
</div>

> [!NOTE]
> The banner is a **concept illustration**, not a screenshot of the program. An actual webcam demonstration can be added below when recorded.

## ✨ At a glance

| 🎥 **Live webcam** | 🟩 **Face detection** | 🎯 **Smooth bounding box** | 🔎 **Auto-framing** |
|:---:|:---:|:---:|:---:|
| Read frames in real time | Detect frontal faces with Haar Cascade | Reduce frame-to-frame jitter | Adjust a digital crop to follow the main face |

## 🎬 Explore the four demos

Each script runs **independently**. Start with the basic camera and work toward auto-framing.

| Stage | File | What you'll see | Run |
|:---:|---|---|---|
| **01** | `camera.py` | Live webcam feed | `python3 camera.py` |
| **02** | `face_detection.py` | Green boxes around detected faces | `python3 face_detection.py` |
| **03** | `face_tracking.py` | A less jittery bounding box | `python3 face_tracking.py` |
| **04** | `auto_framing.py` | Original and digitally reframed webcam views | `python3 auto_framing.py` |

**📽️ Demo preview (coming soon):** Record a short screen capture of your working webcam and place it at `assets/demo.gif`. Then replace this sentence with `![Live demo](assets/demo.gif)`.

## 🧠 How it works

```mermaid
flowchart LR
    A[📷 Webcam frame] --> B[Grayscale image]
    B --> C[Haar Cascade face detector]
    C --> D[Face bounding box]
    D --> E[Exponential smoothing]
    E --> F[Face center]
    F --> G[Dead-zone camera control]
    G --> H[Crop and resize]
    H --> I[🖥️ Auto-framed view]
```

**Face detection.** A pretrained Haar Cascade classifier locates frontal faces and outputs `(x, y, width, height)` bounding boxes.

**Temporal smoothing.** Rather than drawing every new detection directly, we blend it with the previous displayed box:

```text
smoothed = alpha × detected + (1 − alpha) × previous_smoothed
```

Smaller `alpha` values reduce jitter but cause the box to respond more slowly.

**Digital auto-framing.** We find the face center, move the crop center gradually when the face leaves a *dead zone*, then crop and resize the source frame. This **does not physically rotate** the webcam. Reframing is limited by the original image boundaries.

## 🚀 Quick start

**1. Clone**

```bash
git clone https://github.com/SaurabRauniyar/opencv-face-detection-auto-framing.git
cd opencv-face-detection-auto-framing
```

**2. Create and activate a virtual environment** (macOS / Linux)

```bash
python3 -m venv venv
source venv/bin/activate
```

**3. Install dependencies**

```bash
python3 -m pip install -r requirements.txt
```

**4. Choose a demo**

```bash
python3 camera.py
# or
python3 face_detection.py
# or
python3 face_tracking.py
# or
python3 auto_framing.py
```

**To close the camera:** Click the OpenCV window and press **Q**. Make sure another app is not occupying your webcam, and grant camera permission when macOS asks.

## 📁 Project structure

```text
opencv-face-detection-auto-framing/
├── assets/
│   └── project-banner.png
├── camera.py
├── face_detection.py
├── face_tracking.py
├── auto_framing.py
├── requirements.txt
├── .gitignore
└── README.md
```

## 🛠️ Tools and techniques

| Tool / concept | Why it's here |
|---|---|
| **Python** | Readable, modular implementation |
| **OpenCV** | Camera I/O, image transforms, detection, drawing, video windows |
| **Haar Cascade** | Pretrained frontal-face detector |
| **Exponential smoothing** | Reduce small changes in bounding box location and crop position |
| **Dead zone** | Avoid moving the output for tiny face movements |
| **ROI cropping** | Simulate camera panning by selecting a region of the frame |

## 💡 What I learned

- Reading and displaying live video frame by frame.
- Detecting faces and interpreting `(x, y, w, h)` coordinates.
- Balancing **responsiveness vs. stability** with smoothing.
- Keeping the target near the center using **cropping, interpolation, and dead-zone logic**.
- Organizing a computer vision prototype into small, independently runnable demos.

## ⚠️ Limitations

This is a **learning prototype**, not production-grade camera intelligence. It detects mainly frontal faces; unusual angles, lighting, and occlusion can reduce reliability. "Tracking" currently means **detection plus temporal smoothing**, not persistent identity tracking. Auto-framing follows the **largest detected face**, uses a fixed digital zoom, and cannot see beyond the webcam's original field of view. No identity recognition or active-speaker detection is implemented.

## 🔭 Roadmap

- [ ] Record and embed an actual demonstration GIF.
- [ ] Add multi-person tracking with persistent IDs.
- [ ] Explore face landmarks and improved detectors.
- [ ] Test adaptive zoom and more natural camera transitions.
- [ ] Benchmark frame rate, latency, and stability.
- [ ] Explore audio-visual active-speaker framing.

## 👤 Author

**Saurab Rauniyar**  
[GitHub @SaurabRauniyar](https://github.com/SaurabRauniyar)

<div align="center">
  <sub>Made with Python and OpenCV • Computer vision learning project</sub>
</div>
