import sys
def calc():
    if sys.argv[3] =='+':
        res = int(sys.argv[1]) + int(sys.argv[2])
        return res
    elif sys.argv[3] =='-':
        res = int(sys.argv[1]) - int(sys.argv[2])
        return res

    elif sys.argv[3] =='*':
        res = int(sys.argv[1]) * int(sys.argv[2])
        return res

    elif sys.argv[3] =='/':
        res = int(sys.argv[1]) / int(sys.argv[2])
        return res

def write(res):
    if '-f' in sys.argv[1:]:
        with open(f"{sys.argv[2]}", "w") as f:
            f.write(res)
            print(res)


if '-h' in sys.argv[1:]:
    print ("Это калькулятор, введите название файла, 1-ю цифру, через пробел 2-ю цифру и операнд.\n'-v в конце' - для вывода хода операции\n'-f в конце и имя файла' - для сохранения результата")

elif '-v' in sys.argv[1:]:
    print (f"{sys.argv[1]} {sys.argv[3]} {sys.argv[2]} = {calc()}")
elif '-f' in sys.argv[1:]:
        with open(f"{sys.argv[5]}", "w") as f:
            f.write(f"{sys.argv[1]} {sys.argv[3]} {sys.argv[2]} = {calc()}")
else: 
    print(calc())