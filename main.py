import tkinter as tk
from tkinter import messagebox,Tk,PhotoImage,Canvas,Button,Entry
from Transmition import chirp,spectrum,rf,fmrds,nfm,ssb,am,freedv,sstv,pocsag,opera,rtty
from interval import setTimeOut
from PIL import ImageTk
from PIL import Image as Imagee
import subprocess

rpix = Tk()
rpix.title("RPIX")
rpix.geometry("600x500")
bgi = PhotoImage(file = "images/1.png")
imageFolder="images/"     

#canvas creation

mycanvas= Canvas(rpix,width=600,height=500,bg="grey")
mycanvas.place(x=0,y=0)
startButton=Button(rpix,text="enter")
startButton.place(x=300,y=100)
entry = Entry(rpix)
entry.place(x=170,y=100)


def select(name,command):
    startButton.configure(text=name,command=lambda :setTimeOut(lambda :command(rpix,entry.get()),10))

def createButton(root,image,name,command,x,y):
    Button(root,image=image,bg="gray",command=lambda :select(name,command)).place(x=x-430,y=y-200)


def Image(name):
    return ImageTk.PhotoImage(Imagee.open(imageFolder+name+".png"))


#  CHIRP BUTTON
img1=Image("button1")
createButton(rpix,img1,"Chirp",chirp,450,430)
# SPECTRUM BUTTON
img2=Image("button2")
createButton(rpix,img2,"Spectrum",spectrum,450,495)
# RF MYFACE BUTTON
img3=Image("button3")
createButton(rpix,img3,"Rf",rf,450,560)
# FmRds BUTTON
img4=Image("button4")
createButton(rpix,img4,"Fmrds",fmrds,450,625)
# NFM
img5=Image("button5")
createButton(rpix,img5,"Nfm",nfm,650,430)
# SSB
img6=Image("button6")
createButton(rpix,img6,"Ssb",ssb,650,495)
# AM
img7=Image("button7")
createButton(rpix,img7,"Am",am,650,560)
# FREEDV
img8=Image("button8")
createButton(rpix,img8,"Freedv",freedv,650,625)
# SSTV
img9=Image("button9")
createButton(rpix,img9,"Sstv",sstv,850,430)
# POCSAG
img10=Image("button10")
createButton(rpix,img10,"Pocsag",pocsag,850,495)
# Opera
img11=Image("button11")
createButton(rpix,img11,"Opera",opera,850,560)
# RTTY
img12=Image("button12")
createButton(rpix,img12,"Rtty",rtty,850,625)

rpix.mainloop()

