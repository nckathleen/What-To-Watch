
from nose.tools import raises

# Movie data
movie_dict = {
    1 : 'Toy Story',
    2 : 'GoldenEye',
    3 : 'Four Rooms',
    4 : 'Get Shorty'
}

# User rating data
# User Movie Rating TimeStamp
user_data_list = (
[196, 242, 3, 881250949],
[186, 302, 3, 891717742],
[22, 377, 1, 878887116],
[244, 51, 2, 880606923],
[166, 346, 1, 886397596])

def test_get_movie_by_id():
    assert get_movie_by_id(title) == 'Toy Story'
    assert get_movie_by_id(title) != 'Toy Story'
    assert get_movie_by_id(title) != ''

#
# def test_get_user_ratings():
#     assert get_user_ratings(uid, stsrs) ==
#
#
# def test_get_movie_rating():
#     assert get_movie_rating(stars) != ' '


def test_get_rating_data():
    assert User.get_rating_data(movie) == '242'
    assert get_rating_data(movie) != ''
    assert get_rating_data(movie) != '196'
