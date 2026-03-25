Construction Site PPE Compliance Monitor
A real-time computer vision application designed for workplace safety monitoring. This system utilizes a custom-trained YOLOv8 model to detect and verify the use of Protective Personal Equipment (PPE) in industrial and construction environments.

System Features
Detection Classes: Identifies Helmets, Safety Vests, Boots, and Person.
Automated Alerts: Provides immediate visual notification for safety violations.
Input Versatility: Supports high-resolution image uploads and live webcam snapshots.
Performance Optimization: Optimized for low-latency inference using the YOLOv8 architecture.

Model Performance and Validation
The model was validated using a standard COCO-format dataset to ensure reliability in cluttered construction environments.

Core Metrics Table
<img width="668" height="268" alt="image" src="https://github.com/user-attachments/assets/e8827879-446b-4961-a887-b34bf5252da1" />

| Confusion Matrix | F1-Confidence Curve |
| :---: | :---: |
| ![Confusion Matrix](results/readme/confusion_matrix_normalized.png) | ![F1 Curve](results/readme/BoxF1_curve.png) |

Technical Stack
Architecture: YOLOv8 (Ultralytics)
Framework: Streamlit
Libraries: OpenCV, NumPy, Pillow
Environment: Python 3.11+

Installation and Local Development

**1. Environment Setup** Create and activate a virtual environment on Windows:
```powershell
python -m venv venv_311
.\venv_311\Scripts\activate
```

**2. Dependency Installation** Install the required libraries:
```bash
pip install -r requirements.txt
```

**3. Execution** Launch the Streamlit interface:
```bash
streamlit run app.py
```
