import fresh_tomatoes
import media


# Creating 9 instances of the class Movie of the media Module
django = media.Movie(
                    "Django Unchained",
                    "https://goo.gl/sDByYA",
                    "https://www.youtube.com/watch?v=eUdM9vrCbow")

shawshank_redemption = media.Movie(
                    "The Shawshank Redemption",
                    "https://goo.gl/BPqfPD",
                    "https://www.youtube.com/watch?v=6hB3S9bIaco")

mean_girls = media.Movie(
                    "Mean Girls",
                    "https://goo.gl/c6KPZK",
                    "https://www.youtube.com/watch?v=KAOmTMCtGkI")

forrest_gump = media.Movie(
                    "Forrest Gump",
                    "https://goo.gl/hmKFUu",
                    "https://www.youtube.com/watch?v=uPIEn0M8su0")

the_big_sick = media.Movie(
                    "The Big Sick",
                    "https://goo.gl/kkjbkM",
                    "https://www.youtube.com/watch?v=PJmpSMRQhhs")

pitch_perfect = media.Movie(
                    "Pitch Perfect",
                    "https://goo.gl/jUvB5F",
                    "https://www.youtube.com/watch?v=tjlCqm6j0d0")

jump_street = media.Movie(
                    "21 Jump Street",
                    "https://goo.gl/yeopNC",
                    "https://www.youtube.com/watch?v=ISJR4rVO0TQ")

spiderman_homecoming = media.Movie(
                    "Spider-Man: Homecoming",
                    "https://goo.gl/Rn2ZJS",
                    "https://www.youtube.com/watch?v=n9DwoQ7HWvI")

bridesmaids = media.Movie(
                    "Bridesmaids",
                    "https://goo.gl/QFZEL8",
                    "https://www.youtube.com/watch?v=1UW9Zks5L2A")

# Grouping the movies in a list
favorite_movies = [mean_girls, the_big_sick, pitch_perfect,
                   jump_street, spiderman_homecoming, bridesmaids,
                   forrest_gump, django, shawshank_redemption]


# The open_movies_page function takes a list of movies as its argument
# It then creates an HTML file which will display all of the movies
# in the browser
fresh_tomatoes.open_movies_page(favorite_movies)
