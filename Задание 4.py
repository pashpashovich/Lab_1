import random

def merge_dicts(dict1, dict2):
    result = dict1.copy()
    result.update(dict2)
    return result

while True:
    try:
        kol = int(input("Введите количество словарей для добавления: "))
        if kol > 1:
            break
        else:
            print("Введите значение, больше 1")
    except ValueError:
        print("Неверный ввод...Повторите попытку")

while True:
    try:
        choice = int(input(
            "Хотите вводить все значения в словарь вручную или сгенерировать рандомные значения чисел?\n1. Вручную\n2. Сгенерировать\n"))
        if choice == 1 or choice == 2:
            break
        else:
            print("Вы ввели неверное значение... Повторите попытку")
    except ValueError:
        print("Неверный ввод... Повторите попытку")

dict_list = []
my_set = set()

if choice == 1:
    for i in range(1, kol + 1):
        dict_i = dict()
        while True:
            try:
                k = int(input(f"Введите количество значений в словаре {i}: "))
                if k > 1:
                    break
                else:
                    print("Введите значение, больше 1")
            except ValueError:
                print("Неверный ввод...Повторите попытку")
        for c in range(1, k + 1):
            while True:
                key = input(f"Ключ {c}: ")
                if key in my_set:
                    print("Такой ключ уже существует... Повторите попытку")
                else:
                    break
            my_set.add(key)
            value = input(f"Значение {c}: ")
            dict_i[key] = value
        dict_list.append(dict_i)
else:
    for i in range(1, kol + 1):
        dict_i = dict()
        while True:
            try:
                k = int(input(f"Введите количество значений в словаре {i}: "))
                if k > 1:
                    break
                else:
                    print("Введите значение, больше 1")
            except ValueError:
                print("Неверный ввод...Повторите попытку")
        while True:
            try:
                start_value = int(input("Введите начало диапазона значений (целое число): "))
                finish_value = int(input("Введите конец диапазона значений (целое число): "))
            except ValueError:
                print("Неверный ввод... Повторите попытку")
            if start_value < finish_value:
                break
            else:
                print("Начальное значение должно быть меньше конечного... Повторите попытку")
        for c in range(1, k + 1):
            key = random.randint(start_value, finish_value)
            if key not in my_set:
                my_set.add(key)
                value = random.randint(start_value, finish_value)
                dict_i[key] = value
        dict_list.append(dict_i)

# Сливаем несколько словарей в один
merged_dict = dict()
for d in dict_list:
    merged_dict = merge_dicts(merged_dict, d)

print("Результирующий словарь после слияния:")
print(merged_dict)
