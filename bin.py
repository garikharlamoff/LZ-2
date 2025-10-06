a = int (input())
b = 0
c = 1
r = 0
while b < 100:
    a = a + r
    c = c * 1.001
    r = round(c)
    'print(r)'
    print (bin ( a ) [2:])