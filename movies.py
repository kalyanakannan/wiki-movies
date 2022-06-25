from wiki.communication.Movies import Movies

def main():
    wiki_movies = Movies()
    get_movie = True
    eicontinue = False
    while get_movie:
        movies = wiki_movies.getMovies(eicontinue)
        page_ids = wiki_movies.getPageIds(movies[0])
        for ids in page_ids:
            posters = wiki_movies.getPosters(wiki_movies.mergePageIds(ids))
            page_details = wiki_movies.getPageDetails(wiki_movies.mergePageIds(ids))
            details = wiki_movies.extractDetails(page_details)
            wiki_movies.setContinue(movies[1])
            eicontinue = True
            get_movie = False

if __name__ == "__main__":
    main()