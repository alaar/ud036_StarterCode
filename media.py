class Movie():
    """ Movie class

    Attributes:
        title: string represents the title of the movie
        poster_image_url: string representing the url of the movie's poster
        trailer_youtube_url: string representing the url of the movie's trailer
    """

    # Constructor for the Movie class
    def __init__(self, movie_title, poster_image_url, trailer_youtube_url):
        self.title = movie_title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
