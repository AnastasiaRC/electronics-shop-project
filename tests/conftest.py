import csv
import os

import pytest
from src.item import Item
from src.keyboard import KeyBoard
from src.phone import Phone


@pytest.fixture
def test_data_item():
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


@pytest.fixture
def test_data_phone():
    phone = Phone("iPhone 14", 120_000, 5, -1.1)
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    return [phone, phone1]


@pytest.fixture
def test_data_keyboard():
    keyboard = KeyBoard('Dark Project KD87A', 9600, 2)
    keyboard1 = KeyBoard('Dark Project KD87A', 9600, 5)
    return [keyboard, keyboard1]


@pytest.fixture
def test_cls_data():
    cls_data = [Item('Смартфон', 100.0, 1), Item('Сигнализация', 1000.0, 3),
                 Item('Чип', 10.0, 5), Item('Наушники', 50.0, 0)]
    return cls_data