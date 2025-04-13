# decoder.py
import torch
from torchvision import transforms
from PIL import Image
from model import SteganographyNet

def load_image(path):
    image = Image.open(path).resize((256, 256))
    transform = transforms.ToTensor()
    return transform(image).unsqueeze(0)

def decode(stego_path, output_path):
    model = SteganographyNet()
    model.eval()
    
    stego = load_image(stego_path)
    
    with torch.no_grad():
        _, revealed = model(stego, torch.zeros_like(stego))
        revealed_img = transforms.ToPILImage()(revealed.squeeze())
        revealed_img.save(output_path)
