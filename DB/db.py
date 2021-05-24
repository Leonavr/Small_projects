import sqlite3

db = sqlite3.connect('chinook.db')
#1
cg = db.cursor()
cg.execute('''SELECT * FROM customers''')
for i in cg:
	print (i)
cg.close()
#2
bg = db.cursor()
india = bg.execute('''SELECT * FROM customers WHERE country LIKE "India" ORDER BY FirstName;''')
for i in india:
	with open ('India.txt', 'a', encoding = 'utf-8') as f:
		f.write(f'{i}\n')
bg.close()
#3
ag = db.cursor()
brazil = ag.execute('''SELECT * FROM customers WHERE country LIKE "Brazil" ORDER BY LastName;''')
for i in brazil:
	with open ('Brazil.txt', 'a', encoding = 'utf-8') as f:
		f.write(f'{i}\n')
ag.close()
#4
ag1 = db.cursor()
brazil_india = ag1.execute('''SELECT * FROM customers WHERE country LIKE "Brazil" OR country LIKE "India" ORDER BY CustomerID;''')
for i in brazil_india:
	with open ('Brazil_India.txt', 'a', encoding = 'utf-8') as f:
		f.write(f'{i}\n')
ag1.close()
#5
eg = db.cursor()
spravochnik = eg.execute('''SELECT employees.EmployeeId,
							employees.FirstName,
							employees.LastName,
							'---->',
							customers.FirstName,
							customers.LastName
							FROM employees 
							INNER JOIN customers ON employees.EmployeeId = customers.SupportRepId
							ORDER BY employees.EmployeeId;''')
for i in spravochnik:
	with open ('Spravochnik.txt', 'a', encoding = 'utf-8') as f:
		f.write(f'{i}\n')
eg.close()
