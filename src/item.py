import os
import csv


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
        self.all.append(self)

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
        self.price *= self.pay_rate

    @property
    def name(self) -> str:
        """
        Геттер для получения названия товара.
        :return: Название товара.
        """
        return self.__name

    @name.setter
    def name(self, name):
        """
        Сеттер для установки нового названия товара.
        """
        if len(name) <= 10:
            self.__name = name

    @classmethod
    def instantiate_from_csv(cls):
        """Инициализирует экземпляры класса Item данными из файла src/items.csv."""
        cls.all.clear()
        file = os.path.join(os.path.dirname(__file__), 'items.csv')
        with open(file, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                name, price, quantity = row['name'], float(row['price']), int(row['quantity'])
                cls(name, price, quantity)

    @staticmethod
    def string_to_number(str_number):
        """
        Статический метод, возвращающий число из числа-строки
        """
        return int(float(str_number))
