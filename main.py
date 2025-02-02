from datetime import datetime
from xml.dom import minidom

FILE_NAME = "terminal.svg"


doc = minidom.parse(FILE_NAME)


# Get the current date and time in the desired format
new_datetime = datetime.now().strftime("%a %b %d %H:%M:%S %Y on tty1")

# Find all <tspan> elements and search for the one with the id "last-login"
tspans = doc.getElementsByTagName('tspan')

for tspan in tspans:
    if tspan.getAttribute('id') == 'last-login':
        # Update the text content inside the <tspan> element
        tspan.firstChild.nodeValue = new_datetime

# Save the modified SVG back to a file
with open(FILE_NAME, 'w') as file:
    doc.writexml(file)
