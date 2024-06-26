from PIL import Image, ImageTk
import cv2
import google.generativeai as genai
import tkinter as tk
import imutils

def get_cam():
    global cap
    if cap is not None:
      ret,frame=cap.read()
      if ret:
          frame=imutils.resize(frame, width=400)
          frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
          im= Image.fromarray(frame)
          img=ImageTk.PhotoImage(image=im)
          lblVideo.configure(image=img)
          lblVideo.image=img
          lblVideo.after(5,get_cam)
      else:
          lblVideo.image=""
          cap.release()

cap=None
def ini():
    global cap
    cap=cv2.VideoCapture(0, cv2.CAP_DSHOW)
    get_cam()

ven=tk.Tk()
ven.geometry("800x400")
icon=ImageTk.PhotoImage(file="eye-icon.png")
ven.iconphoto(False,icon)
ven.title("IM_YOUR_EYES")
ven.configure(bg="#00FFB9")
buto1=tk.Button(ven, text="Iniciar camara", command=ini, width=20)
buto1["border"]=3
buto1.grid(row=0,column=0,padx=5,pady=5)

buto2=tk.Button(ven, text="wa", command=ini, width=20)
buto2["border"]=3
buto2.grid(row=1,column=0,padx=5,pady=5)

buto3=tk.Button(ven, text="we", command=ini, width=20)
buto3["border"]=3
buto3.grid(row=2,column=0,padx=5,pady=5)

lblVideo=tk.Label(ven)
lblVideo.grid(row=1,column=1,padx=50,pady=5)

ven.mainloop()