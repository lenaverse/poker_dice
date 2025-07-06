""" Testing for poker_dice.py """
from poker_dice import calculate_points, determine_winner, handle_draw

""" Test for the calculate_points function. """


def test_calculate_points_five_kind():
    assert calculate_points([5, 5, 5, 5, 5]) == 50


def test_calculate_points_four_kind():
    assert calculate_points([5, 5, 5, 5, 3]) == 30


def test_calculate_points_full_house():
    assert calculate_points([5, 5, 5, 2, 2]) == 20


def test_calculate_points_three_kind():
    assert calculate_points([5, 5, 5, 1, 2]) == 15


def test_calculate_points_two_pairs():
    assert calculate_points([5, 5, 1, 1, 3]) == 5


def test_calculate_points_one_pair():
    assert calculate_points([5, 5, 1, 2, 6]) == 2


def test_calculate_points_highest_die():
    assert calculate_points([1, 2, 3, 4, 5]) == 1


""" Tests for the determine_winner function. """


def test_player_wins_1():
    assert "You win!" in determine_winner([5, 5, 5, 5, 5], [1, 2, 3, 4, 5])


def test_player_wins_2():
    assert "You win!" in determine_winner([5, 5, 5, 5, 5], [5, 5, 5, 5, 2])


def test_player_wins_3():
    assert "You win!" in determine_winner([5, 5, 5, 4, 3], [5, 5, 6, 6, 2])


# Test fails - there should not be draws unless both players have the
# exact same numbers


def test_player_wins_4():
    assert "You win!" in determine_winner([2, 3, 4, 5, 6], [1, 2, 3, 4, 5])


""" Test handle_draw function """


def test_handle_draw_true_draw():
    assert handle_draw([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]) == "Draw!"
