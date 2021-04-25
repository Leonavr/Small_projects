from tkinter import *
from random import randrange
from PIL import Image, ImageTk

class Main(Frame):
    def __init__(self, root):
        super(Main, self).__init__(root)
        self.startUI()

    def startUI(self):
        pict_1 = Image.open("spock.jpg")
        self.image = ImageTk.PhotoImage(pict_1)
        pict_2 = Image.open("rock.png")
        self.image1 = ImageTk.PhotoImage(pict_2)
        pict_3 = Image.open("sciss.png")
        self.image2 = ImageTk.PhotoImage(pict_3)
        pict_4 = Image.open("paper.png")
        self.image4 = ImageTk.PhotoImage(pict_4)
        pict_5 = Image.open("lizz.png")
        self.image5 = ImageTk.PhotoImage(pict_5)

        btn = Button(root, text="Камень", image = self.image1,
                     command=lambda x=0: self.btn_click(x))
        btn2 = Button(root, text="Ножницы",image = self.image2,
                      command=lambda x=1: self.btn_click(x))
        btn3 = Button(root, text="Бумага",image = self.image4,
                      command=lambda x=2: self.btn_click(x))
        btn4 = Button(root, text="Ящерица", image = self.image5,
                      command=lambda x=3: self.btn_click(x))
        btn5 = Button(root, text="Спок",image = self.image,
                      command=lambda x=4: self.btn_click(x))

        btn.place(x = 50, y = 70)
        btn2.place(x = 108, y = 70)
        btn3.place(x = 166, y = 70)
        btn4.place(x = 218, y = 70)
        btn5.place(x = 270, y = 70)
        
        self.lbl = Label(root, text="    Начнем!")
        self.lbl.place(x = 150, y = 0)

        self.win = self.game = self.lose = 0

        self.lbl2 = Label(root, justify="left",
                         text=f"Партий: {self.game}")
        self.lbl3 = Label(root, justify="left",
                         text=f"Побед: {self.game}")
        self.lbl4 = Label(root, justify="left",
                         text=f"Проиграно: {self.game}")              


        

        self.lbl2.place(x = 60, y = 30)
        self.lbl3.place(x = 160, y = 30)
        self.lbl4.place(x = 260, y = 30)

    
    def btn_click(self, choise):
        list_1 = ['камень','ножницы', "бумагу","ящерицу", "Спока"]
        comp_choise = randrange(len(list_1))

        if (choise == 0 and comp_choise == 1) or (choise == 1 and comp_choise == 2) or (choise == 2 and comp_choise == 0) \
             or (choise == 0 and comp_choise == 3) or (choise == 1 and comp_choise == 2) or (choise == 1 and comp_choise == 3) \
                  or (choise == 2 and comp_choise == 0) or (choise == 2 and comp_choise == 4) or (choise == 3 and comp_choise == 4) \
                      or (choise == 3 and comp_choise == 2) or (choise == 4 and comp_choise == 1) or (choise == 3 and comp_choise == 0):
            self.win += 1
            self.game +=1
            self.lbl.configure(text=f"Я выбрал {list_1[comp_choise]}")
        elif choise == comp_choise:
            self.game +=1
            self.lbl.configure(text=f"Ничья")
        else:
            self.lose += 1
            self.game +=1
            self.lbl.configure(text=f"Я выбрал {list_1[comp_choise]}")
        self.lbl2.configure(text=f"Партий: {self.game}")
        self.lbl3.configure(text=f"Побед: {self.win}")
        self.lbl4.configure(text=f"Проиграно: {self.lose}") 

        f = open('config.ini', 'w')
        f.write(f"Партий = {self.game}" '\n')
        f.write(f"Побед = {self.win}" '\n')
        f.write(f"Проиграно = {self.lose}" '\n')
        f.close()

        del comp_choise


if __name__ == '__main__':
    root = Tk()
    root.geometry("400x150+200+200")
    root.title("Камень, ножницы, бумага")
    root.resizable(False, False)
    app = Main(root)
    app.pack()
    root.mainloop()