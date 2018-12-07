import pytesseract as pt

from PIL import Image

image = Image.open('./number.jpg')

text = pt.image_to_string(image)

print(text)