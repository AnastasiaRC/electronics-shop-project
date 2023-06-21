from src.item import Item


class MixinLanguage:

    def __init__(self, language='EN'):
        self.__language = language

    def change_lang(self):
        """
        Возвращает объект класса с измененной раскладкой клавиатуры
        """
        if self.__language == 'EN':
            self.__language = 'RU'
            return self
        else:
            self.__language = 'EN'
            return self

    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, lang):
        """
        Проверяет Lang на совпадение в картеже (EN,RU) если совпадений нет выдает ошибку AttributeError
        если сопадения есть перезаписывает  self.language на значение lang
        """
        if not lang in ('EN', 'RU'):
            raise AttributeError(f'property {lang} of {__class__.__name__} object has no setter')
        else:
            self.__language = lang


class KeyBoard(Item, MixinLanguage):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)


