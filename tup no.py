n=int(input('Enter how many no: '))
l=[]
for i in range(n):
    x=int(input('Enter no: '))
    l.append(x)
tup=tuple()
for i in l:
    if i%7==0:
        tup+=(i,)
print(tup)

chk=int(input('Enter no to chk: '))
if chk in tup:
    print('it exists',chk)
else:
    print('it does not exist')

print('min= ',min(tup))
print('max= ',max(tup))