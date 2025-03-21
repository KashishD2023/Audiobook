import pyttsx3
import PyPDF2
from tkinter.filedialog import *

filename = askopenfilename()
pdfreader = PyPDF2.PdfFileReader(filename)
numpage = pdfreader.numPages

for num in range (0, numpage):
    page = pdfreader.getPage(num)
    text = page.extractText()
    user = pyttsx3.init()
    user.say(text)
    user.runAndWait()