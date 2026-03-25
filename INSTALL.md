### Local GPU Acceleration Setup
To run the PPE Monitor with your NVIDIA RTX GPU, copy and paste the following block into your terminal:

``` bash
pip install torch torchvision --index-url "[https://download.pytorch.org/whl/cu121](https://download.pytorch.org/whl/cu121)"
pip install -r requirements.txt
python -c "import torch; gpu=torch.cuda.is_available(); print('\n' + '='*25 + f'\n🚀 GPU Status: {'ACTIVE' if gpu else 'NOT FOUND'}\n📍 Device: {torch.cuda.get_device_name(0) if gpu else 'CPU'}\n' + '='*25)"
```
