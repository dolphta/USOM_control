from tkinter import *
import datetime

def control():
    file = open("usom.txt", "r")
    content = file.read()
    file.close()
    ip = entry1.get()
    today = datetime.datetime.now()
    if str(ip) in content:
        file = open("log.txt", "a")
        text = str(ip) + " is malicious.\nDate:" + str(today) + "\n"
        file.write(text)
        file.close()
        v.set("IP is malicious.")
    else:
        file = open("log.txt", "a")
        text = str(ip) + " is not malicious\nDate:" + str(today) + "\n"
        file.write(text)
        file.close()
        v.set("IP is not malicious")

top = Tk()

top.title("USOM IP CONTROL")

B = Button(top, text="Control", command=control)
B.place(x=50, y= 50)
B.pack()

label1 = Label(top, text="Enter the IP adress that will be controled:")
label1.place(x=50, y=100)
label1.pack

entry1 = Entry(top)
entry1.place(x=50, y=150)
entry1.pack

v = StringVar()
entry2 = Entry(top, textvariable=v)
entry2.place(x=50, y=200)
entry2.pack

top.mainloop()