import sqlite3

db = sqlite3.connect('places.sqlite')
#1
cg = db.cursor()
cg.execute('''SELECT datetime(h.visit_date / 1000000, "unixepoch"), p.url, p.title
				FROM moz_historyvisits h INNER JOIN moz_places p ON h.place_id = p.id;''')
for i in cg:
	print (i)
cg.close()
