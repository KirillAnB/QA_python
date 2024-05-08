import pytest



def test_one(ultimate_param):
    assert ultimate_param == 42


def test_two(answer_gen):
    assert answer_gen == 42
