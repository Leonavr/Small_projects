import datetime
vrem = datetime.datetime.strftime(datetime.datetime.now(), "%Y.%m.%d %H:%M:%S")
# служебные заголовки
print("Content-type: text/html")
print()
# содержимое сайта
print('''
<!DOCTYPE html>
<html class="client-nojs" lang="ru" dir="ltr">
<head>
<meta http-equiv="Content-Type" content="text/html" charset="utf-8">
</head>''')
print('''
<body>''')
print('<title>Дата и время</title>')
print(f'<h1>Текущее время:</h1>')
print(f'<p>{vrem}</p>')
print('''
<a href="..\index.html">На главную страницу</a>
<body/>
<html/>''')
	
