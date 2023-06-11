"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


def test_calculate_total_price(test_data):
    assert test_data[1].calculate_total_price() == 200000
    assert test_data[2].calculate_total_price() == 100000


def test_apply_discount(test_data):
    Item.pay_rate = 0.8
    test_data[1].apply_discount()
    assert test_data[1].price == 8000.0
    assert test_data[2].price == 20000


def test_getter_fullname(test_data):
    assert test_data[0].fullname == 'Смартфон'


def test_setter_fullname(test_data):
    assert test_data[0]._Item__name == 'Смартфон'
    assert test_data[3].fullname == 'СуперСмартфон'


def test_instantiate_from_csv(test_data_reader):
    Item.instantiate_from_csv()
    item1 = Item.all[0]
    assert len(Item.all) == 5
    assert item1._Item__name == 'Смартфон'
    for row in test_data_reader:
        assert str(row['name']) == 'Смартфон' or str(row['name']) == 'СуперСмартфон'
        assert float(row['price']) == 100.0 or float(row['price']) == 10000.0
        assert int(row['quantity']) == 1 or int(row['quantity']) == 5


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_repr(test_data):
    assert repr(test_data[1]) == "Item('Смартфон', 10000, 20)"


def test_str(test_data):
    assert str(test_data[1]) == 'Смартфон'

