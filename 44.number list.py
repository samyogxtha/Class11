n = int(input('How many Numbers you want to add?\n'))
lis = []
for i in range(n):
    l = int(input('Enter Number:'))
    lis.append(l)
d={}
for i in lis:
    d[i] = lis.count(i)
print(d)