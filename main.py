from tkinter import *
from speedtest import Speedtest


def SpeedCheck():
    internet = Speedtest()
    internet.get_servers()
    down = str(round(internet.download() / (10 ** 6),3)) + "Mbps"
    up = str(round(internet.upload() / (10 ** 6),3)) + "Mbps"
    label_down.config(text=down)
    label_up.config(text=up)


sp = Tk()
sp.title("Internet Speed")
sp.geometry("500x700")
sp.config(bg="blue")
label = Label(sp,text="Internet Speed Test",font=("Times New Roman",30))
label.place(x=55,y=40,height=50,width=380)

label = Label(sp,text="Downloading Speed",font=("Times New Roman",30))
label.place(x=55,y=130,height=50,width=380)

label_down = Label(sp,text="00",font=("Times New Roman",30))
label_down.place(x=55,y=200,height=50,width=380)

label = Label(sp,text="Upload Speed",font=("Times New Roman",30))
label.place(x=55,y=290,height=50,width=380)

label_up = Label(sp,text="00",font=("Times New Roman",30))
label_up.place(x=55,y=360,height=50,width=380)

button = Button(sp,text="Check Speed",font=("Times New Roman",30),relief=RAISED,bg="red",command=SpeedCheck)
button.place(x=60,y=460,height=50,width=380)

sp.mainloop()
