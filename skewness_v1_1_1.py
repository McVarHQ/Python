import math
x = [9,1,12,11,0,15,8,4,2,11,11,0,6,11,15,1,15,7,11,24,6,7,2,9,8]

def skewData(x):
    N = len(x)
    X = sum(x)/N
    # logic to replicate list elements
    Xn = [X]*N
    # Element-wise substraction and squaring of list
    DiffPow2 = [round((x[i]-Xn[i])**2,2) for i in range(len(x))]
    # Element-wise substraction and power three of list
    DiffPow3 = [round((x[i]-Xn[i])**3,2) for i in range(len(x))]
    S = math.sqrt(sum(DiffPow2)/(N-1))
    skewVal = (sum(DiffPow3)/N)/(S**3)
    
    return round(skewVal,2)

skew_res = skewData(x)
print(skew_res)


