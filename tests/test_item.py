import pytest
from src.item import Item

@pytest.fixture
def item():
    return Item("Смартфон", 10000, 20)


def test_item_calculate_total_price(item):
    assert item.calculate_total_price() == 200000


def test_item_apply_discount(item):
    Item.pay_rate = 0.8
    item.apply_discount()
    assert item.price == 8000.0

