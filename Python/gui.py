from tkinter import *
import codecs

mainWindow = Tk()
# mainWindow.geometry("368x576")
mainFrame = Frame(mainWindow, borderwidth=0, background="red")
mainFrame.pack()

# champ_label = Label(mainFrame, text="Welcome to Simple Notes !")
# champ_label.pack()
# f = open("test.txt", "r").read()
text = ""

with codecs.open('test.txt', encoding='utf-8') as f:
    for line in f:
        text += line

print(text)
textArea = Text(mainFrame)
textArea.insert(END, text)
# textArea.config(state=DISABLED)
textArea.config(font=("Helvetica", 12))
textArea.config(borderwidth=0)
textArea.config(background='black')
textArea.config(foreground="white")

textArea.pack()
mainWindow.resizable(width=False, height=False)
mainWindow.mainloop()