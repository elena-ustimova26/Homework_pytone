import pytest
from string_utils import StringUtils


string_utils = StringUtils()

#capitalize

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


#trim

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),
    (" hello world", "hello world"),
    ("       python", "python"),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    (" hello world ", "hello world "),
    ("  ", ""),
    ("/ com", "/ com"),
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


#contains

@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "S", True),
    ("12345", "3", True),
    ("Hello World", " ", True),
])
def test_contains_positive(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "U", False),
    ("Python", " ", False),
    ("", "a", False),
])
def test_contains_negative(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


#delete_symbol

@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "Pro", "Sky"),
    ("12345", "345", "12"),
    ("Hello World", " ", "HelloWorld"),
])
def test_delete_symbol_positive(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "U", "SkyPro"),
    ("Python", " ", "Python"),
    ("SkyPro", "p", "SkyPro"),
])
def test_delete_symbol_negative(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected