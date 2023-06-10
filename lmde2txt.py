#!/bin/python3

import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askdirectory
from modules.lmde2txtMain import lmde2txt_func
import sv_ttk

guiCheck = True

directory = ''
def directory_func():
    global directory
    directory = askdirectory(title='Select the full path for the input directory')

root = tk.Tk()

root.geometry('355x155')
root.minsize(355, 155)
root.maxsize(355, 155)
root.title('lmde2txt.py')

def toggle_theme():
    if sv_ttk.get_theme() == 'dark':
        sv_ttk.use_light_theme()
    elif sv_ttk.get_theme() == 'light':
        sv_ttk.use_dark_theme()

main_frame = ttk.Frame(root)
main_frame.place(relx=0.5, rely=0.5,anchor='center')

theme_image = tk.PhotoImage(file='gui/night-light-symbolic.symbolic.png')
changeTheme_btn = ttk.Button(main_frame, image=theme_image, command=toggle_theme)
changeTheme_btn.grid(row=0, column=0, sticky='nsew', padx=(0, 10), pady=(0, 10))

main_label = ttk.Label(main_frame, text='Convert lmde to txt', font=('Arial', 20))
main_label.grid(row=0, column=1, sticky='nsew', pady=(0, 10))

open_image = tk.PhotoImage(file='gui/folder-open.png')
open_btn = ttk.Button(main_frame, image=open_image, command=directory_func)
open_btn.grid(row=1, column=0, sticky='nsew', padx=(0, 10))

convert_btn = ttk.Button(main_frame, text='Convert', command=lambda: lmde2txt_func(guiCheck, directory))
convert_btn.grid(row=1, column=1, sticky='nsew')

sv_ttk.set_theme('light')

root.mainloop()
