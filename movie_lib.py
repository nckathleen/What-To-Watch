all_movies = {} # movie objects
all_users = {}  # user objects

class Movie:
    ''' Class for movies '''
    def __init__(self, movie, title):
        self.id = movie
        self.title = title
        all_movies[self.id] = self
        self.ratings = {}
 #key is user_id, value is Rating object
    def __str__(self):
        return 'Movie(movie={}, title={})'.format(self.movie, self.title)

    def __repr__(self):
        return self__str__()

    # def get_movie_by_id(self, title):
    #     movie_id:title
    #     for movie_id in movie_dict
    def get_ratings(self):
        return self.ratings.values()

    def add_rating(self, rating):
        self.ratings[rating.user_id] = rating

class User:
    ''' Class for users '''
    def __init__(self, user):
        self.id = user
        all_users[self.id] = self

    # def get_rating_data(self, movie):
    #     [[id[i]
    #     for id in user_data_list]
    #     for i in range (len(user_data_list[0]))


class Rating:
    ''' Class for movie ratings '''
    def __init__(self, user, movie, stars):
        self.user = user
        self.movie = movie
        self.stars = stars
        all_movies[self.movie].add_rating(self)

    def __str__(self):
    return 'Movie(movie={}, title={})'.format(self.movie, self.title)
        return

    def __repr__(self):
        return self__str__()

#     def get_movie_rating(self, stars):
#         self.mid = mid
#         self.stars = stars

# def main():
#     #  Open data file and prepare contents for processing
#     with open("movie_data_50", newline='') as movie_data:  # Import file in lines
