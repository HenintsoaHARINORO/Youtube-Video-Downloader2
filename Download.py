import tkinter as tk
from pytube import YouTube

window = tk.Tk()
window.geometry('500x300')
window.resizable(0,0)
window.title("Youtube Video Downloader")
tk.Label(window, text ="Youtube Video Downloader", font ="arial 20 bold").pack()

link = tk.StringVar()

tk.Label(window, text ="Paste Link Here:", font ="arial 15 bold").place(x=160, y=60)
link_error = tk.Entry(window, width =70, textvariable = link).place(x =32, y=90)

def Downloader():
    url =YouTube(str(link.get()))
    video =url.streams.first()
    video.download('./Downloads')
    tk.Label(window, text ="Successfully Downloaded", font ="arial 15").place(x =180, y =200)

#Download Button
tk.Button(window, text ="DOWNLOAD", font ="Verdana 15 bold", bg ="orange", padx =2, command =Downloader).place(x=180, y=150)

window.mainloop()
