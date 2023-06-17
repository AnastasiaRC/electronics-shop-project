from src.item import Item


class Phone(Item):

    def __init__(self,name: str, price: float, quantity: int, number_of_sim):
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __repr__(self):
        return super().__repr__()[:-1] + f", { self.__number_of_sim})"

    @property
    def number_of_sim(self):
        """
        Возвращает кол-во сим-карт. К атрибуту можно обращаться без ()
        """
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, num):
        """
        Проверяет являеться ли объект больше 0 и целым числом. В случае невыполнения одного из условий
        выдает ошибку: ValueError('Количество физических SIM-карт должно быть целым числом больше нуля')
        """
        if not isinstance(num, int) and num <= 0:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля')
        self.__number_of_sim = num


