from math import sqrt
# import imp
# import urllib3

#Final version

#each function
pin=[1,2,3,4,5, 4, 21, 2, 3, 42, 35, 3, 45]
# pin=[2,4,6,8] #list of even numbers for checking functions
kim= [[1, 2, 33, 4, 5], [5, 2, 3, 11, 4], [16, 9, 3, 1]]
tim = [{'name': 'moe', 'age': 40}, {'name': 'larry', 'age': 50}, {'name': 'curly', 'age': 60}]

def list_modifier(i):
    box=[]
    for elem in i:
        box.append(elem**3+2)
    return(box)
# list_modifier(pin) #checking the work of first function

def list_in_list(j):
    lim=j*2
    return (lim)
list_in_list(kim)
def dictionary_modifier(i):
   t = {'name': 'Tolkyn', 'age': 21}
   i.append(t)
   return (i)
#1
def each(j, c):
    for l in c(j):
        print('Printing each element of list:', l)
# each(pin, list_modifier)      #изменяет лист и потом передает его в each.

#2
def map(j, c):
    new_a=[]
    for i in c(j):
        i=sqrt(i)
        new_a.append(i)
    print('it is new arr:', new_a)  # находит квадратный корень элементов листа
# map( pin, list_modifier)

#3
def reduce(j, c):
   new = 0
   for i in c(j):
      new = new + i
   print('It is sum of our list elemets:  ', new)
# reduce(pin, list_modifier)

#4
def reduceRight(j, c):  # works with lists which consists from list:) join them into one list
    new=[]
    for i in c(j):
        for e in i:
            new.append(e)
    print(new)
# reduceRight(kim, list_in_list )

#5 FIND FUNCTION
def find(j, c):  # возвращает все элементы которые удолетвю условию
    new = []
    for i in c(j):
        if i > 10:  #условие которое надо выполнить
            new.append(i)
        else:
            continue
    print(new)
# find(pin, list_modifier)

#6 filter
def filter(j, c):  # returns first element which is corresponds conditions
    new = []
    for i in c(j):
        if i > 10:  #условие которое надо выполнить
            new.append(i)
            break
        else:
            continue
    print(new)
# filter(pin, list_modifier)
#7 where()
#8 findWhere()

#9 reject collection #
def reject(b, a):
   new = a(b)
   for i in new:
      if i % 2 == 0:
         new.remove(i)
      else:
         continue
   print('prints all items exept which satisfies condition  ', new)
# reject(pin, list_modifier)

#10 Every collection p

def EVERY(b, a):
    for i in a(b):
        if i % 2 == 0:
            new = True
        else:
            new = False
            break
    print(new)
# EVERY(pin, list_modifier)

#11 Some collection
def SOME(b, a):
   new = True
   for i in a(b):
      if i % 2 == 0:
         new = True
         break
      else:
         new = False
   print(new)
# SOME(pin, list_modifier)


#12 contains

def CONTAINS(b, a, value):
   new = True
   for i in a(b):
      if i == value:
         new = True
         break
      else:
         new = False
         continue
   print('This is the result:', new)
# Помогает искать из листа определенный элемент, если его нет выдает False
# CONTAINS(pin, list_modifier, 8)

#13 invoke collection  # сортирует элементы листа\работает только с листами в листе,
# ops это готовые функции которые можно юзать на лист в пионе
# OPS MIGHT BE =

def INVOKE(a, f, ops):
    d = []
    for k in f(a):
        k = ops(k)
        d.append(k)
    print('It is d:', d)
# INVOKE(kim, list_in_list, sorted)   #you can send somthing like sorted instead

#14 plack
#вытаскивает значения заданного ключа
def plack(modify, l, show):
   set = []
   for i in modify(l):
      set.append(i[show])
   print(set)
# plack(dictionary_modifier, tim, 'age')

#15 MAX(returns max element from list)
def MAX(m, n):
   maximum = max(m(n))
   print('maximum is:', maximum)
# MAX(list_modifier, pin)

#16 MIN(returns min element from list)
def MIN(m, n):
   minimum = min(m(n))
   print('minimum is:', minimum)
# MIN(list_modifier, pin)

#17 SortBy #переписывает данные сзади на  перед
#может обрабатывать только массивы или словари
def sort_by(m, n):
    new=[]
    for i in reversed(m(n)):
        new.append(i)
    print(new)
# sort_by(list_modifier, pin) работает с массивом\с обычным
# sort_by(dictionary_modifier, tim) работает с словарями, но печатает первоначальный вид тоже
#18 GroupBy
def GroupBy(m, n):
    for i in 2:
        items=dict(zip(i, m(n)))
    print(items)



'''#19 indexBY
def indexBy(m, n, value):
    new=[]
    for i in m(n):
        new.append(i[value])
    items=dict(zip(new, m(n)))
    print('New dictionary: ', items)
indexBy(dictionary_modifier, tim, 'age')  #done
'''