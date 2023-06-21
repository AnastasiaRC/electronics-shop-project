from src.keyboard import KeyBoard


def test_str_keyboard(test_data_keyboard):
    assert str(test_data_keyboard[1]) == "Dark Project KD87A"


def test_language(test_data_keyboard):
    assert str(test_data_keyboard[1].language) == "EN"


def test_change_lang(test_data_keyboard):
    test_data_keyboard[1].change_lang()
    assert str(test_data_keyboard[1].language) == "RU"
    test_data_keyboard[1].change_lang().change_lang()
    assert str(test_data_keyboard[1].language) == "RU"


def test_language_setter(test_data_keyboard):
    try:
        test_data_keyboard[0].language = 'CH'
    except AttributeError as error_text:
        print(error_text)
    assert test_data_keyboard[1].language == "EN"