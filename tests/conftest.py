import pytest
from src.item import Item


@pytest.fixture
def test_data():
    item = Item('Смартфон', 10000, 5)
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    item3 = Item('СуперСмартфон', 10000, 5)
    return [item, item1, item2, item3]


@pytest.fixture
def test_data_reader():
    reader = [{'name': 'Смартфон', 'price': '100', 'quantity': '1'},
              {'name': 'СуперСмартфон', 'price': '10000', 'quantity': '5'}]
    return reader
