print('    Функция ZIP в Python')
'''
Здесь я изучаю ZIP

Функция zip() в Python создает итератор, который соединяет элементы из двух и более список. 
Полученный итератор можно использовать для быстрого и согласованного 
решения общих задач программирования, таких как создание словарей.

Операции с zip работают так же, как обычная молния на сумке или паре джинсов. 
Блокирующие пары зубцов по обеим сторонам молнии стягиваются вместе, 
чтобы закрыть отверстие. 
Фактически, эта визуальная аналогия идеально подходит для понимания zip(), 
так как функция была названа в честь физических застежек-молний!

Функция принимает итераторы (то есть последовательности) в качестве аргументов 
и возвращает то же итератор. Этот итератор генерирует серию кортежей, 
содержащих элементы из каждой итерации. 
zip() может принимать любые типы итераций, такие как файлы, списки, кортежи, словари, множества и т. д.

Мат.-> https://webdevblog.ru/ispolzovanie-funkcii-python-zip-dlya-parallelnoj-obrabotki/#:~:text=%D0%A4%D1%83%D0%BD%D0%BA%D1%86%D0%B8%D1%8F%20zip()%20%D0%B2%20Python,%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F%2C%20%D1%82%D0%B0%D0%BA%D0%B8%D1%85%20%D0%BA%D0%B0%D0%BA%20%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5%20%D1%81%D0%BB%D0%BE%D0%B2%D0%B0%D1%80%D0%B5%D0%B9.

'''





numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
zipped = zip(numbers, letters)
'''
Здесь используется zip(numbers, letters) для создания итератора, 
который создает кортежи в форме (x, y)
'''

print('Наверно это ячейка, где хранится:\n',zipped)
print('Распеч тип этого итерируемого объекта:\n',type(zipped))

'''
Чтобы получить окончательный объект списка, 
вам нужно использовать list() для использования итератора.
'''
print('Что бы распечететь сам объект, нужно дописать list:\n',list(zipped))
print('Bынос:', type(list(zipped)))



'''
ZIP & SET
Если вы работаете с последовательностями, такими как списки, кортежи или строки, 
то ваши итерации гарантированно будут оцениваться слева направо. 
Это означает, что результирующий список кортежей будет иметь вид 
[(numbers[0], letters[0]), (numbers[1], letters[1]),…, (numbers[n], letters[n])]. 

Однако для других типов итераций (например, SET(множество)) вы можете увидеть странные результаты:

В этом примере s1 и s2 являются установленными объектами, которые не хранят свои 
элементы в каком-либо определенном порядке. 
Это означает, что кортежи, возвращаемые функцией zip(), 
будут иметь элементы, которые спарены случайным образом.
'''
s1 = {2, 3, 1}
s2 = {'b', 'a', 'c'}
print(list(zip(s1, s2))) # и результат будет постоянно разный !!!



'''    Использование без аргументов    '''

'''
Здесь вызывается zip() без аргументов, поэтому в переменной zipped содержится пустой итератор. 
Если вы используете итератор с list(), то вы также увидите пустой список.
'''

print('    -Использование без аргументов-    ')

zipped = zip()
print('ячейка, где хранится:',zipped)
print('тип объекта:',type(zipped))
print('Сам объект:',list(zipped))


'''
можете попытаться заставить пустой итератор напрямую выдавать элемент. 
В этом случае вы получите исключение StopIteration:'''
zipped = zip()
#next(zipped) # закоментил, что бы не мешла выводимая ошибка



'''    -Передача одного аргумента-    '''
print('    -Передача одного аргумента-    ')
a = [1, 2, 3]
zipped = zip(a)
print('Передача одного аргумента:',list(zipped))



'''
Длина получаемых кортежей всегда будет равна числу итераций, 
которые вы передаете в качестве аргументов. Вот пример с тремя итерациями:
'''
integers = [1, 2, 3]
letters = ['a', 'b', 'c']
floats = [4.0, 5.0, 6.0]
zipped_3 = zip(integers, letters, floats)
print('ZIP с ТРЕМЯ аргументами:',list(zipped_3))



print()
''''    -Передавая аргументы неравной длины-    '''
print('    -Передавая аргументы неравной длины-    ')

'''
Возможно, что итерации, которые вы передаете в качестве аргументов, не имеют одинаковую длину.
В этих случаях количество элементов, которые выдает zip(), будет равно длине самой короткой итерации.
 Остальные элементы в любых более длинных итерациях будут полностью игнорироваться zip()
 '''
print('ZIP с аргументами разной длины:\n',list(zip(range(5), range(100))))

'''
Из второго объекта range() все еще есть 95 непревзойденных элементов. 
Все они игнорируются zip(), так как больше нет элементов из первого объекта range() для завершения пар.


'''
from itertools import zip_longest
numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
longest = range(5)
zipped_itertools = zip_longest(numbers, letters, longest, fillvalue='?')

'''
Здесь используется itertools.zip_longest(), 
чтобы получить пять кортежей с элементами из numbers, letters и longest. 
Итерация останавливается только тогда, когда самый длинный список longest будет израсходован. 
Недостающие элементы из numbers и letters заполнены знаком вопроса ?, 
который был указали с помощью fillvalue.
'''

print('ZIP с функцией itertools:\n',list(zipped_itertools))

boom = range(10, 60, 10)
print('a=',a)
print('integers=', integers)
print('floats=', floats)
print('boom=', boom)
my_zipped_itertools = zip_longest(a, floats, integers, boom, fillvalue='?')
''' 
Не забудь, что нужно писать и 
zip_longest и fillvalue='?'
'''

