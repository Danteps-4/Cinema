class Movie:
    def __init__(self, id, title, tagline, genres, overview, release_date, vote_average, runtime, cast, recommendations, reviews, image):
        self.id = id
        self.title = title
        self.tagline = tagline
        self.genres = genres
        self.overview = overview
        self.release_date = release_date
        self.vote_average = vote_average
        self.runtime = runtime
        self.cast = cast
        self.recommendations = recommendations
        self.reviews = reviews
        self.image = image

    def __str__(self):
        return self.title