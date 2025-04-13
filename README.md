# STEGANOGRAPHY


# Image Steganography

Hide and reveal secret images using convolutional neural networks. This project demonstrates how deep learning can be used to perform image steganography—concealing a secret image within another (cover) image and recovering it with minimal loss.

---

##  Features

-  Hides a secret image inside a cover image using CNNs
-  Reveals hidden image from the generated stego image
-  Clean modular codebase
-  Easily extendable with advanced models (GANs, transformers, etc.)
-  Small footprint for testing and experimentation

---

##  How It Works

The model takes two input images:
- **Cover Image**: Visible image to embed secret into.
- **Secret Image**: The image to hide.

### Architecture
- **Encoder**: Combines cover and secret into a stego image.
- **Decoder**: Extracts the hidden secret image from the stego image.

---

