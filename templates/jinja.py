from jinja2 import Template
import glob
filez = sorted(glob.glob("*.mp3"))
html = open ('template_4.m3u').read()
template = Template(html)

m3 = template.render(filez = filez)
	

f = open('4.html', 'w')
f.write(m3)
f.close()
