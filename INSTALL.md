### Local GPU Acceleration Setup (NVIDIA RTX)
To run the PPE Monitor with your NVIDIA GPU, copy and paste the following block into your terminal:

```bash
# 1. Create and Activate Virtual Environment
python -m venv venv
# Windows: venv\Scripts\activate | Mac/Linux: source venv/bin/activate
venv\Scripts\activate 

# 2. Install GPU-accelerated PyTorch (CUDA 12.1)
pip install torch torchvision --index-url "https://download.pytorch.org/whl/cu121"

# 3. Install Remaining Project Dependencies
pip install -r requirements.txt

# 4. Verify Hardware Status
python -c "import torch; gpu=torch.cuda.is_available(); print('\n' + '='*25 + f'\n GPU Status: {'ACTIVE' if gpu else 'NOT FOUND'}\n Device: {torch.cuda.get_device_name(0) if gpu else 'CPU'}\n' + '='*25)"
```
