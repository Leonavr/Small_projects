import tkinter as tk
import json
import collections
import os
import time

count = 60
def calc ():
    with open(f"{path.get()}", "r", encoding = 'utf-8') as read_file:
        data = json.load(read_file)
    corpus = data['Corpus']
    a = [x.split('|')[1] for x in corpus]
    without_dupl = [item for item, count in collections.Counter(a).items() if count > 1]
    for j in without_dupl:
        with open("duplicates.txt", "a") as f:
            f.write(f'|{j}"\n')
    path.set('')

def destroy():
    global curtime
    global count
    newtime = time.strftime('%H:%M:%S')
    if newtime != curtime:
        count -= 1
        if count < 0:
            root.destroy()
    root.after(1000,destroy)

root = tk.Tk()
root.title ('Find duplicates')
root.geometry('400x150+200+300')
root.resizable(False, False)
path = tk.StringVar()
curtime = ''
en1 = tk.Entry (textvariable = path, width = 55)
en1.place(x = 30, y = 50)
btn1 = tk.Button (text ="Enter", command = calc, background = 'green')
btn1.place(x = 180, y = 75)
lb1 = tk.Label(text ='Введіть шлях до файлу:')
lb1.place(x = 130, y = 25)


destroy()

root.mainloop()