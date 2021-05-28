import sqlite3

db = sqlite3.connect(r'C:\Users\leona\Downloads\chinook\places.sqlite')
#1
cg = db.cursor()
cg.execute('''SELECT datetime(h.visit_date / 1000000, "unixepoch"), p.url, p.title
				FROM moz_historyvisits h INNER JOIN moz_places p ON h.place_id = p.id
				LIMIT 13''')

print("Content-type: text/html")
print()
print('<!DOCTYPE html>')
print ('''
<html>
<head>
<meta charset="utf-8"/>
</head>
<body>''')
print('''
<h2><font color="navy">List of visits</font></h2>''')

for i in cg:
	print(f'<li>{i[0]} <a href="{i[1]}">{i[2]}</a></li>')

print('''

<b><a href="..\index.html">На главную страницу</a></b>

</body>
</html>''')


