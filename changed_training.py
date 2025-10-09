import random
from datetime import datetime


def handle_case_1():
    print('''\nЗадание № 1. Есть список чисел длинной N. Нужно отсортировать его в порядке возрастания и убывания чисел.
             Размерность задаётся при страрте пользователем, сами числа генеряться случайно.''')

    # Обработка исключений
    try:
        # Получаем значение с терминала, генерация рандомных чисел от 0 до 100, длина задается пользователем.
        numbers_list = random.sample(range(0, 100), int(input('\nВведите размерность списка в формате integer: ')))

        # Флаг, который показывает, были ли замены на последнем проходе
        swapped = True

        # Выполнение цикла до тех пор, пока есть замены. Сортировка пузырьком.
        while swapped:
            swapped = False

            # Проходим по списку, кроме последнего элемента
            for elem in range(len(numbers_list) - 1):
                # Сравниваем текущий элемент с следующим, если текущий больше, меняем их местами
                if numbers_list[elem] > numbers_list[elem + 1]:
                    temp = numbers_list[elem]
                    numbers_list[elem] = numbers_list[elem + 1]
                    numbers_list[elem + 1] = temp
                    swapped = True

        print(f'\nСортировка по возрастанию:\n{numbers_list}\n')

        rev_list = []

        for elem in numbers_list:           # Второй цикл, для реверса
            rev_list = [elem] + rev_list
        print(f'Сортировка по убыванию:\n{rev_list}')

    except ValueError:
        print("\nНеобходимо число в формате integer")


def handle_case_2():
    print('''\nЗадание № 2. На вход подаётся строка, нужно выяснить сколько букв "*" содержиться в строке (ввод какой буквы так же с консоли)''')

    # Получаем значение с терминала
    new_line = input('\nВведите строку: ')
    target_elem = input('\nВведите букву, для подсчета экземпляров: ')

    count = 0
    for elem in new_line:             # Цикл подсчета символа в строке
        if elem in target_elem:
            count += 1
    print(f'Всего символов {target_elem} = {count}')


def handle_case_3():
    print('''\nЗадание № 3. На вход подаются числа через запятую, нужно привести их к списку чисел (пример "1, 5, 8, 12, 38.6, 4, 6")
             Важно учитывать варианты "ошибочных" вводов, когда присутствуют не только числа - такие варианты отметаем.''')

    # Проверяем, является ли элемент числом, для этого убираем точку
    def is_number(element):
        return element.replace('.', '', 1).isdigit()

    # Получаем значение с терминала и фильтруем
    new_line_numbers = input('\nВведите в строку числа через запятую: ').split(',')
    # Удаляем пробелы
    values1 = [item.replace(" ", "") for item in new_line_numbers]
    # Перезаписываем список, оставляем элементы прошедшие проверку в функции
    values1 = [value for value in values1 if is_number(value)]
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

    new_string = ''         # Для хранения текущего собираемого числа
    rez_list = []           # Итоговый список чисел

    for elem in input_string:
        if elem.isdigit():                # Если символ цифра
            new_string += elem            # Добавляем цифру к текущему числу
        else:
            if new_string != '':                       # Если было собрано какое-то число
                rez_list.append(int(new_string))       # Преобразуем в число и добавляем в список
                new_string = ''                        # Начинаем собирать новое число заново

    if new_string != '':                   # Если последнее число не завершилось разделителем
        rez_list.append(int(new_string))

    # Создается пустое множество
    unique_numbers = set()
    is_unique = True

    for digit in list(rez_list):           # Цикл перебора каждого символа
        if str(digit).isdigit():           # Если есть дубли, завершение цикла и вывод False
            if digit in unique_numbers:
                is_unique = False
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