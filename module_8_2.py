def personal_sum(numbers):
    result = 0  # Инициализация суммы
    incorrect_data = 0  # Счётчик некорректных данных
    for i in numbers:  # Здесь "i" - список внутри кортежа "numbers"
        for j in i:

            try:
                result += j
            except TypeError:  # Обработка ошибки
                incorrect_data += 1  # Увеличиваем счётчик некорректных данных
                print(f'Некорректный тип данных для подсчёта суммы - {j}')  # Сообщение об ошибке
    return result, incorrect_data  # Возвращаем сумму и количество ошибок


def calculate_average(*numbers):

    try:
        if not hasattr(numbers, '__iter__'):  # Проверка, является ли входной параметр коллекцией
            raise TypeError  # Ошибка, если нет
        total, incorrect_data = personal_sum(numbers)  # Получаем сумму и ошибки
        average = total / (len(*numbers) - incorrect_data)  # Вычисляем среднее
        return average
    except ZeroDivisionError:  # Обработка деления на ноль
        return 0
    except TypeError:  # Обработка некорректного типа данных
        print('В numbers записан некорректный тип данных')
        return None

# Примеры вызовов функции
print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # "Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать
