from src.phone import Phone


def test_str_phone(test_data_phone):
    assert str(test_data_phone[1]) == 'iPhone 14'


def test_repr_phone(test_data_phone):
    assert repr(test_data_phone[1]) == "Phone('iPhone 14', 120000, 5, 2)"


def test_number_of_sim(test_data_phone):
    assert test_data_phone[1]._Phone__number_of_sim == 2


def test_number_of_sim_getter(test_data_phone):
    assert test_data_phone[1].number_of_sim == 2


def test_number_of_sim_setter(test_data_phone):
    try:
        test_data_phone[0].number_of_sim = 0
    except ValueError:
        print('Количество физических SIM-карт должно быть целым числом больше нуля.')
    assert test_data_phone[1].number_of_sim == 2
