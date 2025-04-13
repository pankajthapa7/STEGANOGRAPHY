
import torch.nn as nn

class SteganographyNet(nn.Module):
    def __init__(self):
        super(SteganographyNet, self).__init__()
        self.encoder = nn.Sequential(
            nn.Conv2d(6, 64, 3, padding=1),
            nn.ReLU(),
            nn.Conv2d(64, 3, 3, padding=1),
            nn.Sigmoid()
        )
        self.decoder = nn.Sequential(
            nn.Conv2d(3, 64, 3, padding=1),
            nn.ReLU(),
            nn.Conv2d(64, 3, 3, padding=1),
            nn.Sigmoid()
        )

    def forward(self, cover, secret):
        x = torch.cat([cover, secret], dim=1)
        stego = self.encoder(x)
        revealed = self.decoder(stego)
        return stego, revealed
