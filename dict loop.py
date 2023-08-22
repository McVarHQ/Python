d={'add':0, 'sub':0, 'mul':1, 'div':1}

l=[]
for i in range(5):
    try:
        x=int(input())
        l+=[x]
    except:
        break
       
if len(l)<2:
    print('Insufficient Data')
    
n=l[0]
d['add']=n
d['sub']=n
d['mul']=n
d['div']=n
for i in range(1, len(l)):
    d['add']+=l[i]
    d['sub']-=l[i]
    d['mul']*=l[i]
    d['div']/=l[i]
    d['div']=round(d['div'], 2)

print(d)
