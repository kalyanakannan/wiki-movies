from communication.Movies import Movies
from communication.Books import Books
from communication.Television import Televisions

class WikiFactory:
    
    def __init__(self, type) -> None:
        if(type == 'books'):
            return Movies()
        elif(type == 'television'):
            return Televisions()
        elif(type == 'Books'):
            return Books()
        
