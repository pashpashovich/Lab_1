print("Отображение секунд в виде дни:часы:минуты:секунды")
while True:
    try:
        seconds = int(input("Введите целое число секунд: "))
        if seconds < 0:
            print("Пожалуйста, введите неотрицательное число секунд.")
        else:
            break
    except ValueError:
        print("Неверный ввод... Повторите попытку")

days = seconds // 86400  # количество целых дней
seconds = seconds - days * 86400  # остаток секунд
hours = seconds // 3600  # количество целых часов
seconds = seconds - hours * 3600  # остаток секунд
minutes = seconds // 60  # количество целых минут
seconds = seconds - minutes * 60  # остаток секунд
print(f"Результат: {days}:{hours}:{minutes}:{seconds}")
