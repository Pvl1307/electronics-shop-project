from src.item import Item, InstantiateCSVError

if __name__ == '__main__':
    # Файл items.csv отсутствует.
    try:
        Item.instantiate_from_csv()
    # FileNotFoundError: Отсутствует файл item.csv
    except FileNotFoundError as e:
        print(e)
    # В файле items.csv удалена последняя колонка.

    except InstantiateCSVError as e:
        print(e.message)
    # InstantiateCSVError: Файл item.csv поврежден
