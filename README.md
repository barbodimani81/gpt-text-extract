# 🧠 Persian OCR Extractor with Python & Tesseract

Extract Persian (Farsi) text from any image using the power of **Python** + **Tesseract OCR** — in just a few lines of code!  
This is your minimalist yet powerful OCR tool for handling Persian script. 🇮🇷📄

---

## 🚀 Features

- 🔍 Extract Persian text (`lang="fas"`) from any image
- ⚡ Super simple setup with Python
- 🛠️ Fully customizable
- 🖼️ Works on scanned documents, screenshots, handwriting, etc.

---

## 🧪 Code

```python
from PIL import Image
import pytesseract

# Path to your image
image_path = "/Users/barbod/Desktop/29.png"

# Path to Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r"/opt/homebrew/bin/tesseract"

# Extract Persian text
text = pytesseract.image_to_string(Image.open(image_path), lang="fas")
print(text)