import tkinter as tk


root = tk.Tk()
root.title('1')
root.geometry('800x600+500-50')



lb_text = tk.StringVar()
fr = tk.Frame(background ='red', borderwidth =15, relief = 'ridge', 
width = 200, height = 200)
fr.place(x = 0, y = 0)
fr_small = tk.Frame(fr, background ='blue', borderwidth =15, relief = 'ridge', 
width = 50, height = 50)
fr_small.place(x = 0, y = 0)
fr_small_1 = tk.Frame(fr, background ='blue', borderwidth =15, relief = 'ridge', 
width = 50, height = 50)
fr_small_1.place(x = 120, y = 0)
fr_small_2 = tk.Frame(fr, background ='blue', borderwidth =15, relief = 'ridge', 
width = 50, height = 50)
fr_small_2.place(x = 60, y = 120)

fr1 = tk.Frame(background ='red', borderwidth =15, relief = 'ridge', 
width = 200, height = 200)
fr1.place(x = 600, y = 0)
fr_small = tk.Frame(fr1, background ='blue', borderwidth =15, relief = 'ridge', 
width = 50, height = 50)
fr_small.place(x = 0, y = 0)
fr_small_1 = tk.Frame(fr1, background ='blue', borderwidth =15, relief = 'ridge', 
width = 50, height = 50)
fr_small_1.place(x = 120, y = 0)
fr_small_2 = tk.Frame(fr1, background ='blue', borderwidth =15, relief = 'ridge', 
width = 50, height = 50)
fr_small_2.place(x = 60, y = 120)

fr2 = tk.Frame(background ='red', borderwidth =15, relief = 'ridge', 
width = 200, height = 200)
fr2.place(x = 300, y = 400)
fr_small_2 = tk.Frame(fr, background ='blue', borderwidth =15, relief = 'ridge', 
width = 50, height = 50)
fr_small_2.place(x = 0, y = 0)
fr_small = tk.Frame(fr2, background ='blue', borderwidth =15, relief = 'ridge', 
width = 50, height = 50)
fr_small.place(x = 0, y = 0)
fr_small_1 = tk.Frame(fr2, background ='blue', borderwidth =15, relief = 'ridge', 
width = 50, height = 50)
fr_small_1.place(x = 120, y = 0)
fr_small_2 = tk.Frame(fr2, background ='blue', borderwidth =15, relief = 'ridge', 
width = 50, height = 50)
fr_small_2.place(x = 60, y = 120)


root.mainloop()