import wikitextparser as wtp
class Template:

    def __init__(self, template_name, infobox_name) -> None:
        self.template_name = template_name
        self.infobox_name = infobox_name
        self.attributes = {}
    
    def setAttributes(self, content):
        """_summary_

        Args:
            attributes (_type_): _description_
        """
        parsed = wtp.parse(content)
        index = 0
        for template in parsed.templates:
            template.name.strip()
            if template.name.strip() == self.infobox_name:
                for attribute in parsed.templates[index].arguments:
                    self.attributes[attribute.name.strip()] = attribute.value.strip()
            index = index + 1

    def getAttribute(self, key):
        """_summary_

        Args:
            key (_type_): _description_

        Returns:
            _type_: _description_
        """
        return self.attributes[key]

    def getCurrentAttributes(self):

        return self.attributes.keys()

    def getTemplateName(self):
        return self.template_name
    
    def getInfoboxName(self):
        return self.infobox_name
