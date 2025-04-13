
from encoder import encode
from decoder import decode

if __name__ == "__main__":
    cover = "data/cover_images/sample.jpg"
    secret = "data/secret_data/secret.jpg"
    stego = "data/output/stego.png"
    revealed = "data/output/revealed.png"

    encode(cover, secret, stego)
    print("Stego image created.")

    decode(stego, revealed)
    print("Secret image revealed.")
