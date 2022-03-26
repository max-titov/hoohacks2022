from PIL import Image, ImageEnhance
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# assigning an image from the source path
img = Image.open("woolftext.jpeg")
# adding some sharpness and contrast to the image
enhancer1 = ImageEnhance.Sharpness(img)
enhancer2 = ImageEnhance.Contrast(img)
img_edit = enhancer1.enhance(20.0)
img_edit = enhancer2.enhance(1.5)
# save the new image
img_edit.save("edited_image.png")
# converts the image to result and saves it into result variable
result = pytesseract.image_to_string(img_edit)
print(result)
