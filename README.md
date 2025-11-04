# Smart Vehicle Violation Detection System

## Overview
This project detects **helmet** and **seatbelt** violations using a **YOLOv8** model and **OpenCV**.  
It highlights violators in video frames, saves snapshots, and logs details automatically.

> 🚫 *Traffic light violation excluded as per project scope.*

---

## Features
- Helmet detection ✅  
- Seatbelt detection ✅  
- Real-time webcam or video file input ✅  
- Violation snapshot saving ✅  
- Violation logging to CSV ✅  
- Optional Streamlit dashboard ✅  

---

## Tools Used
- Python 3.x  
- OpenCV  
- NumPy  
- Ultralytics YOLOv8  
- Pandas  
- Streamlit *(optional)*  

---

##  Setup
```bash
git clone https://github.com/<your-username>/smart-vehicle-detection.git
cd smart-vehicle-detection
pip install ultralytics opencv-python pandas streamlit
```

###  Run Detection

For webcam:
```bash
python main.py
```

For video file:
```bash
python main.py --source path_to_video.mp4
```
###  View Results

Violations and images will be saved in the violations/ folder.

Logs will be saved to logs/violations.csv.