print('Чисто мой эксперимент, звездочки и & не принимает :\n', list(my_zipped_itertools))



print()
''''    -Параллельное прохождение списков-    '''
print('    -Параллельное прохождение списков-    ')

'''
Функция zip() позволяет выполнять параллельные итерации по двум и более последовательностям. 
Поскольку zip() генерирует кортежи, вы можете распаковать их в заголовке цикла for:
'''
letters = ['a', 'b', 'c']
numbers = [0, 1, 2]
for l, n in zip(letters, numbers):
    print(f'Letter: {l}')
    print(f'Number: {n}')
    print('попробую в строку:',f'Letter: {l}',f'Number: {n}')


'''
также можете выполнить более двух итераций в одном цикле for.
Нет ограничений на количество итераций, которые можно использовать с функцией zip().
'''
print('-более двух итераций в одном цикле for.-')
operators = ['*', '/', '+']
for l, n, o in zip(letters, numbers, operators):
    print(f'Letter: {l}')
    print(f'Number: {n}')
    print(f'Operator: {o}')
    print(f'Letter:{l}', f'Number:{n}', f'Operator:{o}')



print()
''''    -Параллельная обработка словарей-    '''
print('    -Параллельная обработка словарей-    ')

'''
Здесь параллельно перебирается dict_one и dict_two. 
В этом случае zip() генерирует кортежи с элементами из обоих словарей. 
Затем вы можете распаковать каждый кортеж и получить доступ к элементам обоих словарей одновременно.
'''


dict_one = {'name': 'John', 'last_name': 'Doe', 'job': 'Python Consultant'}
dict_two = {'name': 'Jane', 'last_name': 'Doe', 'job': 'Community Manager'}
for (k1, v1), (k2, v2) in zip(dict_one.items(), dict_two.items()):
    print(k1, '->', v1)
    print(k2, '->', v2)





print()
''''    -Распаковка последовательности-    '''
print('    -Распаковка последовательности-    ')

''' 
противоположностью zip() является …, zip(). 
Вы помните, что функция zip() работает так же, как настоящая молния? 
Пока приведенные примеры показали, как Python закрывает молнию. 
Итак, как распаковывать объекты Python?

Допустим, у вас есть список кортежей и вы хотите разделить элементы каждого 
кортежа на независимые последовательности. 
Для этого вы можете использовать zip() вместе с оператором распаковки *, например так:
'''

pairs = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
numbers, letters = zip(*pairs)
print('распаковка numbers', numbers)
print('распаковка letters', letters)



print()
''''    -Параллельная сортировка-    '''
print('    -Параллельная сортировка-    ')

'''
Для этого вы можете использовать zip() вместе с .sort() следующим образом:
'''
letters = ['b', 'a', 'd', 'c']
numbers = [2, 4, 3, 1]
data1 = list(zip(letters, numbers))
print('здесь letters+numbers:\n',data1)
data1.sort()
print('здесь letters+numbers+SORT:\n',data1)


data2 = list(zip(numbers, letters))
print('numb+letters', data2)
data2.sort()
print('numb+letters+SORT',data2)
'''
сначала объединяются два списка с помощью zip() 
и затем сортируются. 
Обратите внимание, 
как data1 сортируются по letters, 
а data2 — по numbers


Вы также можете использовать sorted() и zip() 
вместе для достижения аналогичного результата:
'''
letters = ['b', 'a', 'd', 'c']
numbers = [2, 4, 3, 1]
data = sorted(zip(letters, numbers))
print('ZIP & SORTED одновременно:', data)
'''
В этом случае sorted() проходит через итератор, сгенерированный zip (), 
и сортирует элементы по letters, и все за один раз. 
Этот подход может быть немного быстрее, 
так как нам понадобятся только два вызова функций: zip() и sorted()
'''


print()
''''    -Вычисления в парах-    '''
print('    -Вычисления в парах-    ')
'''
Вы можете использовать функцию zip() для быстрых вычислений.
zip() может предоставить быстрый способ сделать эти вычисления:

Здесь рассчитывается прибыль за каждый месяц, 
вычитая costs из sales. 
Функция zip() объединяет правильные пары данных для выполнения расчетов.

'''


total_sales = [52000.00, 51000.00, 48000.00]
prod_cost = [46800.00, 45900.00, 43200.00]
for sales, costs in zip(total_sales, prod_cost):
    profit = sales - costs
    print(f'Total profit: {profit}')



print()
''''    -Создание словарей-    '''
print('    -Создание словарей-    ')

'''
Иногда вам может потребоваться создать словарь из двух разных, 
но тесно связанных последовательностей. 
Удобный способ добиться этого — использовать dict() и zip() вместе. 
Например, предположим, что вы извлекли данные из формы или базы данных. 
Теперь у вас есть следующие списки данных:
'''
fields = ['name', 'last_name', 'age', 'job']
values = ['John', 'Doe', '45', 'Python Developer']

'''
В этом случае можно использовать dict() вместе с zip() следующим образом:
'''

a_dict = dict(zip(fields, values))
print('Наш получившийся dict', a_dict)

''''
zip(fields, values) возвращает итератор, который генерирует кортежи из 2 элементов. 
Если вы вызовете dict() для этого итератора, то таким образом создается нужный словарь. 
Элементы полей становятся ключами словаря, а элементы значений представляют значения в словаре.

Вы также можете обновить существующий словарь, 
комбинируя zip() с dict.update(). 
Предположим, что Джон меняет свою работу, и вам нужно обновить словарь. 
Вы можете сделать что-то вроде следующего:
'''

new_job = ['Python Consultant']
field = ['job']
a_dict.update(zip(field, new_job))
print(a_dict)
