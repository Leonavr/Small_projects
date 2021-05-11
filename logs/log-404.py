import logging
with open ('red_apple.org.access.log', 'r') as f:
	f = f.readlines()
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.ERROR)
for i in f:
	if '404' in i.split()[8]:
		logging.error(f'{i}')

f.close()

