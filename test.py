import torch

ckpt = torch.load(
    r"C:\Users\aroli\runs\detect\pothole_y8m\weights\best.pt",
    map_location="cpu",
    weights_only=False  # IMPORTANT
)

print(type(ckpt))