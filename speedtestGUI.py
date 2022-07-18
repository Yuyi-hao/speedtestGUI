from tkinter import *
from numpy import imag
from plumbum import BG
import speedtest

BG_COLOR = "#1a212d"

def get_data():
    testResult = speedtest.Speedtest()
    upload_speed = round(testResult.upload()/(1024*1024),2)
    download_speed = round(testResult.download()/(1024*1024),2)

    servernames = []
    testResult.get_servers(servernames)
    ping = round(testResult.results.ping,1)

    return (upload_speed,download_speed,ping)

class InternetSpeed:
    def __init__(self) -> None:
        window = Tk()
        window.title("Internet Speed Test")
        window.geometry("380x600")
        window.resizable(False,False)
        window.config(background=BG_COLOR)

        # images instances  
        icon = PhotoImage(file="logo.png")
        button_image = PhotoImage(file="button.png")
        main_image = PhotoImage(file="main.png")
        top_image = PhotoImage(file="top.png")

        # set icon
        window.iconphoto(False,icon)

        # setting up images 
        self.top_label = Label(window, image=top_image, bg=BG_COLOR)
        self.top_label.pack(pady=(10,5))
        self.main_label = Label(window, image=main_image, bg=BG_COLOR)
        self.main_label.pack(pady=(20,0))
        self.start_button = Button(window, image=button_image, bg=BG_COLOR, bd=0,activebackground=BG_COLOR,cursor="hand2", command=self.update_data)
        self.start_button.pack(pady=10)

        # Showing label 
        # top labels 
        Label(window,text = "PING",font="arial 10 bold", bg = "#384056",fg="white").place(x=61,y=10)
        Label(window,text = "DOWNLOAD",font="arial 10 bold", bg = "#384056",fg="white").place(x=151,y=10)
        Label(window,text = "UPLOAD",font="arial 10 bold", bg = "#384056",fg="white").place(x=274,y=10)
        
        # show units
        Label(window, text="MS", font="arial 7 bold",bg ="#384056",fg="white").place(x=68,y=80,)
        Label(window, text="MBPS", font="arial 7 bold",bg ="#384056",fg="white").place(x=173,y=80,)
        Label(window, text="MBPS", font="arial 7 bold",bg ="#384056",fg="white").place(x=283,y=80,)
        Label(window, text="Download", fg="white", font="arial 18 bold", bg = "#384056").place(x=135, y=260)
        Label(window, text="MBPS", fg="white", font="arial 18 bold", bg = "#384056").place(x=154, y=368)

        # show values 
        self.ping_label = Label(window, text="00", font="arial 15 bold",bg ="#384056",fg="white")
        self.ping_label.place(x=80,y=70, anchor="center")

        self.upload_label = Label(window, text="00", font="arial 15 bold",bg ="#384056",fg="white")
        self.upload_label.place(x=190,y=70, anchor="center")

        self.download_label = Label(window, text="00", fg="white", font="arial 15 bold", bg = "#384056")
        self.download_label.place(x=300, y=70, anchor="center")

        self.bdownload_label = Label(window, text="00.00", fg="white", font="arial 40 bold", bg = "#384056")
        self.bdownload_label.place(x=193, y=327, anchor="center")

        window.mainloop()

    def update_data(self):
        data = get_data()
        self.ping_label["text"]=str(data[2])
        self.download_label["text"] = str(data[1])
        self.upload_label["text"] = str(data[0])
        self.bdownload_label["text"] = str(data[1])


InternetSpeed()