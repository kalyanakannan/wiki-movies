from src.wikipedia.templates.Template import Template
from src.library.configManager import ConfigManager
class MovieTemplate(Template):

    def __init__(self):
        config = ConfigManager()
        Template.__init__(self, config.get("templates")["movie"], config.get("infoBox")["movie"])

    def getAllAttributes(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return ["name","image","alt","caption","native_name","director","writer","screenplay","story","based_on","producer","starring","narrator","cinematography","editing","music","studio","distributor","released","runtime","country","language","budget","gross",
        ]