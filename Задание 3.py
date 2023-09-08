myList = ['Python', 15442, 32, 'QweRty', 34, 19, 'love']
print("Дан список list=['Python',15442,32,’QweRty’,34,19,'love’]. В словах посчитать количество гласных и согласных")


def is_vowel(char):  # проверяем,гласная ли данный символ
    vowels = 'aeiouyAEIOUY'
    return char in vowels


# итерация по элементам списка и подсчет гласных и согласных в строках
for item in myList:
    if isinstance(item, str):  # проверяем, является ли элемент строкой
        vowels_count = 0
        # считаем количество гласных
        for letter in item:
            if is_vowel(letter):
                vowels_count += 1
        consonants_count = len(item) - vowels_count  # остальные буквы - согласные
        print(f"Для строки '{item}': Гласных - {vowels_count}, Согласных - {consonants_count}")
    else:
        print(f"Для элемента {item} типа {type(item)} подсчет невозможен.")
