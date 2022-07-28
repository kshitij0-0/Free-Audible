import os
import cv2
import pytesseract
import pyttsx3
from gtts import gTTS
from pdf2image import convert_from_path

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
poppler_path = r'C:\Program Files\poppler-0.68.0\bin'
pdf_path=r'C:\Users\kshit\OneDrive\Desktop\Machine Learning\Free Audible\2.pdf'

engine = pyttsx3.init()

images = convert_from_path(pdf_path=pdf_path,poppler_path=poppler_path)
for i in range(len(images)):
    images[i].save('page'+ str(i+1) +'.png', 'PNG')
for h in range(1,i):
    img = cv2.imread('page'+str(h)+'.png')

    text = pytesseract.image_to_string(img)
    file = open('output.txt','a')
    file.write(text)

mytext = open("output.txt", "r").read()
engine.say(mytext)
engine.runAndWait()



