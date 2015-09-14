import csv

all_movies = {} # movie objects
all_users = {}  # user objects


class Movie:
    ''' Class for movies '''
    def __init__(self, movie, title):
        self.id = movie
        self.title = title
        all_movies[self.id] = self
        self.ratings = {}   # key: user id, value: rating object

    def add_rating(self, rating):
        self.ratings[rating.user_id] = rating

    def get_ratings(self):
        return self.ratings.values()  # creates a list

    def __str__(self):
        return 'Movie(movie={}, title={})'.format(self.id, repr(self.title))

    def __repr__(self):
        return self.__str__()


class User:
    ''' Class for users '''
    def __init__(self, user):
        self.id = user
        all_users[self.id] = self


class Rating:
    ''' Class for movie ratings '''
    def __init__(self, user, movie, stars):
        self.user_id = user
        self.movie_id = movie
        self.stars = stars
        all_movies[self.movie_id].add_rating(self)

    def __str__(self):
        return 'Rating(user_id = {}, movie_id = {}], stars = {})'.format(self.user_id, self.movie_id, self.stars)

    def __repr__(self):
        return self.__str__()

# Read in files

# with open('u.item', encoding='latin_1') as f:
#     reader = csv.reader(f, delimiter='|')
#     for row in reader:
#         all_movies[row[0]] = Movie(mid = row[0],
#                             title = row[1], release_date = row[2],
#                             vid_rel_date = row[3], IMDb_url = row[4],
#                             genres = row[5], action = row[6],
#                             adventure = row[7], animation = row[8],
#                             childrens = row[9], comedy = row[10],
#                             crime = row[11], documentary = row[12],
#                             drama = row[13], fantasy = row[14],
#                             film_noir = row[15], horror = row[16],
#                             musical = row[17], mystery = row[18],
#                             romance = row[19], sci_fi = row[20],
#                             thriller = row[21], war = row[22],
#                             western = row[23])
#
# with open('u.user') as f:
#     reader = csv.reader(f, delimiter='|')
#     for row in reader:
#         all_users[row[0]] = User(uid = row[0],
#                             age = row[1],
#                             gender = row[2],
#                             occupation = row[3],
#                             zip_code = row[4])
#
# with open('u.data')as f:
#     reader = csv.DictReader(f, fieldnames = ['uid', 'mid', 'rating'], delimiter = '\t')
# #        key = all_movies[0]
#     for row in reader:
#         print(row)
#         Rating[row[0]] = [uid, mid, rating, timestamp]
# #        print(row(1))
