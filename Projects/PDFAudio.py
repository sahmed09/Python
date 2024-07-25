import pyttsx3  # pip install pyttsx3
import PyPDF2  # pip install PyPDF2

"""engine = pyttsx3.init()  # initialization
text = "Hello World"
engine.say(text)
engine.say("Hi, this is Shihab")
engine.say("This is a")
engine.say("Text to speech")
engine.say("Program")
engine.runAndWait()"""

book = open("thinkpython2.pdf", "rb")
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)

friend = pyttsx3.init()
page = pdfReader.getPage(22)
text = page.extractText()
friend.say(text)
friend.runAndWait()

# For multiple pages
"""for i in range(22, pages):
    page = pdfReader.getPage(i)
    text = page.extractText()
    friend.say(text)
    friend.runAndWait()"""
