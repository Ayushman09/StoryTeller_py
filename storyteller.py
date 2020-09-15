from time import sleep

import pyttsx3 #pip install pyttsx3
import PyPDF2 #pip install PyPDF2

story = open('story.pdf', 'rb') #name of your story(inplace of story.pdf) make sure it's in pdf format
pdfReader = PyPDF2.PdfFileReader(story)
pages = pdfReader.numPages
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) #For male voice change the value

for num in range(0, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    engine.say(text)
    engine.runAndWait()
