from tkinter import *
from tkinter import filedialog as fd
import hashlib

root = Tk()
root.geometry("250x190")


def apply_md5():
    print("MD5 function")
    file = fd.askopenfilename(
        title="Open The File", filetypes=(("Text Files", "*.txt"),)
    )
    RFile = open(file, "r")
    textD = RFile.read()
    hashed_data = hashlib.md5(textD.encode())
    hexd_data = hashed_data.hexdigest()
    WFile = open(file, "w")
    WFile.write(hexd_data)
    WFile.close()


def apply_sha256():
    print("SHA function")
    file = fd.askopenfilename(
        title="Open The File", filetypes=(("Text Files", "*.txt"),)
    )
    RFile = open(file, "r")
    textD = RFile.read()
    hashed_data = hashlib.sha256(textD.encode())
    hexd_data = hashed_data.hexdigest()
    WFile = open(file, "w")
    WFile.write(hexd_data)
    WFile.close()


btn = Button(root, text="Apply MD5", command=apply_md5)
btn.place(relx=0.3, rely=0.5, anchor=CENTER)
btn1 = Button(root, text="Apply SHA256", command=apply_sha256)
btn1.place(relx=0.7, rely=0.5, anchor=CENTER)
root.mainloop()
