l=[]
for i in range(3):
    sub=[]
    for j in range(3):
        n=int(input('Enter Number: '))
        sub.append(n)
    l.append(sub)

print(l)

for i in range(3):
    for j in range(3):
        print(l[i][j],end='\t')
    print('\n')
    