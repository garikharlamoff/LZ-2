import math
a = (input()).split()
c =  int(input('Выберите операцию '))
s = 0
min = int(a[1])#min(a)
max = int(a[1])#max(a)
k = 0
f = 1
b = 1
for i in range(0,len(a)):
    a[i]=int(a[i])
if c == 0:
    for i in range(0,len(a)): 
        if min > a[i]:
            min = a[i]
    for i in range(0,len(a)): #a.count(max(a))=>2
         if a[i]==min:
             k +=1
    if k>=2:
        print(k)
    print(min)
elif c == 1:
    for i in range(0,len(a)):
        if max < a[i]:
            max = a[i]
    for i in range(0,len(a)):
         if a[i]==max:
             k +=1
    if k>=2:
        print(k)
    print(max)
elif c == 2:
    for i in range(0,len(a)):
        if min > a[i]:
            min = a[i]
    for i in range(0,len(a)):
        if max < a[i]:
            max = a[i]
    a[0]=min
    for i in range(1,max-min):
        a[i]=a[i-1]+max 
    for i in range(0,max-min):
        print(a[i], end=' ')
elif c == 3:
    for i in range(0,len(a)):
        if min > a[i]:
            min = a[i]
    for i in range(0,len(a)):
        if max < a[i]:
            max = a[i]
    a[0]=min
    for i in range(1,max-min):
        a[i]=a[i-1]*max 
    for i in range(0,max-min):
        print(a[i], end=' ')
else:
    for i in range(0,len(a)):
        s += a[i]
        m = s/len(a)
    print(m)
    while b<=int(m): #print(math.factorial(int(m)))
        f *= b
        b = b + 1
    if m > 0:
        print(f)
    else:
        print('0')
