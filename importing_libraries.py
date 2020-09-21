import imp
#connection with our library
library_1 = imp.load_source('call_function', 'C:\\Users\\User\\Desktop\\задачи\\call_function.py')
#массив котрый мы хотим обработать:
p=[1,2,3,4,5, 4, 21, 2, 3, 42, 35, 3, 45]


def list_modifie(i):
    box=[]
    for elem in i:
        box.append(elem**3+2)
    return(box)
#calling function, one method from our library
# library_1.MIN(list_modifie, p) #right code

# Function for group by: # 18 problem
def group_by_condi(m):
    odd=[]
    even=[]
    for i in m:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
            return even
# group_by_condi(p)
library_1.GroupBy(list_modifie, p)