from utils import *
import pytest


@pytest.fixture
def card_number():
    return "1234567890123456"


@pytest.fixture
def long_card_number():
    return "12345678901234567890"


@pytest.fixture
def date_string():
    return "2023-10-03T12:34:56.789Z"


def test_blurer(card_number, long_card_number):
    assert blurer(card_number) == "1234 56** **** 3456"
    assert blurer(long_card_number) == "**7890"
    assert blurer("1234") is None
    assert blurer("123456789012345") is None


def test_second_string(card_number, long_card_number):
    assert second_string(f"значение по ключу from {card_number}") == "значение по ключу from 1234 56** **** 3456"
    assert second_string(f"значение по ключу to {card_number}") == "значение по ключу to 1234 56** **** 3456"
    assert second_string(f"значение по ключу from {long_card_number}") == "значение по ключу from **7890"
    assert second_string(f"значение по ключу to {long_card_number}") == "значение по ключу to **7890"


def test_date_reformat(date_string):
    assert date_reformat(date_string) == "03.10.2023"
    assert date_reformat("2023-01-01T00:00:00.000Z") == "01.01.2023"
    assert date_reformat("2023-12-31T23:59:59.999Z") == "31.12.2023"
    assert date_reformat("2023-10-03") == "03.10.2023"
