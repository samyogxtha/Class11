n = int(input('How many Fruitss you want to add?\n'))
lis = []
for i in range(n):
    l = input('Enter Fruit:')
    lis.append(l)
d = {}
for i in lis:
    x=i[0]
    if x not in d:
        d[x]=[]
    d[x].append(i)
print(d)