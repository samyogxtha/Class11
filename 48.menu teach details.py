teacher = {}
while True:
    print('\n\n')
    print('Menu Driven Program')
    print('1.Add teacher')
    print('2.Display all the Teacher')
    print('3.Search for a teacher')
    print('4.Modify the details')
    print('5.Delete a teacher')
    print('0.Exit')
    print('\n\n')
    choice = int(input('Enter Choose:'))
    print('\n\n')
    if choice == 1:
        tch_id = int(input('Enter id No.: '))
        tch_name = input('Enter Name: ')
        tch_sub = input('Enter Subject: ')
        teacher[tch_id] = [tch_name,tch_sub]
        print(teacher)
    elif choice == 2:
        print('Teachers List:')
        for i in teacher:
            print(teacher[i][0])
    elif choice == 3:
        chk = input('Enter ID or Name to search: ')
        for i in teacher:
            if chk == i:
                print('Teacher Found\n',i,',',teacher[i][0])
                break
            elif chk == teacher[i][0]:
                print('Teacher Found\n',i,',',teacher[i][0])
                break
    elif choice == 4:
        mod = int(input('Enter the id no to Modify. '))
        tch_name = input('Enter Name: ')
        tch_sub = input('Enter Subject: ')
        teacher[mod] = [tch_name,tch_sub]
    elif choice == 5:
        rem = int(input('Enter the ID no. to Remove. '))
        del teacher[rem]
    elif choice == 0:
        break
