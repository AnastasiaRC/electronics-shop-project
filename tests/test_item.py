from src.item import Item


def test_calculate_total_price(test_data_item):
    assert test_data_item[1].calculate_total_price() == 200000
    assert test_data_item[2].calculate_total_price() == 100000


def test_apply_discount(test_data_item):
    Item.pay_rate = 0.8
    test_data_item[1].apply_discount()
    assert test_data_item[1].price == 8000.0
    assert test_data_item[2].price == 20000


def test_getter_fullname(test_data_item):
    assert test_data_item[0].fullname == 'Смартфон'


def test_setter_fullname(test_data_item):
    assert test_data_item[0]._Item__name == 'Смартфон'
    assert test_data_item[3].fullname == 'СуперСмартфон'


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


def test_repr(test_data_item):
    assert repr(test_data_item[1]) == "Item('Смартфон', 10000, 20)"


def test_str_item(test_data_item):
    assert str(test_data_item[1]) == 'Смартфон'


def test_add(test_data_item, test_data_phone):
    assert test_data_item[1] + test_data_phone[1] == 25
    assert test_data_phone[1] + test_data_phone[1] == 10


