import sqlite3

db = sqlite3.connect(r'C:\Users\leona\Downloads\chinook\chinook.db')
cg = db.cursor()
cg.execute('''SELECT FirstName, LastName, Country
				FROM customers
				LIMIT 13''')
print("Content-type: text/html")
print()
print('''
<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html" charset="utf-8">
</head>
<h2><font color="navy">List of visits</font></h2>
<body>
<ul>''')

for i in cg:
	print(f"<li>Имя: {i[0]} | Фамилия: {i[1]} | Страна: {i[2]}</li>")
print(f'''
</ul>
<a href="..\index.html">На главную страницу</a>
<body/>
<html/>''')
