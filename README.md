#  Netra AI - Smart Navigation System for Visually Impaired

Netra AI is an assistant system designed to help visually impaired individuals navigate environments safely. Built on Python and computer vision techniques, Netra AI detects real-time obstacles, estimates object proximity, and provides voice-guided audio feedback.

---

##  Key Features
- **Real-Time Obstacle Detection:** Powered by a lightweight YOLOv8 architecture optimized for low latency.
- **Proximity & Distance Estimation:** Uses camera geometry algorithms to estimate object distance in meters.
- **Spatial Navigation Engine:** Categorizes hazards into **Left**, **Center**, and **Right** zones to guide user movement.
- **Asynchronous Audio Feedback:** Non-blocking Text-to-Speech (TTS) alerts triggered when obstacles enter critical proximity thresholds.

---

##  Tech Stack
- **Language:** Python 3.9+
- **Computer Vision:** OpenCV, Ultralytics YOLOv8
- **Speech Engine:** `pyttsx3`
- **Machine Learning:** PyTorch

---

##  Quick Start & Installation

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/rajxy/Netra-AI-Smart-Navigation.git](https://github.com/rajxy/Netra-AI-Smart-Navigation.git)
   cd Netra-AI-Smart-Navigation
