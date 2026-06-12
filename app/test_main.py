from app.main import get_human_age


def test_get_human_age_zero():
    assert get_human_age(0, 0) == [0, 0]


def test_get_human_age_less_than_first_stage():
    assert get_human_age(14, 14) == [0, 0]


def test_get_human_age_first_stage():
    assert get_human_age(15, 15) == [1, 1]


def test_get_human_age_second_stage_boundary():
    assert get_human_age(24, 24) == [2, 2]


def test_get_human_age_middle_values():
    assert get_human_age(27, 27) == [2, 2]


def test_get_human_age_third_stage_boundary():
    assert get_human_age(28, 28) == [3, 2]


def test_get_human_age_large_values():
    assert get_human_age(100, 100) == [21, 17]
