import pytest
from src.phone import Phone


@pytest.fixture()
def phone():
    return Phone("iPhone 4s", 10000, 1, 7)


def test_phone__str__(phone):
    assert str(phone) == "iPhone 4s"


def test_phone__repr__(phone):
    assert repr(phone) == "Phone('iPhone 4s', 10000, 1, 7)"


def test_phone_number_of_sim(phone):
    assert phone.number_of_sim == 7
    phone.number_of_sim = 53
    assert phone.number_of_sim == 53
