
from nose.tools import *
#
# # Movie data
# movie_dict = {
#     1 : 'Toy Story',
#     2 : 'GoldenEye',
#     3 : 'Four Rooms',
#     4 : 'Get Shorty'
# }
#
# # User rating data
# # User Movie Rating TimeStamp
# user_data_list = (
# [196, 242, 3, 881250949],
# [186, 302, 3, 891717742],
# [22, 377, 1, 878887116],
# [244, 51, 2, 880606923],
# [166, 346, 1, 886397596])

print(all_movies)

print(all_movies[3])

user1 = User(5)
user2 = User(12)
movie1 = Movie(3, 'Toy Story')
movie2 = Movie(9, 'Pretty Woman')
rating1 = Rating(user1.id, movie1.id, 4)
rating2 = Rating(user2.id, movie2.id, 1)
rating3 = Rating(user1.id, movie1.id, 3)
rating4 = Rating(user2.id, movie1.id, 2)

def test_user_creation():
    assert User1.id == 5
    assert User2.id == 12

def test_movie_creation():
    assert Movie1.id == 3
    assert Movie1.title == 'Toy story'
    assert Movie2.id == 9
    assert Movie2.title == 'Pretty Woman'

def test_rating_creation():
    assertrating1.user.id == rating3.user.id == user1.id
    assertrating2.user.id == rating4.user.id == user2.id
    assert rating1.stars == 4
    assert rating2.stars == 1
    assert rating3.stars == 3
    assert rating4.stars == 2

def test_find_ratings_for_movie():
    # return a list of Rating objects
    toy_story_ratings = all_movies[movie1.id].get_ratings()
    print len(toy_story_ratings)
    print (toy_story_ratings)
    assert len(toy_story_ratings) == 2


# def test_get_movie_by_id():
#     assert get_movie_by_id(title) == 'Toy Story'
#     assert get_movie_by_id(title) != 'Toy Story'
#     assert get_movie_by_id(title) != ''
#
# #
# # def test_get_user_ratings():
# #     assert get_user_ratings(uid, stsrs) ==
# #
# #
# # def test_get_movie_rating():
# #     assert get_movie_rating(stars) != ' '
#
#
# def test_get_rating_data():
#     assert User.get_rating_data(movie) == '242'
#     assert get_rating_data(movie) != ''
#     assert get_rating_data(movie) != '196'
