from src.wikipedia.Factory.WikiFactory import WikiFactory

def main():
    wiki_factory = WikiFactory()
    wiki = wiki_factory.createObject("Movies")
    get_movie = True
    eicontinue = False
    while get_movie:
        movies = wiki.getMovies(eicontinue)
        page_ids = wiki.getPageIds(movies[0])
        for ids in page_ids:
            posters = wiki.getPosters(wiki.mergePageIds(ids))
            page_details = wiki.getPageDetails(wiki.mergePageIds(ids))
            details = wiki.extractDetails(page_details)
            wiki.setContinue(movies[1])
            eicontinue = True
            get_movie = False

if __name__ == "__main__":
    main()