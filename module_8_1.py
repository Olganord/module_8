def add_everything_up(a, b):
    try:
        return a + b
    except TypeError:
        # Обработка исключений, если возникла ошибка типа
        return str(a) + str(b)

# Тот же результат без блоков try и except: (В первом случае программа выглядит красивее,
# надежность, скорее всего, одинаковая.)

# def add_everything_up(a, b):
#
#         if isinstance(a, (int, float)) and isinstance(b, (int, float)):
#             return a + b  # Складываем числа
#         else:
#             # Если типы разные (число и строка), возвращаем их строковое представление
#             if isinstance(a, (int, float)) and isinstance(b, str):
#                 return str(a) + b
#             elif isinstance(a, str) and isinstance(b, (int, float)):
#                 return a + str(b)



# Примеры использования функции
print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))

# Для вывода "130.456" можно воспользоваться форматированием результата либо округлением:

# result = add_everything_up(123.456, 7)
# formatted_result = "{:.3f}".format(result)
# print(formatted_result)
#
# print(round((add_everything_up(123.456, 7)), 3))




