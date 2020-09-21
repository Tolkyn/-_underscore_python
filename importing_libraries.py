import imp
#connection with library
library_1 = imp.load_source('Functions_set', 'C:\\Users\\User\\Desktop\\задачи\\Functions_set.py')
#массив котрый мы хотим обработать:
p=[1,2,3,4,5, 4, 21, 2, 3, 42, 35, 3, 45]


def list_modifie(i):
    box=[]
    for elem in i:
        box.append(elem**3+2)
    return(box)
#calling function/one method from our library
library_1.MIN(list_modifie, p) #right code
