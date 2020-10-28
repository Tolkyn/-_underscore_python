#import imp
#connection with library
#library_1 = imp.load_source('Functions_set', 'Functions_set.py') # используй относительные пути, чтобы код был переносимым
import Functions_set as library_1 # библиотеку проще импортировать простым import

#массив котрый мы хотим обработать:
p=[1,2,3,4,5, 4, 21, 2, 3, 42, 35, 3, 45]


def list_modifie(i):
    box=[]
    for elem in i:
        box.append(elem**3+2)
    return(box)
#calling function/one method from our library
library_1.MIN(list_modifie, p) #right code
# Не очевидное поведение. По имени функции полагаю она должна искать минимальный элемент из переданных параметров. 
# Но в функцию передается массив и функция модифицирующая массив. В чем задумка?

r = library_1.list_modifier(library_1.pin)
print(r)
# получает массив и высчитывает новые значения для нового массива. не понятна цель. если можно было функции передавать не только массив, но правила модификации в виде функции
# def line(x):
#     k = 3
#     b = 4
#     return k*x + b
# list_modifier(pin, pow)

library_1.list_in_list(library_1.kim)
# ???

i = []
r = library_1.dictionary_modifier(i)
print(r)
# ??

r = library_1.each(library_1.pin, library_1.list_modifier)
print(r)
# Функция должна перебирать элементы массива и изменять их при помощи операций описаных в функции модификации
# Пример ниже:
def line(x): # функция модификации получает элемент для обработки
    k = 3
    b = 4
    return k*x + b # возвращает результат
def each(list, mutagen): # Функция each
    ret = [] # новый массив для возврата
    for i in list: # обходим каждый элемент
        ret.append(mutagen(i)) # применяем модификатор и записываем в новый массив
    return ret
# !!! Проверь и исправь все функции начиная с each, map, reduce, reduceRight, find, filter, ...
print("input: ", end='')
print(library_1.pin)
r = each(library_1.pin, line)
print("output: ", end='')
print(r)