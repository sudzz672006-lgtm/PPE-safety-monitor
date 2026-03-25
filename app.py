import streamlit as st
from ultralytics import YOLO
from PIL import Image
import cv2
import numpy as np
import os
import torch

# --- Page Configuration ---
st.set_page_config(page_title="PPE Safety Monitor", layout="wide")
st.title("🏗️ Construction Site PPE Compliance Monitor")

# --- 1. Load Model ---
@st.cache_resource 
def load_model():
    # This logic finds 'best.pt' regardless of if you are on Windows or Linux
    model_path = os.path.join(os.getcwd(), 'best.pt')
    
    # Check if the file actually exists to prevent a crash
    if not os.path.exists(model_path):
        st.error(f"Error: {model_path} not found! Please place best.pt in the same folder as app.py")
        return None
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    
    return YOLO(model_path).to(device)
    
model = load_model()

# --- 2. Sidebar Controls ---
st.sidebar.header("Settings")
conf_threshold = st.sidebar.slider("Confidence Threshold", 0.0, 1.0, 0.25)
iou_threshold = st.sidebar.slider("IoU (Merge) Threshold", 0.0, 1.0, 0.45)
source_option = st.sidebar.radio("Select Input Source:", ("Upload Image", "Live Webcam"))

# --- 3. Prediction Function ---
def process_image(img):
    if model is None:
        return None
        
    img_array = np.array(img)
    img_array = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR) 
    
    # Run Prediction - Using list() to avoid generator error
    results = list(model.predict(
        source=img_array, 
        conf=conf_threshold, 
        iou=iou_threshold, 
        imgsz=640, 
        rect=True
    ))
    
    res = results[0]
    st.write(f"Debug: Found {len(res.boxes)} objects in this image.")
    
    # Standard YOLO boxes
    annotated_img = res.plot() 
    annotated_img = cv2.cvtColor(annotated_img, cv2.COLOR_BGR2RGB)
    
    # --- Violation Logic ---
    classes = res.boxes.cls.tolist()
    # 0: Boots, 1: Helmet, 2: Person, 3: Vest
    has_person = 2 in classes
    has_helmet = 1 in classes
    has_vest = 3 in classes
    
    person_count = len(res.boxes.cls[res.boxes.cls == 2]) 
    
    if has_person:
        violations = []
        if not has_helmet: violations.append("NO HELMET")
        if not has_vest: violations.append("NO VEST")
        
        if violations:
            msg = " | ".join(violations)
            cv2.putText(annotated_img, f"ALERT: {msg}", (50, 80), 
                        cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 0, 0), 4)
            st.error(f"⚠️ Safety Violation: {msg} (Detected in {person_count} tracked zones)")
        else:
            st.success(f"✅ Compliance Verified for {person_count} detected worker(s).")
    else:
        st.info("No person detected in current frame.")        
    
    return annotated_img

# --- 4. Main Interface ---
if source_option == "Upload Image":
    uploaded_file = st.file_uploader("Upload a site photo...", type=['jpg', 'jpeg', 'png'])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        
        col1, col2 = st.columns(2)
        with col1:
            st.info("Original")
            st.image(image, width='stretch')
        
        if st.button("Run Compliance Check"):
            with col2:
                processed_img = process_image(image)
                if processed_img is not None:
                    st.info("Detection Result")
                    st.image(processed_img, width='stretch')

elif source_option == "Live Webcam":
    img_file = st.camera_input("Take a snapshot")
    if img_file:
        img = Image.open(img_file)
        processed_img = process_image(img)
        if processed_img is not None:
            st.image(processed_img, width='stretch')
