s=[1,2,3,4,5,5,6,5767,86,676,676,78,88,9767]
def mod(i):
    sss=[]
    for j in i:
        sss.append(j+4)
    return (sss)

def sort_by (a, b):
    k=[]
    k.append(a(b))
    for i in k:
        i.sort()
    print(k)
    # print((a(b)).sort())
sort_by(mod, s)
#sorts lists in lists
