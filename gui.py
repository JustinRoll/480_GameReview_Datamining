from tkinter import *

def Classify():
   print(entry1.get())

def Analyze():
   print(textBox.get("1.0",END))

root = Tk()

hi = Label(root,text = "Video Game Review Datamining",padx=30,pady=10,justify=CENTER,font="Verdana 24 bold")
hi.grid(row=0,column=1)

# Classification and statistics on a video game title in the corpus of data
vg = Label(root, text="Video Game Title", padx=10,pady=10,justify=LEFT,font="16").grid(row=1)

entry1 = Entry(root, font="14")
entry1.grid(row=1,column=1)

classifyButton = Button(root,text='Classify',command=Classify,padx=10,pady=10,font="16")
classifyButton.grid(row=1,column=2,sticky=W)

# User-provided review that we perform sentiment analysis on
reviewLb = Label(root, text="Analyze a Review", padx=10,pady=10,justify=LEFT,font=16)
reviewLb.grid(row=2)

textBox = Text(root, height=8,width=80,font="14",padx=5,pady=5)
textBox.grid(row=2,column=1)

analyzeButton = Button(root,text='Analyze',command=Analyze,padx=10,pady=10,font="16")
analyzeButton.grid(row=2,column=2,sticky=W)

# And run it! :D
root.mainloop()

