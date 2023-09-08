jewelry_store = {
    "Кольцо": ["золото", 100, 5],
    "Браслет": ["серебро", 60, 15],
    "Серьги": ["платина", 40, 14],
    "Ожерелье": ["жемчуг", 200, 13],
    "Часы": ["сталь", 100, 20]
}


def show_description():
    print("Описание изделий:")
    for item, description in jewelry_store.items():
        print(f"{item} - {description[0]}")


def show_price():
    print("Цены на изделия:")
    for item, description in jewelry_store.items():
        print(f"{item} - {description[1]} бел. рублей")


def show_quantity():
    print("Количество изделий в магазине:")
    for item, description in jewelry_store.items():
        print(f"{item} - {description[2]}")


def show_all_info():
    print("Информация о всех изделиях:")
    for item, description in jewelry_store.items():
        print(f"{item} – {description[0]}, Цена: {description[1]} бел. рублей, Количество: {description[2]}")


def purchase():
    total_price = 0
    while True:
        item = input(
            "Введите название изделия (или 'n' для завершения покупок): ").capitalize()
        # делает первый символ заглавным, а остальные маленькими
        if item == 'N':
            break
        if item not in jewelry_store:
            print("Такого изделия нет в магазине. Попробуйте еще раз.")
            continue
        try:
            quantity = int(input(f"Введите количество для покупки ({item}): "))
            if quantity < 0:
                print("Количество не может быть отрицательным.")
                continue
            elif quantity > jewelry_store[item][2]:
                print("В магазине нет столько изделий.")
                continue
        except ValueError:
            print("Неверный ввод. Попробуйте еще раз.")
            continue
        price_per_item = jewelry_store[item][1]
        total_price += price_per_item * quantity
        jewelry_store[item][2] -= quantity
        print(f"Вы купили {quantity} шт. {item} за {price_per_item * quantity} руб.")
    print(f"Общая стоимость покупок: {total_price} руб.")
    print("Обновленное количество изделий в магазине:")
    show_quantity()


def main():
    while True:
        print("Выберите действие:")
        print("1. Просмотр описания")
        print("2. Просмотр цен")
        print("3. Просмотр количества")
        print("4. Получить всю информацию")
        print("5. Покупка")
        print("6. До свидания")

        choice = input("Выбор: ")

        if choice == '1':
            show_description()
        elif choice == '2':
            show_price()
        elif choice == '3':
            show_quantity()
        elif choice == '4':
            show_all_info()
        elif choice == '5':
            purchase()
        elif choice == '6':
            print("До свидания!")
            break
        else:
            print("Неверный выбор. Повторите попытку")


if __name__ == "__main__":
    main()
