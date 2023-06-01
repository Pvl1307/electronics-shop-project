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

def test_item_name():
    item = Item('Smartphone', 100, 1)
    assert item.name == 'Smartphone'


def test_item_setter_valid_len():
    item = Item('Smartphone', 100, 1)
    item.name = 'PC'
    assert item.name == 'PC'


def test_item_setter_invalid_len():
    item = Item('Smartphone', 100, 1)
    item.name = 'Электрогитара'
    assert item.name == 'Smartphone'


def test_item_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5


def test_item_string_to_number():
    assert Item.string_to_number('10') == 10
    assert Item.string_to_number('1241231232134') == 1241231232134
