""" Testing for poker_dice.py """
from poker_dice import calculate_points


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
