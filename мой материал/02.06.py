2+2
print (2+2)
# todo -list и tuple
# todo - условный оператор if
# todo - операторы for и while
# todo - лаконичная запись циклов


# типа данных
x =1 #числа
world = 'hello' # строки

# Изменяемый массив
shop_list =['картошка', 'капуста', 'морковь']


from pprint import pprint
# pprint(dir(shop_list))
# pprint (dir(shop_list))
# Задача 1
# Приведем список покупок в магазине
 
shop_list = ['Картофель', 'Горошек', 'Рис', 'Хлеб']
 
# Измените список согласно пунктам задания
# Выведите результат каждого пункта на консоль по очереди
 
#   а. Вставьте рыбу между горошком и рисом
#   b. Добавьте фрукты из списка fruits в конец списка shop_list
 
fruits = ['Яблоко', 'Апельсин', 'Клубника']
 
#   c. Удалите из списка shop_list картофель
#   d. Какими по счету стоят хлеб и апельсин? Выведите номера на консоль в формате
#   Номер "продукта" в списке - N 
print ('список до:', (shop_list))
shop_list.insert(shop_list.index('Рис'), 'Рыба')
print ('список после:', (shop_list))
#shop_list.append(fruits)
#print ('добавили фрукты:', (shop_list))
shop_list.extend(fruits)
print('список через екстенд и распаковку', shop_list,len(shop_list))
#print(shop_list.pop(0)) # выкинули по индексу 0 - картошку
#print(shop_list)
print ('номер "продукта" в списке-', shop_list.index ('Хлеб'))
# формирование строк в пайтоне
# вариант 1- передавать в качестве параметров списка
# вариант 2- форматирование строки
serch ='Хлеб'
print('номер {} в списке - {}'.format(serch,shop_list.index(serch)+1))
# вариант 3 f- строки
print(f'номер {serch} в списке - {serch,shop_list.index(serch)+1}') 

# КОРТЕЖИ - неизменяемый массив
archive = (1,2,3)
archive 

# Отличия списков от кортежей
rainbow = ['red','green','blue']
colors=rainbow
colors.append('violet')
print (colors) # изменил раин боу и будет менять исходник, т.к. это СПИСОК а не кортеж

# Копирование кортежа
archive = (1,2,3)
new_archive = archive + (4,5)
print(archive,new_archive, 'добавили цифры 4 5')

# неизменяемые обьекты - int str tuple(кортежи) и тд
# изменяемые - list dict