n = int(input('Enter the no. of rows:'))
m = int(input('Enter the no. of coloumns:'))
l = list()
while True:
    if n != m:
        n = int(input('Enter the no. of rows:'))
        m = int(input('Enter the no. of coloumns:'))
        if n == m:
            break
        else:
            continue
    else:
        break
for i in range(n):
    sublist = list()
    for j in range(n):
        x = int(input('Enter number: '))
        sublist.append(x)
    l.append(sublist)
print('Forward Diagonal')
fd_elements = list()
fd_sum = 0
fd_above = list()
fd_below = list()
for i in range(n):
    for j in range(n):
        if i == j:
            print(l[i][j],end='\t')
            fd_sum+=l[i][j]
            fd_elements.append(l[i][j])
        else:
            print('_',end='\t')
        if j>i:
            fd_above.append(l[i][j])
        elif j<i:
            fd_below.append(l[i][j])
print('Elements =',fd_elements)
print('Sum = ',fd_sum)
print('Elements above = ',fd_above)
print('Elements below = ',fd_below)
print('Backward Diagonal')
bd_elements = list()
bd_sum = 0
bd_above = list()
bd_below = list()
for i in range(n):
    for j in range(n):
        if (i+j) == (n-1):
            print(l[i][j],end='\t')
            bd_sum+=l[i][j]
            bd_elements.append(l[i][j])
        else:
            print('_',end='\t')
        if j>i:
            bd_above.append(l[i][j])
        elif j<i:
            bd_below.append(l[i][j])
print('Elements =',bd_elements)
print('Sum = ',bd_sum)
print('Elements above = ',bd_above)
print('Elements below = ',bd_below)
