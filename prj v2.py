student_ID_list = list()
student_A = 0
student_B = 0
student_C = 0
student_D = 0
student_E = 0

student_A_ = list()
student_B_ = list()
student_C_ = list()
student_D_ = list()
student_E_ = list()

staff_ID_list = list()
staff_A = 0
staff_B = 0
staff_C = 0
staff_D = 0
staff_E = 0

staff_A_ = list()
staff_B_ = list()
staff_C_ = list()
staff_D_ = list()
staff_E_ = list()

print('BELL TIMING PROPOSAL')
print('We would like to allow students and staff to show their preference on the start and finish time of the school days.')

while True:
    position = input('Are you a Student? (y/n)')
    if position == 'Y' or position == 'y':
        while True:
            id = input('Please Enter your Unique ID Number :')
            if id in student_ID_list:
                print('ID has been used already. Please Try Ag')
                continue
            else:
                student_ID_list.append(id)
                break
        
        print('Options:')
        print('Option A | Start: 08:00 - Finish: 15:00')
        print('Option B | Start: 08:20 - Finish: 15:20')
        print('Option C | Start: 08:40 - Finish: 15:40')
        print('Option D | Start: 09:00 - Finish: 16:00')
        print('Option E | Start: 09:30 - Finish: 16:30')
        
        print('Please Rate each of them from 1 - 5:')
        print('1: Strongly Agree')
        print('2: Agree')
        print('3: Neutral')
        print('4: Disagree')
        print('5: Strongly Di')

        while True:
            print('Option A | Start: 08:00 - Finish: 15:00')
            a = int(input('Please Rate this Option: '))
            if a<1 or a>5:
                print('INVALID INPUT. Please enter values from 1 - 5.')
                continue
            else:
                student_A += a
                student_A_.append(a)
                break

        while True:
            print('Option B | Start: 08:20 - Finish: 15:20')
            b = int(input('Please Rate this Option: '))
            if b<1 or b>5:
                print('INVALID INPUT. Please enter values from 1 - 5.')
                continue
            else:
                student_B += b
                student_B_.append(b)
                break

        while True:
            print('Option C | Start: 08:40 - Finish: 15:40')
            c = int(input('Please Rate this Option: '))
            if c<1 or c>5:
                print('INVALID INPUT. Please enter values from 1 - 5.')
                continue
            else:
                student_C += c
                student_C_.append(c)
                break

        while True:
            print('Option D | Start: 09:00 - Finish: 16:00')
            d = int(input('Please Rate this Option: '))
            if d<1 or d>5:
                print('INVALID INPUT. Please enter values from 1 - 5.')
                continue
            else:
                student_D += d
                student_D_.append(d)
                break

        while True:
            print('Option E | Start: 09:30 - Finish: 16:30')
            e = int(input('Please Rate this Option: '))
            if e<1 or e>5:
                print('INVALID INPUT. Please enter values from 1 - 5.')
                continue
            else:
                student_E += e
                student_E_.append(e)
                break

    elif position == 'N' or position == 'n':
        while True:
            id = input('Please Enter your Unique ID Number : ')
            if id in staff_ID_list:
                print('ID has been used already. Please Try Again')
                continue
            else:
                staff_ID_list.append(id)
                break
        print('Options:')
        print('Option A | Start: 08:00 - Finish: 15:00')
        print('Option B | Start: 08:20 - Finish: 15:20')
        print('Option C | Start: 08:40 - Finish: 15:40')
        print('Option D | Start: 09:00 - Finish: 16:00')
        print('Option E | Start: 09:30 - Finish: 16:30')
        
        print('Please Rate each of them from 1 - 5:')
        print('1: Strongly Agree')
        print('2: Agree')
        print('3: Neutral')
        print('4: Disagree')
        print('5: Strongly Di')

        while True:
            print('Option A | Start: 08:00 - Finish: 15:00')
            a = int(input('Please Rate this Option: '))
            if a<1 or a>5:
                print('INVALID INPUT. Please enter values from 1 - 5.')
                continue
            else:
                staff_A += a
                staff_A_.append(a)
                break

        while True:
            print('Option B | Start: 08:20 - Finish: 15:20')
            b = int(input('Please Rate this Option: '))
            if b<1 or b>5:
                print('INVALID INPUT. Please enter values from 1 - 5.')
                continue
            else:
                staff_B += b
                staff_B_.append(b)
                break

        while True:
            print('Option C | Start: 08:40 - Finish: 15:40')
            c = int(input('Please Rate this Option: '))
            if c<1 or c>5:
                print('INVALID INPUT. Please enter values from 1 - 5.')
                continue
            else:
                staff_C += c
                staff_C_.append(c)
                break

        while True:
            print('Option D | Start: 09:00 - Finish: 16:00')
            d = int(input('Please Rate this Option: '))
            if d<1 or d>5:
                print('INVALID INPUT. Please enter values from 1 - 5.')
                continue
            else:
                staff_D += d
                staff_D_.append(d)
                break

        while True:
            print('Option E | Start: 09:30 - Finish: 16:30')
            e = int(input('Please Rate this Option: '))
            if e<1 or e>5:
                print('INVALID INPUT. Please enter values from 1 - 5.')
                continue
            else:
                staff_E += e
                staff_E_.append(e)
                break
        
    print('Thank Youu for your Response.')    
    cont = input('Do you want to Enter another Response? (y/n): ')
    if cont == 'Y' or cont == 'y':
        continue
    else:
        break

print('RESULTS')

print('Student Response Results:')
print('Option A |',student_A)
print('Option B |',student_B)
print('Option C |',student_C)
print('Option D |',student_D)
print('Option E |',student_E)

print('Staff Response Results:')
print('Option A |',staff_A)
print('Option B |',staff_B)
print('Option C |',staff_C)
print('Option D |',staff_D)
print('Option E |',staff_E)

print('Total Response Results:')
print('Option A |',student_A+staff_A)
print('Option B |',student_B+staff_B)
print('Option C |',student_C+staff_C)
print('Option D |',student_D+staff_D)
print('Option E |',student_E+staff_E)


print('Number of times the preference 1 (Strongly Agree) was chosen by Students for:')
print('Option A |',student_A_.count(1))
print('Option B |',student_B_.count(1))
print('Option C |',student_C_.count(1))
print('Option D |',student_D_.count(1))
print('Option E |',student_E_.count(1))

print('Number of times the preference 1 (Strongly Agree) was chosen by Staffs:')
print('Option A |',staff_A_.count(1))
print('Option B |',staff_B_.count(1))
print('Option C |',staff_C_.count(1))
print('Option D |',staff_D_.count(1))
print('Option E |',staff_E_.count(1))

print('Number of times the preference 1 (Strongly Agree):')
print('Option A |',student_A_.count(1)+staff_A_.count(1))
print('Option B |',student_B_.count(1)+staff_B_.count(1))
print('Option C |',student_C_.count(1)+staff_C_.count(1))
print('Option D |',student_D_.count(1)+staff_D_.count(1))
print('Option E |',student_E_.count(1)+staff_E_.count(1))