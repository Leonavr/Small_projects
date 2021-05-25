import sqlite3

db = sqlite3.connect('places.sqlite')
#1
cg = db.cursor()
cg.execute('''SELECT datetime(h.visit_date / 1000000, "unixepoch"), p.url, p.title
				FROM moz_historyvisits h INNER JOIN moz_places p ON h.place_id = p.id
				LIMIT 13''')
f = open('top_13_list.html','w', encoding = 'utf-8')
f.write('''<html>
		<body>
		<h2><font color="navy">List of visits</font></h2>
		<ul>''')
for i in cg:
	f.write(f"<li>Visit time: {i[0]} <a href={i[1]}>{i[2]}</a> </li>")
f.write('''</ul>  
	</form>
	</body>
	</html>''')
