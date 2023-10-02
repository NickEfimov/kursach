from utils import *


def test_blurer():
    assert blurer("1234567890123456") == "1234 56** **** 3456"
    assert blurer("12345678901234567890") == "**7890"
    assert blurer("1234") is None
    assert blurer("123456789012345") is None

def test_second_string():
    assert second_string("значение по ключу from 1234567890123456") == "значение по ключу from 1234 56** **** 3456"
    assert second_string("значение по ключу to 1234567890123456") == "значение по ключу to 1234 56** **** 3456"
    assert second_string("значение по ключу from 12345678901234567890") == "значение по ключу from **7890"
    assert second_string("значение по ключу to 12345678901234567890") == "значение по ключу to **7890"

def test_date_reformat():
    assert date_reformat("2023-10-03T12:34:56.789Z") == "03.10.2023"
    assert date_reformat("2023-01-01T00:00:00.000Z") == "01.01.2023"
    assert date_reformat("2023-12-31T23:59:59.999Z") == "31.12.2023"
    assert date_reformat("2023-10-03") == "03.10.2023"