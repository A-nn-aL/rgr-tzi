import os
from tkinter import *

def add_message_to_file(infile, string):
    f = open(infile.txt, 'w+')
    # CHECK IF THERE IS SOMETHING IN THE FILE

    f.write(string)

    f.close()


def read_file(infile, mode):
    f = open(infile, mode)
    text = f.read()
    f.close()
    return text


# def myClick(file, mode, row1, column1):
def show_text():
    file = 'infile.txt'
    mode = 'r+'
    row1 = 4
    column1 = 0
    text = read_file(file, mode)
    myLable1 = Label(root, text=text)
    myLable1.grid(row=row1, column=column1)


def show_encrypted_text():
    file = 'output.txt'
    mode = 'rb'
    row1 = 6
    column1 = 0
    text = read_file(file, mode)
    myLable1 = Label(root, text=text)
    myLable1.grid(row=row1, column=column1)



root = Tk()

myLable = Label(root, text="Демонстрація роботи блочного шифру PC5").grid(row=0, column=0)

inn = Entry(root)


def write_file():
    infile = 'infile.txt'
    message = inn.get()
    f = open(infile, 'w+')
    f.truncate()
    f.write(message)
    encrypt = r'python main.py encrypt infile.txt output.txt'
    stream = os.popen(encrypt)
    decrypt = r'python main.py decrypt output.txt output.txt.key decripted.txt'
    stream1 = os.popen(decrypt)
    f.close()


inn.grid(row=1, column=0)

myButton0 = Button(root, text="Підтвердити", command=write_file).grid(row=2, column=0)
# myButton = Button(root, text="Показати текст", command=myClick('infile.txt', 'r+', 4,0))

myButton = Button(root, text="Показати текст", command=show_text).grid(row=3, column=0)

myButton1 = Button(root, text="Показати шифр", command=show_encrypted_text).grid(row=5, column=0)


def show_decrypted_text():

    file = 'decripted.txt'
    mode = 'rb'
    row1 = 8
    column1 = 0
    text = read_file(file, mode)
    myLable1 = Label(root, text=text)
    myLable1.grid(row=row1, column=column1)

myButton2 = Button(root, text="Показати розшифровку тексту", command=show_decrypted_text).grid(row=7, column=0)
root.mainloop()
