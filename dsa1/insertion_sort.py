def insert_sort(a):
    for i in range(1,len(a)):
        j=i-1
        temp=a[i]
        while j>=0 and a[j] > temp:
            #so i shift 
            a[j+1]= a[j]
            j=j-1
        a[j+1]=temp


import random
a=[random.randint(0,1000) for x in range(1000)]

b=a.copy()
insert_sort(b)

print(b == sorted(a))
