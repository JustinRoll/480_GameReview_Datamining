from tkinter import *
import pickle
from tkinter import messagebox
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from reviewUtil import *
from clusterUtil import *

def Cluster():
   game = textBox.get("1.0",END)
   if len(game) > 1:
      clusterResult = list(clusterTestGame(game))
      resultStr = ""
      if "Test Game Title" in clusterResult:
        clusterResult.remove("Test Game Title")
      for item in clusterResult:
        resultStr += item[:-4] + ", "
      
      messagebox.showinfo(title="Cluster Results", message=resultStr[:-2])

def ClusterFile():
    game = textBox2.get("1.0",END)
    if len(game) > 1:
      clusterResult = list(clusterTestGame(game))
      resultStr = ""
      if "Test Game Title" in clusterResult:
        clusterResult.remove("Test Game Title")
      for item in clusterResult:
        resultStr += item[:-4] + ", "
      
      messagebox.showinfo(title="Cluster Results", message=resultStr[:-2])

def Analyze():
   game = textBox.get("1.0",END)
   if len(game) > 1:
      rating = classifyGame(game)
      if rating == 1:
         messagebox.showinfo(title="Analysis Results", message="This was a positive review :)")
      elif rating == 0:
         messagebox.showinfo(title="Analysis Results", message="This was a negative review :(")

def AnalyzeEntities():
    game = textBox2.get("1.0",END)
    if len(game) > 1:
        makeChart(getEntities(game))

def AnalyzeEntitiesRaw():
   game = textBox.get("1.0",END)
   if len(game) > 1:
      makeChart(getEntities(game))

def AnalyzeFile():
   name = filedialog.askopenfilename(title = "Select a video game review", initialdir="/Users/jroll/dev/480/480_GameReview_Datamining/sampleReviews",filetypes=(("text files","*.txt"),("all files","*.*")))
   rating = classifyGameReviewFile(name)

   textBox2.delete("1.0",END)
   f = open(name, 'r')
   fText = ''.join(f.readlines())
   f.close()
   textBox2.insert(INSERT,fText)

   if rating == 1:
      messagebox.showinfo(title="Analysis Results", message="This was a positive review :)")
   elif rating == 0:
      messagebox.showinfo(title="Analysis Results", message="This was a negative review :(")


root = Tk()

hi = Label(root,text = "Video Game Review Datamining",padx=30,pady=10,justify=CENTER,font="Verdana 24 bold")
hi.grid(row=0,column=1)

# Border and frame spacing stuff
border = Frame(root, height=10)
border.grid(row=1)
border2 = Frame(root, height=10)
border2.grid(row=6)
border3 = Frame(root, height=10)
border3.grid(row=11)
col = Frame(root, width=20)
col.grid(column=2)
col2 = Frame(root, width=20)
col2.grid(column=4)

# User-provided review that we perform sentiment analysis on
reviewLb = Label(root, text="Analyze a Review", padx=20,pady=10,justify=LEFT,font=16)
reviewLb.grid(row=3,rowspan=3)

textBox = Text(root, wrap=WORD,height=20,width=120,borderwidth=2,font="14",padx=5,pady=5,highlightbackground="GRAY",highlightthickness="0.5")
textBox.grid(row=3,column=1,rowspan=3)

analyzeButton = Button(root,text='Analyze Review',command=Analyze,width=20,pady=10,font="16")
analyzeButton.grid(row=3,column=3,sticky=W)

analyzeButton4 = Button(root,text='Analyze Entities',command=AnalyzeEntitiesRaw,width=20,pady=10,font="16")
analyzeButton4.grid(row=4,column=3,sticky=W)

classifyButton = Button(root,text='Cluster',command=Cluster,width=20,pady=10,font="16")
classifyButton.grid(row=5,column=3,sticky=W)


# File provided review that we perform sentiment analysis on
reviewLb = Label(root, text="Analyze a Review from a file", padx=20,pady=10,justify=LEFT,font=16)
reviewLb.grid(row=8,rowspan=3)

textBox2= Text(root, wrap=WORD,height=20,width=120,borderwidth=1,font="14",padx=5,pady=5,highlightbackground="GRAY",highlightthickness="0.5")
textBox2.grid(row=8,column=1,rowspan=3)

analyzeButton2 = Button(root,text='Analyze Review File',command=AnalyzeFile,width=20,pady=10,font="16")
analyzeButton2.grid(row=8,column=3,sticky=W)

analyzeButton3 = Button(root,text='Analyze Entities',command=AnalyzeEntities,width=20,pady=10,font="16")
analyzeButton3.grid(row=9,column=3,sticky=W)

classifyButton2 = Button(root,text='Cluster',command=ClusterFile,width=20,pady=10,font="16")
classifyButton2.grid(row=10,column=3,sticky=W)

# And run it! :D
root.mainloop()

