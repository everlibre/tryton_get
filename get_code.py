import urllib2
import re
import subprocess
subprocess.call(['hg', 'clone', 'http://hg.tryton.org/trytond'])
subprocess.call(['hg', 'clone', 'http://hg.tryton.org/tryton'])

res = urllib2.urlopen("http://hg.tryton.org/modules/?sort=name")
content = res.read()
pattern = '<td><a href="/modules/(.*)/">'
list_modules = re.findall(pattern, content)
for module in list_modules:
    subprocess.call(['hg', 'clone', 'http://hg.tryton.org/modules/'+module,
        'trytond/trytond/modules/'+module])
