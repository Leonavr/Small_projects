import sys
import random
from PySide2 import QtCore, QtWidgets, QtGui
from random import randrange


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.win = self.game = self.lose = 0

        self.button = QtWidgets.QPushButton("Камень")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("rock.png"))
        self.button.setIcon(icon)
        self.button1 = QtWidgets.QPushButton("Ножницы")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("sciss.png"))
        self.button1.setIcon(icon)
        self.button2 = QtWidgets.QPushButton("Бумага")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("paper.png"))
        self.button2.setIcon(icon)
        self.button3 = QtWidgets.QPushButton("Ящерица")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("lizz.png"))
        self.button3.setIcon(icon)
        self.button4 = QtWidgets.QPushButton("Спок")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("spock.jpg"))
        self.button4.setIcon(icon)

        self.text = QtWidgets.QLabel("Let's go!",
                                    alignment=QtCore.Qt.AlignCenter)
        self.text1 = QtWidgets.QLabel(f"Партий: {self.game}",
                                    alignment = QtCore.Qt.AlignCenter)
        self.text2 = QtWidgets.QLabel(f"Побед: {self.game}",
                                    alignment=QtCore.Qt.AlignCenter)
        self.text3 = QtWidgets.QLabel(f"Проиграно: {self.game}",
                                    alignment=QtCore.Qt.AlignCenter)


        self.layout = QtWidgets.QVBoxLayout()
        self.hbox = QtWidgets.QHBoxLayout()
        self.layout.addWidget(self.text)
        self.hbox.addWidget(self.text1)
        self.hbox.addWidget(self.text2)
        self.hbox.addWidget(self.text3)
        self.layout.addLayout(self.hbox)

        self.hbox1 = QtWidgets.QHBoxLayout()
        self.hbox1.addWidget(self.button)
        self.hbox1.addWidget(self.button1)
        self.hbox1.addWidget(self.button2)
        self.hbox1.addWidget(self.button3)
        self.hbox1.addWidget(self.button4)
        self.layout.addLayout(self.hbox1)
        self.setLayout(self.layout)


        self.button.clicked.connect(lambda x: self.magic(0))
        self.button1.clicked.connect(lambda x: self.magic(1))
        self.button2.clicked.connect(lambda x: self.magic(2))
        self.button3.clicked.connect(lambda x: self.magic(3))
        self.button4.clicked.connect(lambda x: self.magic(4))
    
    @QtCore.Slot()
    def magic(self, choise):
        list_1 = ['камень','ножницы', "бумагу","ящерицу", "Спока"]
        comp_choise = randrange(len(list_1))
        self.text.setText(f"Я выбрал {list_1[comp_choise]}")
        if ((choise == 0 and comp_choise == 1) or (choise == 1 and comp_choise == 2) or (choise == 2 and comp_choise == 0) 
            or (choise == 0 and comp_choise == 3) or (choise == 1 and comp_choise == 2) or (choise == 1 and comp_choise == 3) 
            or (choise == 2 and comp_choise == 0) or (choise == 2 and comp_choise == 4) or (choise == 3 and comp_choise == 4)
            or (choise == 3 and comp_choise == 2) or (choise == 4 and comp_choise == 1) or (choise == 3 and comp_choise == 0)):
            self.win += 1
            self.game +=1
            self.text.setText(f"Я выбрал {list_1[comp_choise]}")
        elif choise == comp_choise:
            self.game +=1
            self.text.setText(f"Ничья")
        else:
            self.lose += 1
            self.game +=1
            self.text.setText(f"Я выбрал {list_1[comp_choise]}")
        self.text1.setText(f"Партий: {self.game}")
        self.text2.setText(f"Побед: {self.win}")
        self.text3.setText(f"Проиграно: {self.lose}") 

        f = open('config.ini', 'w')
        f.write(f"Партий = {self.game}" '\n')
        f.write(f"Побед = {self.win}" '\n')
        f.write(f"Проиграно = {self.lose}" '\n')
        f.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(400, 100)
    widget.setWindowTitle('The Big Bang Theory')
    widget.show()

    sys.exit(app.exec_())
