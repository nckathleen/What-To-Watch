import csv

all_movies = {} # movie objects
all_users = {}  # user objects
ratings = {}  # ratings key = mid

# with open('u.data') as f:
#     reader = csv.reader(f, fieldnames=['user', 'movie', 'rating', 'timestamp'], delimiter='|')
#     for row in reader:
#         all_users[x] = row
#

with open('u.item', encoding='latin_1') as f:
    reader = csv.reader(f, delimiter='|')
    for row in reader:
        all_movies[row[0]] = all_movies(
                            mid = row[0],
                            title = row[1], release_date = row[2],
                            vid_rel_date = row[3], IMDb_url = row[4],
                            unk_genre = row[5], action = row[6],
                            adventure = row[7], animation = row[8],
                            childrens = row[9], comedy = row[10],
                            crime = row[11], documentary = row[12],
                            drama = row[13], fantasy = row[14],
                            film_noir = row[15], horror = row[16],
                            musical = row[17], mystery = row[18],
                            romance = row[19], sci_fi = row[20],
                            thriller = row[21], war = row[22],
                            western = row[23] )
#
#
# with open('u.user') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         all_users[row[0]] = User(
#                             uid = row[0],
#                             age = row[1],
#                             gender = row[2],
#                             occupation = row[3],
#                             zip_code = row[4])
#
#
with open('u.data')as f:
    reader = csv.reader(f)
        key = all_movies[0]
        for row in reader:
            reader =




# class Movie:
#     ''' Class for movies '''
#     def __init__(self, movie, title):
#         self.id = movie
#         self.title = title
#         all_movies[self.id] = self
#         self.ratings = {}
#
#  #key is user_id, value is Rating object
#     def __str__(self):
#         return 'Movie(movie={}, title={})'.format(self.movie, self.title)
#
#     def __repr__(self):
#         return self__str__()
#
#     def calc_avg_rating():
# # For item_id in Ratings, get all ratings and average them.
# # Store in all_movies.
#         for mid in all_movies:
#
#
#
#     # def get_movie_by_id(self, title):
#     #     movie_id:title
#     #     for movie_id in movie_dict
#     def get_ratings(self):
#         return self.ratings.values()
#
#     def add_rating(self, rating):
#         self.ratings[rating.user_id] = rating
#
# class User:
#     ''' Class for users '''
#     def __init__(self, user):
#         self.id = user
#         all_users[self.id] = self
#
#
#     # def get_rating_data(self, movie):
#     #     [[id[i]
#     #     for id in user_data_list]
#     #     for i in range (len(user_data_list[0]))
#
# class Rating:
#     ''' Class for movie ratings '''
#     def __init__(self, user, movie, stars):
#         self.user = user
#         self.movie = movie
#         self.stars = stars
#         all_movies[self.movie].add_rating(self)
#
#     def __str__(self):
#     return 'Movie(movie={}, title={})'.format(self.movie, self.title)
#         return
#
#     def __repr__(self):
#         return self__str__()
#
# #     def get_movie_rating(self, stars):
# #         self.mid = mid
# #         self.stars = stars
#
# # def main():
# #     #  Open data file and prepare contents for processing
# #     with open("movie_data_50", newline='') as movie_data:  # Import file in lines
