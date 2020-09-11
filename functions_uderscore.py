list_1=[3, 4, 21, 2, 3, 42, 35, 3, 45]
list_2= [[1, 2, 3, 4, 5], [5, 2, 3, 1, 4], [6, 9, 3, 1]]
dict = {1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'}

#modifier for lists
def modify_lists(i):
   l = i**3 + (2+i)
   print(l)
   return(l)

#modifier for dictionaries
def modify_dict(i):
   emp=[]
   d={'name':'Tolkyn', 'age':21, 'status':'stuff'}
   emp.append(d)
   for j in i:
      emp.append(j)
      print(emp)
      return (emp)
#1 EACH FUNCTION

def each(j, c):
   for i in j:
      c(i)  # c is function
      print('It is K: ', с(i))
# each(modify_lists, list_1 )

#2 MAP FUNCTION

def map(j, c):
   new_a = []
   for i in j:
      c(i)  # c is function
      new_a.append(c(i))
   print('It is new arr: ', new_a)
# map(modify_lists, list_1 )

#3 REDUCE FUNCTION

def reduce(j, c):
   new = 0
   for i in j:
      c(i)  # c is function
      new = new + c(i)
   print('It is sum of:  ', new)
# map(modify_lists, list_1 )

#4 REDUCE RIGHT FUNCTION
def reduce(j, c):
   new = 0
   for i in reversed(j):
      new = new + c(i)
      print(new)
# reduce(modify_lists, list_1 )

#5 FIND FUNCTION
def find(j, c):
   new = []
   for i in j:
      c(i)
      if c(i) > 10:
         new.append(i)
         print(new)
      else:
         continue
# find(modify_lists, list_1)

#6 FILTER FUNCTION
def find(j, c):
   new = []
   pred = True
   for i in j:
      c(i)
      if c(i) < 8:
         new.append(c(i))
         print(new)
      else:
         continue
# find(modify_lists, list_1)

# WHERE_FUNCTON  (не работает)

def WHERE(q, w):
   print(q(w))
   for k in q(w):
      if k == {1: 'something'}:
         print('bingo')
      else:
         print(k)
         print('ops')

WHERE(modify_lists, list_1 )

# FIND_WHERE
# just function with BREAK, it is

def FIND_WHERE(q, w):
   print(q(w))
   for k in q(w):
      if k == 1:
         print(k)
         break
      else:
         print('no one')


# FIND_WHERE(modify_lists, list_1 )

# REJECT()
____________________________
l = [3, 4, 5, 6, 7, 7, 8, 8, 9, 9, 0, 12]


def modify(i):
   set = []
   for element in i:
      element = element + 3
      set.append(element)
   return (set)


def reject(a, b):
   new = a(b)
   print(new)
   for i in new:
      if i % 2 == 0:
         new.remove(i)
      else:
         continue
   print(new)


reject(modify, l)
__________________________
# every
__________________________
l = [3, 4, 5, 6, 7, 7, 8, 8, 9, 9, 0, 12]


def modify(i):
   set = []
   for element in i:
      element = element + 3
      set.append(element)
   return (set)


def EVERY(a, b):
   new = True
   while new is True:
      for i in a(b):
         if i % 2 == 0:
            new = True
         else:
            new = False
   print(new)


EVERY(modify, l)
__________________________
# some
__________________________
l = [3, 4, 5, 6, 7, 7, 8, 8, 9, 9, 0, 12]


def modify(i):
   set = []
   for element in i:
      element = element + 3
      set.append(element)
   return (set)


def SOME(a, b):
   new = True
   for i in a(b):
      if i % 2 == 0:
         new = True
         break
      else:
         new = False
   print(new)


SOME(modify, l)
__________________________
# Contains
__________________________

l = [3, 4, 5, 6, 7, 7, 8, 8, 9, 9, 0, 12]

value = input("What do u want to find ?")


def modify(i):
   set = []
   for element in i:
      element = element + 3
      set.append(element)
   print(set)
   return (set)


def CONTAINS(a, b, value):
   new = True
   for i in a(b):
      if i == value:
         new = True
         break
      else:
         new = False
         continue
   print('This is the result:', new)


CONTAINS(modify, l, value)
______________________________________
# invoke
--------------------------------------
l = [[3, 9, 5, 6, 7, 3, 8], [8, 9, 9, 0, 12], [8, 9, 10, 2, 5, 1]]


def modify(var):
   c = []
   b = []
   for i in var:
      for j in i:
         j = j + 8
         c.append(j)
      b.append(c)
   print('It is B:', b)
   return (b)


def INVOKE(f, a):
   new = f(a)
   d = []
   for k in new:
      k = k.sort()
      d.append(k)

   print('It is d:', k)


INVOKE(modify, l)
______________________________________________________
# plack
______________________________________________________
s = [{'name': 'moe', 'age': 40}, {'name': 'larry', 'age': 50}, {'name': 'curly', 'age': 60}]


def modify(i):
   t = {'name': 'Tolkyn', 'age': 21}
   i.append(t)
   print(i)
   return (i)


# show=input('what do u want to see?')
def pack(modify, l):
   set = []
   for i in modify(l):
      set.append(i['name'])
   print(set)


pack(modify, s)
____________________________________________________
# max
____________________________________________________
s = [{'name': 'moe', 'age': 40}, {'name': 'larry', 'age': 50}, {'name': 'curly', 'age': 60}]


def modify(i):
   t = {'name': 'Tolkyn', 'age': 21}
   i.append(t)
   print(i)
   return (i)


# show=input('what do u want to see?')
def MAX(modify, l):
   set = []
   for i in modify(l):
      set.append(i['age'])
   maximum = max(set)
   print(set, 'max of set:', maximum)


MAX(modify, s)
_______________right
version
of
MAX____________

ss = [{'name': 'moe', 'age': 40}, {'name': 'larry', 'age': 50}, {'name': 'curly', 'age': 60}]
s = [1, 2, 3, 4, 5, 5, 6, 5767, 86, 676, 676, 78, 88, 9767]


def modify(s):
   sq = []
   for i in s:
      i = i + 7
      sq.append(i)
   print(sq)
   return (sq)


def MAX(m, n):
   maximum = min(m(n))
   print('maximum is:', maximum)


MAX(modify, s)
_____________________________________________
# min for array of numbers:
ss = [{'name': 'moe', 'age': 40}, {'name': 'larry', 'age': 50}, {'name': 'curly', 'age': 60}]
s = [1, 2, 3, 4, 5, 5, 6, 5767, 86, 676, 676, 78, 88, 9767]


def modify(s):
   sq = []
   for i in s:
      i = i + 7
      sq.append(i)
   print(sq)
   return (sq)


def MIN(m, n):
   mininm = min(m(n))
   print('minimum is:', mininm)


MIN(modify, s)



