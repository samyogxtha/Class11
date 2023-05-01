n = int(input('Enter the no of rows'))
m = int(input('Enter the no of coloum'))




l=[]
for i in range(m):
    sub=[]
    for j in range(m):
        n=int(input('Enter Number: '))
        sub.append(n)
    l.append(sub)

for i in range(m):
    for j in range(m):
        if i==j:
            print(l[i][j],end='\t')
        else:
            print('_',end='\t')
    print('\n')