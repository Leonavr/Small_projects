import sqlite3

db = sqlite3.connect('places.sqlite')
#1
cg = db.cursor()
cg.execute('''SELECT datetime(h.visit_date / 1000000, "unixepoch"), p.url, p.title
				FROM moz_historyvisits h INNER JOIN moz_places p ON h.place_id = p.id
				LIMIT 13''')
f = open('top_13_table.html','w', encoding = 'utf-8')
f.write('''<html>
		<body>
		<h2><font color="navy">List of visits</font></h2>
		<table cellspacing="2" border="1" cellpadding="5">
		<caption>Journal of visits</caption>
		<tr>
		<th><font color="red">Visit time</font></th>
		<th><font color="navy">URL</font></th>
		</tr>''')
for i in cg:
	f.write(f"<tr><td>{i[0]}</td> <td><a href={i[1]}>{i[2]}</a> </td><tr>")
f.write('''</table>
	</body>
	</html>''')
