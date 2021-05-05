import argparse
import sys
parser = argparse.ArgumentParser()
nums = parser.add_argument('nums', type=int, nargs='+',
                    help='Список всех введенных цифр')
oper = parser.add_argument("oper")

parser.add_argument("--verbose", "-v", 
                    action = 'store_true',
                    help="подробность вывода")
parser.add_argument("--file", "-f", type=argparse.FileType('w', encoding='utf-8'), 
                    help="Запись в файл и вывод на экран")
parser.add_argument("--quite", "-q", nargs = '?', const=True, action="store",
                    help="Запись в файл без вывода")
parser.add_argument("--append", "-a", type=argparse.FileType('a', encoding='utf-8'),
                    help="Дополнение в файл без вывода")
args = parser.parse_args()

def calc():
    if args.oper == '+':
        summa = 0
        for i in range(len(args.nums)):
            summa += args.nums[i]
        return summa
    
    elif args.oper == '-':
        diff = args.nums[0]
        for i in range(len(args.nums)):
            if i == 0:
              continue
            else:
                diff -= args.nums[i]
        return diff
    
    elif args.oper == '*':
        multiple = args.nums[0]
        for i in range(len(args.nums)):
            if i == 0:
                continue
            else:
                multiple *= args.nums[i]
        return multiple
    elif args.oper == '/':
        dell = args.nums[0]
        for i in range(len(args.nums)):
            if i == 0:
                continue
            else:
                dell /= args.nums[i]
        return dell

result = f' {args.oper} '.join(map(str, args.nums)) + ' = ' + str(calc())

if args.verbose:
    print(result)

elif args.file:
    args.file.write(f'{result}\n')
    print(result)

elif args.quite:
    if not True:
        with open (f'{args.quite}', 'w') as f:
            f.write(result)

elif args.append:
    args.append.write(f'{result}\n')

else:
    print(calc())

