import tkinter as tk
import random

root = tk.Tk()
root.title('1')
root.geometry('900x700+500-50')

def bandit():
    text['text'] = random.randint(1,10)
    text1['text'] = random.randint(1,10)
    text2['text'] = random.randint(1,10)

lb_text = tk.StringVar()
fr = tk.Frame(background ='red', borderwidth =15, relief = 'ridge', 
width = 200, height = 500)
fr.pack(expand = True, side = 'right')
fr1 = tk.Frame(background ='red', borderwidth =15, relief = 'ridge', 
width = 200, height = 500)
fr1.pack(expand = True, side = 'right')

fr2 = tk.Frame(background ='red', borderwidth =15, relief = 'ridge', 
width = 200, height = 500)
fr2.pack(expand = True, side = 'right')

text = tk.Label(fr, text = 'Test', bg ='gray', width = 20, height = 20,font = 'Arial 50')
text.place(relwidth = 1, relheight = 1)
text1 = tk.Label(fr1, text ='Test', bg ='gray', width = 25, height = 30,font = 'Arial 50')
text1.place(relwidth = 1, relheight = 1)
text2 = tk.Label(fr2, text ='Test', bg ='gray', width = 25, height = 30,font = 'Arial 50')
text2.place(relwidth = 1, relheight = 1)

btn1 = tk.Button (text ="Lever arm", command = bandit )
btn1.pack(expand = True, side = 'right', fill = 'both')

root.mainloop()