from app.main import get_human_age


def test_type_of_output_should_be_a_list() -> None:
    assert isinstance(get_human_age(0, 0), list)


def test_should_return_zero_years_when_ages_are_zero() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_should_return_zero_years_when_age_less_than_15() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_should_return_one_years_when_ages_equal_15() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_should_return_two_years_when_ages_equal_24() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_cat_age_greater_than_dog_age() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_validate_years_with_large_ages() -> None:
    assert get_human_age(100, 100) == [21, 17]
