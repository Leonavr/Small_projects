import tkinter as tk
import time
count = 30
def calc ():
    print(password.get())
    password.set('')
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
root.title ('Password')
root.geometry('400x400+200+300')

password = tk.StringVar()
curtime = ''
en1 = tk.Entry (textvariable = password)
en1.place(x = 130, y = 150)
btn1 = tk.Button (text ="Enter", command = calc, background = 'green')
btn1.place(x = 170, y = 175)
lb1 = tk.Label(text ='Введите пароль:')
lb1.place(x = 140, y = 125)

destroy()

root.mainloop()