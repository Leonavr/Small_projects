import os
path = input('Введите путь к папке: ')
files = os.listdir(path)
files_mp3 = [i for i in files if i.endswith('.mp3')]

def create_playlist(playlist_path, files):
	with open(playlist_path, 'w', encoding='utf-8') as p:
		for f in files_mp3:
			print(f, file=p)
'''name = path.split('\\')[-1]
artist = name.split('-')[0]'''

d = 'audio/mp3'
def html_playlist():
	f = open ('playlist.html','w', encoding='utf-8')
	f.write('''<html>
		<body>
		<h2><font color="navy">Playlist</font></h2>
		<table cellspacing="2" border="1" cellpadding="5">
		''')
	for i in files_mp3:
		f.write(f'<audio controls> <source src={i} type={d}></audio>')
	f.write('''
	</table>
	</body>
	</html>''')

create_playlist('my.m3u',files_mp3)
html_playlist()
