

''''
10.4 Покрытие тестами

Покрытие тестами осуществляется с помощью специального пакета
coverage (нужно установить)

Для старта тестирования В терминале пишу:
            coverage run coverage_example.py
   после этого для получения отчета:
             coverage report и выйдет отчет

Что бы посомтреть покрытие по веткам:
        coverage run --branch coverage_example.py
        coverage report и выйдет отчет

Stmts -> строки
Miss -> пропущено целых строчек
branch -> ветвей
BrPart -> пропущена
Cover -> покрытие тестами

Для эксперимента, можно коментить методы, функции или строки и видеть в статистике(coverage report)
как меняется цифры
'''
def longest_str(str1, str2):
    '''' Функция будет возвращать из двух строк самую большую '''
    if len(str1) > len(str2):
        return str1
    elif len(str1) == len(str2): # дописали тнетью ветку для подсчитывания веток
        return 'Чего это...'
    else:
        return str2

''''
Он не всегда пишет адекватное количесво веток  (Branch)
Сначало было 2 ветки, потом дописали-он стал видеть 4

Что бы увидеть, как в coverage меняется количество строк,
Мы дописали в функцию тертью строку:
    elif len(str1) == len(str2): # дописали тнетью ветку для подсчитывания веток
        return 'Чего это...'
А что бы в репорте был вывод 100% покрытие, мы дописали тест для третьей ветки:
     assert longest_str('BMW', 'KIA') == 'Чего это...' # дописали тест третьей ветки


'''

assert longest_str('Volvo', 'Audi') == 'Volvo'
assert longest_str('BMW', 'Audi') == 'Audi'
assert longest_str('BMW', 'KIA') == 'Чего это...' # дописали тест третьей ветки



