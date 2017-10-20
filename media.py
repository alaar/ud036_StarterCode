class Movie():
    """ Movie class

    Attributes:
        title: A string representing the title of the movie
        poster_image_url: An string representing the url of the movie's poster
        trailer_youtube_url: A string representing the url of the movie's trailer
    """

    # Constructor for the Movie class
    def __init__(self, movie_title, poster_image_url, trailer_youtube_url):
        self.title = movie_title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    
