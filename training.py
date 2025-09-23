import random
import re
from datetime import datetime


def handle_case_1():
    print('''\nЗадание № 1. Есть список чисел длинной N. Нужно отсортировать его в порядке возрастания и убывания чисел.
             Размерность задаётся при страрте пользователем, сами числа генеряться случайно.''')

    # Обработка исключений
    try:
        # Получаем значение с терминала, генерация рандомных чисел от 0 до 100, длина задается пользователем.
        len_list = random.sample(range(0, 100), int(input('\nВведите размерность списка в формате integer: ')))

        len_list.sort()
        print(f'\nСортировка по возрастанию:\n{len_list}\n')
        len_list.reverse()
        print(f'Сортировка по убыванию:\n{len_list}')

    except ValueError:
        print("\nНеобходимо число в формате integer")


def handle_case_2():
    print('''\nЗадание № 2. На вход подаётся строка, нужно выяснить сколько букв "*" содержиться в строке (ввод какой буквы так же с консоли)''')

    # Получаем значение с терминала
    new_line = input('\nВведите строку для подсчета экземпляров символов: ').upper()

    for i in new_line:                               # Циклы перебора каждого символа и сравнение
        count = 0
        print(f'Всего символов {i}', end=' = ')
        for g in new_line:
            if i == g:
                count += 1

        print(count)


def handle_case_3():
    print('''\nЗадание № 3. На вход подаются числа через запятую, нужно привести их к списку чисел (пример "1, 5, 8, 12, 38.6, 4, 6")
             Важно учитывать варианты "ошибочных" вводов, когда присутствуют не только числа - такие варианты отметаем.''')

    # Получаем значение с терминала
    new_line_numbers = input('\nВведите в строку числа через запятую: ')

    # Фильтруем значения
    values1 = re.split(',', new_line_numbers)
    values1 = [item.replace(" ", "") for item in values1]

    values1 = [value for value in values1 if not re.sub(r'[^A-Za-z!?@#$%^&*()~/><:;"_+=\'-]', '', value)]
    print(', '.join(values1))


def handle_case_4():
    print('''\nЗадание № 4. На вход поддаётся дата с патерном "yyyy-MM-dd:hh-mm". Нужно отдельно вывести день, месяц, год, часы и минуты. пример:
             На вход 2025-09-22:14-32"
             Вывод:
             День -- 19
             Месяц -- 05
             Год -- 2025
             Час -- 14
             Минута -- 32
             Выведи месяц и день человеческим названием (май \ пятница) в скобочках. А так же, выведи время в формате AM \ PM.
             ''')


    # Массив месяцев
    monthly = ['Январь', 'Февраль', 'Март', 'Апрель', 'Мая', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']

    # Массив дней недели
    weekday = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']

    # Получаем значение с терминала
    input_date = input('''\nВведите дату в формате 'yyyy-MM-dd:hh-mm': ''').strip()

    # Через модуль datetime форматируем с помощью метода strptime
    dt = datetime.strptime(input_date, '%Y-%m-%d:%H-%M')

    print(f'\nДень -- {dt.day}\n'
          f'Месяц -- {dt.month}\n'
          f'Год -- {dt.year}\n'
          f'Час -- {dt.hour}\n'
          f'Минута -- {dt.minute}\n'
          f'({monthly[dt.month - 1]} \ {weekday[dt.weekday()]})\n'
          f'''{datetime.strftime(dt, '%H:%M')} \ {datetime.strftime(dt, '%I:%M %p')}'''
          )


def handle_case_5():
    print('''\nЗадание № 5. На вход подаётся список чисел (с любым делимером, на выбор), нужно вывести true \ false если все числа уникальны.''')


    # Получаем значение с терминала
    input_string = input('\nВведите список чисел (с любым делимером, на выбор): ')

    # Создается пустое множество
    unique_numbers = set()
    is_unique = True

    for digit in list(input_string):        # Цикл перебора каждого символа
        if digit.isdigit():                 # Если есть дубли, завершение цикла и вывод False
            if digit in unique_numbers:
                is_unique=False
                break
            else:
                unique_numbers.add(digit)

    print(is_unique)


def handle_default():
    print("\nЗадания под таким номером нет")

# Создание словаря, сопоставляющий условия с функциями
switch_case = {
    1: handle_case_1,
    2: handle_case_2,
    3: handle_case_3,
    4: handle_case_4,
    5: handle_case_5,
}

# Получение номера задачи от пользователя
condition = int(input("\nВведите номер задачи от 1 до 5: "))

# Использование словаря, для определения соответствующего действия.
action = switch_case.get(condition, handle_default)
# Выполнение действия
action()