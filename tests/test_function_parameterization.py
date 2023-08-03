"""
Test Function Parameterization.
"""
import pytest
from src.examples import (
    addition,
    subtraction,
    reverse_string,
    capitalize_string,
    clean_string,
)


# Test Math Functions
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, 3),
        (5, -1, 4),
    ],
)
def test_addition(a, b, expected):
    assert addition(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, -1),
        (5, -1, 6),
    ],
)
def test_subtraction(a, b, expected):
    assert subtraction(a, b) == expected


# Test String Functions
@pytest.mark.parametrize(
    "string, expected",
    [
        ("hello", "olleh"),
        ("world", "dlrow"),
    ],
)
def test_reverse_string(string, expected):
    assert reverse_string(string) == expected


@pytest.mark.parametrize(
    "string, expected",
    [
        ("hello", "HELLO"),
        ("world", "WORLD"),
    ],
)
def test_capitalize_string(string, expected):
    assert capitalize_string(string) == expected


@pytest.mark.parametrize(
    "string, expected",
    [
        (" hello ", "hello"),
        (" WoRlD ", "world"),
    ],
)
def test_clean_string(string, expected):
    assert clean_string(string) == expected


# Simple test to demo how to mark a pytest parameter test
@pytest.mark.parametrize(
    "string, expected",
    [
        (" hello ", "hello"),
        (" WoRlD ", "world"),
        pytest.param(None, 42, marks=pytest.mark.xfail(reason="some bug")),
    ],
)
def test_clean_string_marked(string, expected):
    assert clean_string(string) == expected


# Parameterized testing with 2 arguments and ranges
@pytest.mark.parametrize("a", range(5))
@pytest.mark.parametrize("b", range(10))
def test_addition_2_args(a, b):
    assert addition(a, b) == a + b


# Using Pytest generate tests to create tests
def pytest_generate_tests(metafunc):
    if 'x' in metafunc.fixturenames and 'y' in metafunc.fixturenames:
        metafunc.parametrize('x', [1, 2, 3])
        metafunc.parametrize('y', [5, 6, 7])

def test_addition_generate_tests(x, y):
    assert addition(x, y) == x + y