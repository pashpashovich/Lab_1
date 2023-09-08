import random


# функция подсчёта суммы до 1 отрицательного элемента кортежа
def sum_before_negative(cor):
    my_sum2 = 0
    for index, num in enumerate(cor):
        if num < 0:
            if index == 0:
                print("Первый элемент в кортеже отрицательный")
            break
        my_sum2 += num
    else:
        print("Нет отрицательных элементов в кортеже")
        return "Nothing"
    return my_sum2


numbers = tuple()  # объявление кортежа
while True:
    try:
        amount = int(input("Введите количество элементов в кортеже: "))
        if amount > 1:
            break
        else:
            print("Введите значение больше 1")
    except ValueError:
        print("Неверный ввод... Повторите попытку")
while True:
    choice = -1
    try:
        choice = int(input(
            "Хотите сгенерировать случайный кортеж или вводить его самостоятельно?\n1.Сгенерировать\n2.Вводить\n"))
        break
    except ValueError:
        print("Неверный ввод... Повторите попытку")
if choice == 1:
    while True:
        while True:
            try:
                start_value = int(input("Введите начало дипазона значений (целое число): "))
                break
            except ValueError:
                print("Неверный ввод... Повторите попытку")
        while True:
            try:
                finish_value = int(input("Введите конец диапазона значений (целое число): "))
                break
            except ValueError:
                print("Неверный ввод... Повторите попытку")
        if start_value < finish_value:
            break
        else:
            print("Начальное значение должно быть меньше конечного... Повторите попытку")
    numbers = tuple(random.randint(start_value, finish_value) for _ in range(amount))

elif choice == 2:
    input_numbers = []  # список для добавления элементов
    for i in range(amount):
        input_numbers.append(int(input(f"Введите элемент кортежа {i + 1}: ")))
    numbers = tuple(input_numbers)  # из списка кортеж
else:
    print("Неверный выбор( Повторите попытку")
print(f"Кортеж: {numbers}")
my_sum = sum_before_negative(numbers)  # считаем количество до первого отрицательного
if my_sum != "Nothing":
    print(f"Сумма до первого отрицательного числа: {my_sum}")
