import csv
import os
from math import floor


class InstantiateCSVError(Exception):
    def __init__(self):
        self.message = "Файл item.csv поврежден"

    def __str__(self):
        return self.message


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.
        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        super().__init__()

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.__name}'

    def __add__(self, other):
        """
        Позволяет складывать  свои экземпляры и дочерних классов
        """
        if isinstance(other, self.__class__):
            return self.quantity + other.quantity
        return None

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.
        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = float(self.price * self.pay_rate)

    @property
    def fullname(self):
        """
        Возвращает наименование товара. К атрибуту можно обращаться без ()
        """
        return self.__name

    @fullname.setter
    def fullname(self, name):
        """
        Проверяет длину наименования товара если больше 10 символов выводит сообщение: "Длина наименования
        товара превышает 10 символов", если меньше инициализирует новое значение
        """
        if len(name) > 10:
             raise Exception('Длина наименования товара превышает 10 символов')
        else:
            self.__name = name
            return self.__name

    @classmethod
    def instantiate_from_csv(cls):
        """
        Cоздает объекты из данных файла src/items.csv, добавляет адрес ячейки памяти со значением экземпляра класса,
        возвращает заново инициализирование значения класса
        """
        try:
            with open(f'{os.path.dirname(os.path.realpath(__file__))}/items.csv', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if row['name'] and row['price'] and row['quantity']:
                        name = row['name']
                        price = float(row['price'])
                        quantity = int(row['quantity'])
                        new = Item(name, price, quantity)
                        cls.all.append(new)
                        return cls(name, price, quantity)
                    else:
                        raise InstantiateCSVError
        except FileNotFoundError:
            raise FileNotFoundError("Отсутствует файл item.csv")

    @staticmethod
    def string_to_number(meaning):
        """
        Cтатический метод, возвращающий число из числа-строки
        """
        return int(floor((float(meaning))))

