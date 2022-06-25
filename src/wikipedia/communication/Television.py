from src.wikipedia.templates.TelevisionTemplate import TelevisionTemplate
from src.wikipedia.communication.Api import Api
class Televisions(TelevisionTemplate, Api):
    """_summary_

    Args:
        TelevisionTemplate (_type_): _description_
        Api (_type_): _description_
    """
    def __init__(self):
        Api.__init__(self)
        TelevisionTemplate.__init__(self)
        self.params = {
            "action": "query",
            "list": "embeddedin",
            "einamespace":0,
            "eilimit":500,
            "eititle": self.template_name,
        }

    
    def extractDetails(self,page_details) -> dict:
        """extract television details like name,director name ...etc
        Args:
            page_details (_type_): _description_
        """
        television_details = []
        for pageid in page_details:
            content = page_details[pageid]['revisions'][0]["*"]
            self.setAttributes(content)
            details = self.extractTemplateAttributeByPageId(content,self.infobox_name, pageid)
            television_details.append(details)
        return television_details

    def getTelevisions(self):
        """_summary_

        Args:
            eicontinue (bool, optional): _description_. Defaults to False.

        Returns:
            _type_: _description_
        """
        self.setFormat()
        response = {
            "televisions":"",
            "continue":""
        }
        if (self.eicontinue):
            self.params['eicontinue'] = self.getContinue()
        televisions = self.request.get(url=self.BaseUrl, params=self.params).json()
        if "embeddedin" in televisions["query"]:
            response['televisions'] = televisions["query"]["embeddedin"]
        if "continue" in televisions:
            response['continue'] = televisions["continue"]["eicontinue"]
        return response
