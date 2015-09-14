
from nose.tools import *
from movie_lib import *

user1 = User(5)
user2 = User(12)
movie1 = Movie(3, 'Toy Story')
movie2 = Movie(9, 'Pretty Woman')
rating1 = Rating(user1.id, movie1.id, 4)
rating2 = Rating(user2.id, movie2.id, 1)
rating3 = Rating(user1.id, movie2.id, 3)
rating4 = Rating(user2.id, movie1.id, 2)

def test_user_creation():
    assert user1.id == 5
    assert user2.id == 12

def test_movie_creation():
    assert movie1.id == 3
    assert movie1.title == 'Toy Story'
    assert movie2.id == 9
    assert movie2.title == 'Pretty Woman'

def test_rating_creation():
    assert rating1.user_id == rating3.user_id == user1.id
    assert rating2.user_id == rating4.user_id == user2.id
    assert rating1.user_id == rating3.user_id == user1.id
    assert rating2.user_id == rating4.user_id == user2.id
    assert rating1.stars == 4
    assert rating2.stars == 1
    assert rating3.stars == 3
    assert rating4.stars == 2

def test_find_ratings_for_movie():
    # the below returns a list of Rating objects
    toy_story_ratings = all_movies[movie1.id].get_ratings()
    print(len(toy_story_ratings))
    print(toy_story_ratings)
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
