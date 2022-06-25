from src.wikipedia.Factory.WikiFactory import WikiFactory

def main():
    wiki_factory = WikiFactory()
    wiki = wiki_factory.createObject("Movies")
    get_data = True
    while get_data:
        movies = wiki.getMovies()
        if movies["movies"]:
            page_ids = wiki.getPageIds(movies["movies"])
            for ids in page_ids:
                posters = wiki.getPosters(wiki.mergePageIds(ids))
                page_details = wiki.getPageDetails(wiki.mergePageIds(ids))
                details = wiki.extractDetails(page_details)
                if movies["continue"]:
                    wiki.setContinue(movies["continue"])
                else:
                    get_data = False
        else:
            get_data = False

if __name__ == "__main__":
    main()