from urllib import response
from src.wikipedia.templates.MovieTemplate import MovieTemplate
from src.wikipedia.communication.Api import Api
class Movies(MovieTemplate, Api):

    def __init__(self):
        Api.__init__(self)
        MovieTemplate.__init__(self)
        self.params = {
            "action": "query",
            "list": "embeddedin",
            "einamespace":0,
            "eilimit":500,
            "eititle": self.template_name,
        }
    
    def extractDetails(self,page_details) -> dict:
        """extract movie details like name,director name ...etc
        Args:
            page_details (_type_): _description_
        """
        movie_details = []
        for pageid in page_details:
            content = page_details[pageid]['revisions'][0]["*"]
            self.setAttributes(content)
            details = self.extractTemplateAttributeByPageId(content,self.infobox_name, pageid)
            movie_details.append(details)
        return movie_details

    def getMovies(self):
        """_summary_

        Args:
            eicontinue (bool, optional): _description_. Defaults to False.

        Returns:
            _type_: _description_
        """
        self.setFormat()
        response = {
            "movies":"",
            "continue":""
        }
        if (self.eicontinue):
            self.params['eicontinue'] = self.getContinue()
        movies = self.request.get(url=self.BaseUrl, params=self.params).json()
        if "embeddedin" in movies["query"]:
            response['movies'] = movies["query"]["embeddedin"]
        if "continue" in movies:
            response['continue'] = movies["continue"]["eicontinue"]
        return response
