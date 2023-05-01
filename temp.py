x=int(input('how many numbers do you want to input: '))
l=[]
for i in range(x):
    n = int(input('Enter Number: '))
    l.append(n)
tup = ()
for i in l:
    if i % 7 == 0:
        tup += (i,)
print(tup)
print('Min val = ',min(tup))
print('Max val = ',max(tup))
chk = int(input('Enter no to check if it exists: '))
if chk in tup:
    print(chk,'Exists')
    print('Count = ',tup.count(chk))
else:
    print(chk,'Does not Exist')







    