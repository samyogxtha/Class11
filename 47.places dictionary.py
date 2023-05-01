d = {}
n = int(input('How many places you wish to add?'))
for i in range(1,n+1):
    a = input('Enter Place Name: ')
    d[i]=a
for i in d:
    if len (d[i]) > 6:
        if ' ' in d[i]:
            print(d[i])