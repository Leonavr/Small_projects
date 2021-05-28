import cgi
import sqlite3
form = cgi.FieldStorage()
kan = form.getfirst("kan")
poisk = form.getfirst("poisk")
db = sqlite3.connect(r'C:\Users\leona\Downloads\chinook\chinook.db')
cg = db.cursor()
bg = db.cursor()
zg = db.cursor()
cg.execute(f'''SELECT FirstName, LastName, Country
				FROM customers WHERE Country LIKE "{kan}"''')
bg.execute(f'''SELECT FirstName, LastName, Country
				FROM customers WHERE FirstName LIKE "{poisk}"''')
zg.execute(f'''SELECT FirstName, LastName, Country
				FROM customers WHERE FirstName LIKE "poisk" AND Country LIKE "{kan}"''')
print("Content-type: text/html\n")
print('''<!DOCTYPE html>
    <html lang="ru">
        <head>
            <meta charset="utf-8">
            <body>''')
if kan:
	for FirstName, LastName, Country in cg:
		print('Поиск по стране: ')
		print(f"<li>Имя: {FirstName} | Фамилия: {LastName} | Страна: {Country}</li>")
elif poisk:
	for FirstName, LastName, Country in bg:
		print('Поиск по имени: ')
		print(f"<li>Имя: {FirstName} | Фамилия: {LastName} | Страна: {Country}</li>")
else:
	print("Вы ничего не ввели")


print('''
<a href="..\index.html">На главную страницу</a>
</body>
</html>''')
