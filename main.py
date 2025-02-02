from datetime import datetime
from xml.dom import minidom

FILE_NAME = "terminal.svg"


doc = minidom.parse(FILE_NAME)


new_datetime = datetime.now().strftime("%a %b %d %H:%M:%S %Y on tty1")

tspans = doc.getElementsByTagName('tspan')

for tspan in tspans:
    if tspan.getAttribute('id') == 'last-login':
        tspan.firstChild.nodeValue = new_datetime

with open(FILE_NAME, 'w') as file:
    doc.writexml(file)
