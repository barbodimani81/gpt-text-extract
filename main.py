from PIL import Image
import pytesseract

# Path to your image
image_path = "/Users/barbod/Desktop/29.png"

# Specify the Tesseract executable path
pytesseract.pytesseract.tesseract_cmd = r"/opt/homebrew/bin/tesseract"

# Extract Persian text
text = pytesseract.image_to_string(Image.open(image_path), lang="fas")
print(text)
