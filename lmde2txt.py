#!/bin/python3

import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askdirectory
from modules.lmde2txtMain import lmde2txt_func
from ttkthemes import ThemedTk

guiCheck = True

directory = ''
def directory_func():
    global directory
    directory = askdirectory(title='Select the full path for the input directory')

root = ThemedTk(theme='yaru')

root.geometry('300x150')
root.minsize(300, 150)
root.maxsize(300, 150)
root.title('lmde2txt.py')

main_frame = ttk.Frame(root)
main_frame.place(relx=0.5, rely=0.5,anchor='center')

main_label = ttk.Label(main_frame, text='Convert lmde to txt', font=('Arial', 20))
main_label.grid(row=0, column=0, columnspan=2, sticky='nsew', pady=(0, 10))

open_image = tk.PhotoImage(file='gui/folder-open.png')
open_btn = ttk.Button(main_frame, image=open_image, command=directory_func)
open_btn.grid(row=1, column=0, sticky='nsew', padx=(0, 10))

convert_btn = ttk.Button(main_frame, text='Convert', command=lambda: lmde2txt_func(guiCheck, directory))
convert_btn.grid(row=1, column=1, sticky='nsew')

root.mainloop()
