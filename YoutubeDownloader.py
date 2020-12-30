import time
from tkinter import *
# from tkinter import PhotoImage
from pytube import YouTube
# from PIL import Image, ImageTk as Ptk


global arg
def funkcija():
    arg=v.get()
    print("arg is",arg)
    return arg

def create_window():
    window = Toplevel()
    window.title("Downloaded!")
    l1 = Label(window,text = "Your Video has been downloaded!")
    l1.pack()
    # tk.Label("Download!")


# Youtube Download Function
def downloadVid(x):
    funkcija()
    print("Value of x is:",x)
    global E1
    string = E1.get()
    yt = YouTube(str(string))
    videos = yt.streams.all()
    x=2
    s = 1
    for v in videos:
        print(str(s) + ". " + str(v))
        s += 1

    n = x
    vid = videos[n]
    destination = "E:/"
    vid.download(destination)
    print(r"The video has been downloaded at G:/")

# GUI Design

root = Tk(screenName=None,  baseName=None,  className= ' Param\'s Youtube Downloader',  useTk=1)
root.resizable(height = 0, width = 0)
root.geometry("300x300")
w0 = Canvas(width=500, height=60)
# arg=0
# Top Image
# photo = PhotoImage(file=r"G:\Misc\New folder\YTD.gif")
# w0.create_image(0,0, anchor="nw",image=photo)
w0.pack()


# Labels
w = Label(root,text = "Paste your link here")
w.pack()
# a = Label(root,text = "",justify='left')
# a.pack()
E1 = Entry(root,bd=2)
E1.pack(side=TOP)
a = Label(root,text = "",justify='left')
a.pack()

# Buttons


w = Label(root,text = "Choose Quality:",justify='left')
w.pack()
v = IntVar()
# Radiobutton(root, text='360p', variable=v, value=2, padx=100,command=funkcija).pack(anchor='w')
# Radiobutton(root, text='480p', variable=v, value=7,padx=100,command=funkcija).pack(anchor='w')
Radiobutton(root, text='720p', variable=v, value=0,padx=100,command=funkcija).pack(anchor='w')
qual=funkcija()

# print(qual)
# try:
#   print(qual)
# except NameError:
#   print("Variable x is not defined")
# except:https://www.youtube.com/watch?v=oSCX78-8-q0&t=1s
#     qual = funkcija()
# if qual==1:
#     arg = 3
# elif qual==2:
#     arg = 8
# elif qual ==3:
#     arg=1

a = Label(root,text = "",justify='left')
b = Label(root,text = "",justify='left')
a.pack()
b.pack()
button=Button(root,text="Download",fg="red",command=lambda:[create_window(),downloadVid(qual)])

button.pack()

# End
# w = Label(root,compound = CENTER,text = "Log In to download in 1080p",pady=10)
# w.pack()
# button2=Button(root,text="Log in",fg="red",command=downloadVid)
# button2.pack()
# a = Label(root,text = "",justify='left')
# a.pack()




root.mainloop()
