try:
    a = int(input('Введите первое число: '))
    b = int(input('Введите второе число: '))
    result = a / b
except ZeroDivisionError:
    print("Ошибка: Деление на ноль!")
except ValueError:
    print("Ошибка: введено не число!")
else:
    print(f"Результат: {result}")
finally:
    print("Файл закрыт.")
