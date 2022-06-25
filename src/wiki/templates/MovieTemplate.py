from wiki.templates.Template import Template
class MovieTemplate(Template):

    def __init__(self):
        Template.__init__(self, "Template:Infobox_film", "Infobox film")

    def getAllAttributes(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return ["name","image","alt","caption","native_name","director","writer","screenplay","story","based_on","producer","starring","narrator","cinematography","editing","music","studio","distributor","released","runtime","country","language","budget","gross",
        ]