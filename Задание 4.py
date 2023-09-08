def merge_dicts(dict1, dict2):  # функция слияния двух словарей в один
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

dict_list = []
my_set = set()
for i in range(1, kol + 1):
    dict_i = dict()  # создаем новый словарь для каждого ввода
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
        dict_i[key] = value  # Добавляем пару ключ-значение в текущий словарь
    dict_list.append(dict_i)  # Добавляем текущий словарь в список

# Слияние всех словарей из списка в один
merged_dict = dict()
for d in dict_list:
    merged_dict = merge_dicts(merged_dict, d)

print("Результирующий словарь после слияния:")
print(merged_dict)