### Construction Site PPE Compliance Monitor
A real-time computer vision application designed for workplace safety monitoring. This system utilizes a custom-trained YOLOv8 model to detect and verify the use of Protective Personal Equipment (PPE) in industrial and construction environments.

## System Features
Detection Classes: Identifies Helmets, Safety Vests, Boots, and Person.

Automated Alerts: Provides immediate visual notification for safety violations.

Input Versatility: Supports high-resolution image uploads and live webcam snapshots.

Performance Optimization: Optimized for low-latency inference using the YOLOv8 architecture.

Model Performance and Validation

The model was validated using a standard COCO-format dataset to ensure reliability in cluttered construction environments.

## Core Metrics Table

<img width="668" height="268" alt="image" src="https://github.com/user-attachments/assets/e8827879-446b-4961-a887-b34bf5252da1" />


| Confusion Matrix | F1-Confidence Curve |
| :---: | :---: |
| <img src="https://github.com/user-attachments/assets/24e1832f-c6e9-49d9-a148-404b1e282431" width="400" alt="Confusion Matrix"> | <img src="https://github.com/user-attachments/assets/51c7a4ac-93c6-486a-97c6-022f13992d0b" width="400" alt="F1 Curve"> |

## Technical Stack

Architecture: YOLOv8 (Ultralytics)

Framework: Streamlit

Libraries: OpenCV, NumPy, Pillow

Environment: Python 3.11+


## Installation and Local Development(Command Prompt)

**1. Environment Setup** Create and activate a virtual environment on Windows:
```batch
python -m venv venv_311
venv_311\Scripts\activate
```

**2. Dependency Installation** Install the required libraries:
```bash
pip install -r requirements.txt
```
Note for GPU Users: The command above installs the standard CPU version of PyTorch. If you have an NVIDIA GPU and want to use it for faster inference, please follow the instructions at [pytorch.org](https://pytorch.org/) to install the version compatible with your CUDA version.

**3. Execution** Launch the Streamlit interface:
```bash
streamlit run app.py
```
Note on Hardware: This application is optimized for NVIDIA GPUs using CUDA. If no GPU is detected, the system will automatically switch to CPU mode (inference may be slower).

## Live Demo
Experience the monitor in action here: [ppe-compliance-monitor.streamlit.app](https://ppe-compliance-monitor.streamlit.app/)
**Note:** The live web version operates on shared cloud CPUs. For real-time, high-performance inference using NVIDIA CUDA (RTX 50-series), please run the repository locally.
