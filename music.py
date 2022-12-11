import os
import time
from tkinter import *
from tkinter import filedialog
from pygame import mixer

root = Tk()
root.title("MymusicApp")
root.geometry("450x600+200+10")
root.configure(background='#000')
root.resizable(False,False)
image_icon=PhotoImage(file="logo png.png")
root.iconphoto(False,image_icon)
mixer.init()
stopGUI=""

# function for open file

def addmusic():
    path=filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs=os.listdir(path)
        for song in songs:
            if song.endswith('.mp3'):
                playlist.insert(END,song)

def playmusic():
    musicname=playlist.get(ACTIVE)
    print(musicname)
    print(musicname[0:-4])
    mixer.music.load(playlist.get(ACTIVE))
    mixer.music.play()
    update(0)


isvolume=True
def volume():
    volm=mixer.music.get_volume()
    print(volm)
    if isvolume :
        print(volm)
        isvolume=False
        mixer.music.set_volume(0)
    else:
        print("esle",volm)
        isvolume=True
        mixer.music.set_volume(100)


def stop():
    print(stopGUI)
    # root.after_cancel(stopGUI)
    mixer.music.pause()
    
# icon=
lower_frame=Frame(root,bg='#fff',width=450,height=100)
lower_frame.place(x=0,y=400)



framecount=30
frames=[PhotoImage(file='aa1.gif',format='gif -index %i' %(i)) for i in range(framecount)]
def update(ind):
    frame=frames[ind]
    ind +=1
    if ind == framecount:
        ind=0
    label.configure(image=frame)
    stopGUI=root.after(100,update,ind)
label= Label(root)
label.place(x=0,y=0)

#button
Buttonplay=PhotoImage(file='play1.png')
Button(root,image=Buttonplay,bg="#fff",bd=0,height=60,width=50,command=playmusic).place(x=215,y=420)

buttonstop=PhotoImage(file='stop1.png')
Button(root,image=buttonstop,bg='#fff',bd=0,height=60,width=60,command=stop).place(x=130,y=420)

buttonvolume=PhotoImage(file='volume.png')

Button(root,image=buttonvolume,bg="#fff",bd=0,height=60,width=60,command=volume).place(x=20,y=420)

buttonpause=PhotoImage(file='pause1.png')
Button(root,image=buttonpause,bg='#fff',bd=0,height=60,width=60,command=mixer.music.unpause).place(x=300,y=420)

# label
# menu=PhotoImage(file='menu.png')
# Label(root,image=menu).place(x=0,y=400,width=450,height=130)

# loaded music appear in this below frame
frame_music=Frame(root,bd=2,relief=RIDGE)
frame_music.place(x=0,y=500,width=450,height=100)

Button(root,text="BROWSE MUSIC",width=60,height=1,font="calibri 12 bold",fg="#fff",bg='#000',command=addmusic).place(x=0,y=500)

Scroll=Scrollbar(frame_music)
playlist=Listbox(frame_music,width=300,font=("Times new roman",12),bg="#333333",fg="grey",selectbackground='lightblue',cursor="hand2",bd=0,yscrollcommand=Scroll.set)
Scroll.config(command=playlist.yview)
Scroll.pack(side=RIGHT,fill=Y)
playlist.pack(side=RIGHT,fill=BOTH)


root.mainloop()
