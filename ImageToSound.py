# importing modules

import os
from gtts import gTTS
from PIL import Image
import pytesseract
# first of all we need to install above module - pip install pytesseract
pytesseract.pytesseract.tesseract_cmd = r"put the path of your installation"
def convert_to_sound(Image):
    try:
        osen_image = Image.open(image)
        text = pytesseract.image_to_string(oprn_image)
        text_file = " ".join(text.split("\n"))
        print(text_file)
        sound = gTTS(text_file, lang = "en")
        sound.save("sound.mp3")
        os.system("sound.mp3")
        return True
    except Exception as bug:
        print("The errore while exeception the code\n",bug)
        return

if __name__ == "__main__":
    image_to_sound("imagetext.jpg")
    input()

