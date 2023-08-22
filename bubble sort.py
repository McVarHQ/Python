def bubble_sort(l):
    length=len(l)
    for i in range(length):
        for j in range(length-1-i):
            if l[j]<l[j+1]:
                l[j], l[j+1]=l[j+1], l[j]
    return l

print(bubble_sort([1,2,3,4,5,3.2]))
