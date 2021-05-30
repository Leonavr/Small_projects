#№2,3 HW
from mako.template import Template
import glob
filez = sorted(glob.glob("*.mp3"))
t = Template(filename = 'template_3.m3u')
m3 = t.render(list_of_files = filez)
print(m3)
f = open('1.html', 'w')
f.write(m3)
f.close()
