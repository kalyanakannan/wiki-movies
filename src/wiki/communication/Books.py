from wiki.templates.BookTemplate import BookTemplate
from wiki.communication.Api import WikiApi
class Books(BookTemplate, WikiApi):
    """_summary_

    Args:
        BookTemplate (_type_): _description_
        WikiApi (_type_): _description_
    """

    def __init__(self):
        WikiApi.__init__(self)
        BookTemplate.__init__(self)
        self.params = {
            "action": "query",
            "list": "embeddedin",
            "einamespace":0,
            "eilimit":500,
            "eititle": self.template_name,
        }

    
    def extractDetails(self,page_details) -> dict:
        """extract book details like name,director name ...etc
        Args:
            page_details (_type_): _description_
        """
        book_details = []
        for pageid in page_details:
            content = page_details[pageid]['revisions'][0]["*"]
            self.setAttributes(content)
            details = self.extractTemplateAttributeByPageId(content,self.infobox_name, pageid)
            book_details.append(details)
        return book_details

    def getBooks(self, eicontinue=False):
        """_summary_

        Args:
            eicontinue (bool, optional): _description_. Defaults to False.

        Returns:
            _type_: _description_
        """
        self.setFormat()
        if (eicontinue):
            self.params['eicontinue'] = self.getContinue()
        books = self.request.get(url=self.BaseUrl, params=self.params).json()
        return [books["query"]["embeddedin"],books["continue"]["eicontinue"]]
