from src.wikipedia.templates.BookTemplate import BookTemplate
from src.wikipedia.communication.Api import Api
class Books(BookTemplate, Api):
    """_summary_

    Args:
        BookTemplate (_type_): _description_
        Api (_type_): _description_
    """

    def __init__(self):
        Api.__init__(self)
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

    def getBooks(self):
        """_summary_

        Args:
            eicontinue (bool, optional): _description_. Defaults to False.

        Returns:
            _type_: _description_
        """
        self.setFormat()
        response = {
            "books":"",
            "continue":""
        }
        if (self.eicontinue):
            self.params['eicontinue'] = self.getContinue()
        books = self.request.get(url=self.BaseUrl, params=self.params).json()
        if "embeddedin" in books["query"]:
            response['books'] = books["query"]["embeddedin"]
        if "continue" in books:
            response['continue'] = books["continue"]["eicontinue"]
        return response
