n=int(input())
l=[]
for i in range(n):
    x=int(input())
    l.append(x)
m=[]       
for i in l:
    if i not in m:
        m.append(i)
m.sort(reverse=True)        
print(l)
print('second runner up score=',m[2])
