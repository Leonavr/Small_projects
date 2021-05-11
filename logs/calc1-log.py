import argparse
import logging

# create logger
logger = logging.getLogger('Calculator logs')
logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

ch.setFormatter(formatter)

logger.addHandler(ch)

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
    logger.info(f'Ход операции: {result}')

elif args.file:
    args.file.write(f'{result}\n')
    logger.info('Файл записан')
    logger.info(f'Ход операции: {result}')

elif args.quite:
    if not True:
        with open (f'{args.quite}', 'w') as f:
            f.write(result)
        logger.info('Файл записан')

elif args.append:
    args.append.write(f'{result}\n')
    logger.info('Файл дополнен')

elif args.oper not in ['+','-','*','/'] :
        logger.error('Что-то пошло не так')
        logger.critical('Алярм!!!')
else:
    logger.info(f'Результат: {calc()}')

