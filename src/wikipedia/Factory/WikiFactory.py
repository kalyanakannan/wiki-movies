from src.wikipedia.communication.Movies import Movies
from src.wikipedia.communication.Books import Books
from src.wikipedia.communication.Television import Televisions

class WikiFactory:
    
    def __init__(self) -> None:
        pass

    def createObject(self, type):
        targetclass = type.capitalize()
        return globals()[targetclass]()
        
