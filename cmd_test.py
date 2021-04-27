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
with open("log.txt", "w") as f:
    f.write(f"{sys.argv[1]} {sys.argv[3]} {sys.argv[2]} = {calc()}")

if '-h' in sys.argv[1:]:
    print ("Это калькулятор, введите название файла, 1-ю цифру, через пробел 2-ю цифру и операнд.\n'-v в конце' - для вывода хода операции")

elif '-v' in sys.argv[1:]:
    print (f"{sys.argv[1]} {sys.argv[3]} {sys.argv[2]} = {calc()}")

else: 
    print(calc())