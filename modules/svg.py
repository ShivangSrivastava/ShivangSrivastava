from xml.dom import minidom


class SVGTextModifier:
    def __init__(self, input_svg):
        self.input_svg = input_svg
        self.doc = minidom.parse(input_svg)

    def modify_text(self, tag="tspan", id_name=None, new_value=None):
        elements = self.doc.getElementsByTagName(tag)
        for elem in elements:
            if id_name and elem.getAttribute("id") != id_name:
                continue
            if elem.firstChild:
                elem.firstChild.nodeValue = new_value

    def save(self, output_svg=None):
        with open(output_svg or self.input_svg, "w") as file:
            self.doc.writexml(file)
