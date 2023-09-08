import re

print("Ввести строку текста. Вывести на экран все числа, которые встречаются в строке.")
text = input("Введите строку текста: ")

numbers = re.findall(r'\d+', text)  # ищем все скопления цифр в строке с помощью регулярного выражения

if len(numbers) == 0:
    print("Нет чисел в строке")
else:
    print("Числа в строке:")
    for number in numbers:
        print(number)