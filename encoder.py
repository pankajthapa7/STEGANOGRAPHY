
import torch
from torchvision import transforms
from PIL import Image
from model import SteganographyNet

def load_image(path):
    image = Image.open(path).resize((256, 256))
    transform = transforms.ToTensor()
    return transform(image).unsqueeze(0)

def encode(cover_path, secret_path, output_path):
    model = SteganographyNet()
    model.eval()
    
    cover = load_image(cover_path)
    secret = load_image(secret_path)
    
    with torch.no_grad():
        stego, _ = model(cover, secret)
        stego_img = transforms.ToPILImage()(stego.squeeze())
        stego_img.save(output_path)
