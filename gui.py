from tkinter import *
import pickle
from tkinter import messagebox
import randomGameTest.py

# this may be redundant when randomGameTest.py is actually imported
#classData =  pickle.load(open("reviewclassifier.p", "rb", -1))
#classData =  pickle.load(open("reviewClassifier.p", "rb", -1))

def Classify():
   game = entry1.get()
   if len(game) > 0:
      print(game)

   #print(entry1.get())

def Analyze():
   game = textBox.get("1.0",END)
   # HAVE TO UNCOMMENT AND TEST THIS BAD BOY WOOOOOOOOOOOOOO
   if len(game) > 0:
      print(classifyGame(game))
   #   print(makeChart(getEntities(fText)))
   messagebox.showinfo(title="Analysis Results", message="This was a positive review :)")
   messagebox.showinfo(title="Analysis Results", message="This was a negative review :(")




root = Tk()


hi = Label(root,text = "Video Game Review Datamining",padx=30,pady=10,justify=CENTER,font="Verdana 24 bold")
hi.grid(row=0,column=1)

# Classification and statistics on a video game title in the corpus of data
vg = Label(root, text="Video Game Title", padx=20,pady=10,justify=LEFT,font="16").grid(row=1)

entry1 = Entry(root, borderwidth=2,font="14")
entry1.grid(row=1,column=1)

classifyButton = Button(root,text='Classify',command=Classify,padx=70,pady=10,font="16")
classifyButton.grid(row=1,column=3,sticky=W)

# Border and frame spacing stuff
border = Frame(root, height=10)
border.grid(row=2)
border2 = Frame(root, height=10)
border2.grid(row=4)
col = Frame(root, width=20)
col.grid(column=2)
col2 = Frame(root, width=20)
col2.grid(column=4)

# User-provided review that we perform sentiment analysis on
reviewLb = Label(root, text="Analyze a Review", padx=20,pady=10,justify=LEFT,font=16)
reviewLb.grid(row=3)

textBox = Text(root, height=8,width=80,borderwidth=2,font="14",padx=5,pady=5)
textBox.grid(row=3,column=1)

analyzeButton = Button(root,text='Analyze',command=Analyze,padx=70,pady=10,font="16")
analyzeButton.grid(row=3,column=3,sticky=W)

# And run it! :D
root.mainloop()

