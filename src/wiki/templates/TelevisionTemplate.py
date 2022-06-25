from wiki.templates.Template import Template
class TelevisionTemplate(Template):

    def __init__(self):
        Template.__init__(self,"Template:Infobox_television","Infobox television")

    def getAllAttributes(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return ["image","image_upright","image_size","image_alt","caption","alt_name","native_name","genre","creator","based_on","inspired_by","developer","writer","screenplay","story","director","creative_director","presenter","starring","judges","voices","narrated","theme_music_composer","open_theme","end_theme","composer","country","language","num_seasons","num_episodes","list_episodes","executive_producer","producer","news_editor","location","cinematography","animator","editor","camera","runtime","company","distributor","budget","network","picture_format","audio_format","first_aired","last_aired","preceded_by","followed_by","related",
        ]