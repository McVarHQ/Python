
def triangle(n):
    l=[]
    if n<=0:
        print()
    else:
        a=11**(x-n)
        for i in str(a):
            l+=[int(i)]
        print(l)
        triangle(n-1)

x=int(input('Enter no of rows- '))
triangle(x)

        
        
            
