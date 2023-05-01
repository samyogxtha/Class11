std_details={}
while True:
    print('\n\n\tMENU')
    print('1. Input student Details')
    print('2. Display all Students')
    print('3. Search')
    print('4. Modify')
    print('5. Remove Student')
    print('6. Exit')
    br = int(input('Enter Choose:'))
    print('\n\n')
    if br == 1:
        std_roll = int(input('Enter Roll No.: '))
        std_name = input('Enter Name: ')
        std_grade = int(input('Enter Grade: '))
        std_division = input('Enter Division: ')
        std_details[std_roll] = [std_name,std_grade,std_division]
        print(std_details)
    elif br == 2:
        print('Student List:')
        for i in std_details.keys():
            print(std_details[i][0])
    elif br == 3:
        chk = int(input('Enter Roll no to search: '))
        if chk in std_details:
            print('Student Found\n',std_details[chk][0])
        else:
            print('Student not found.')
    elif br == 4:
        mod = int(input('Enter the Roll no to Modify. '))
        std_name = input('Enter Name: ')
        std_grade = int(input('Enter Grade: '))
        std_division = input('Enter Division: ')
        std_details[mod] = [std_name,std_grade,std_division]
    elif br == 5:
        rem = int(input('Enter the Roll no to Remove. '))
        del std_details[rem]
    elif br == 6:
        break
