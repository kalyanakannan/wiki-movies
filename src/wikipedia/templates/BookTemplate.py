from src.wikipedia.templates.Template import Template
from src.library.configManager import ConfigManager
class BookTemplate(Template):

    def __init__(self):
        config = ConfigManager()
        Template.__init__(self, config.get("templates")["book"], config.get("infoBox")["book"])

    def getAllAttributes(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return ["italic_title","name","image","image_size","border","alt","caption","author","audio_read_by","title_orig","orig_lang_code","title_working","translator","illustrator","cover_artist","country","language","series","release_number","subject","genre","set_in","publisher","publisher2","pub_date","english_pub_date","published","media_type","pages","awards","isbn","isbn_note","oclc","dewey","congress","preceded_by","followed_by","native_wikisource","wikisource","notes","exclude_cover","website",
        ]