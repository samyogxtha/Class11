S_response = []
T_response = []
ID_list = []

A_sum_T = 0
B_sum_T = 0
C_sum_T = 0
D_sum_T = 0
E_sum_T = 0
A_sum_S = 0
B_sum_S = 0
C_sum_S = 0
D_sum_S = 0
E_sum_S = 0


#the below variables are for the tally marks

TA1=0
TA2=0
TA3=0
TA4=0
TA5=0

TB1=0
TB2=0
TB3=0
TB4=0
TB5=0

TC1=0
TC2=0
TC3=0
TC4=0
TC5=0

TD1=0
TD2=0
TD3=0
TD4=0
TD5=0

TE1=0
TE2=0
TE3=0
TE4=0
TE5=0
#TALLY FOR STUDENTS
SA1=0
SA2=0
SA3=0
SA4=0
SA5=0

SB1=0
SB2=0
SB3=0
SB4=0
SB5=0

SC1=0
SC2=0
SC3=0
SC4=0
SC5=0

SD1=0
SD2=0
SD3=0
SD4=0
SD5=0

SE1=0
SE2=0
SE3=0
SE4=0
SE5=0

print( 'PYTHON SCHOOL BELL TIMINGS PROPOSAL \n\nThe school has been given options for bell timings proposed by the staff and other members \nWe would like to know what your opinions are on this matter')
print( '\n\nGiven are five options, please rate all of them from 1 - 5 :  \n1 being strongly agree \n2 being agree \n3 being neutral \n4 being disagree \n5 being strongly disagree')
print( '\n\nYou will be asked to enter your four digit ID number given to you by the school, \nStaff ID starting with T and student ID starting with S')

while True:
    id = input( 'Please enter your four digit ID number : ')
    if id in ID_list:
        print( 'Sorry, that ID has already been used \nPlease check if you have mistyped it or enter another ID.')
        continue
    elif len(id) != 4:
        print( 'sorry invalid ID, please enter again.')
        continue
    else:
        ID_list.append(id)
    if id.startswith('T') or id.startswith('t'):
        while True:
            A = int(input( 'the first option is : \nA Start: 08:00- Finish: 15:00\nrate this from 1 - 5 : \n'))
            if A>5 or A<1:
                print( 'Invalid value, Please enter correct value')
                print( '\n\nplease rate this proposal from 1 - 5 :  \n1 being strongly agree \n2 being agree \n3 being neutral \n4 being disagree \n5 being strongly disagree')
                continue
            else:
                if A == 1:
                    TA1 += 1
                elif A == 2:
                    TA2 += 1
                elif A == 3:
                    TA3 += 1
                elif A == 4:
                    TA4 += 1
                else:
                    TA5 += 1
                A_sum_T += A
                break
        while True:
            B = int(input( 'the second option is : \nB Start: 08:20-Finish: 15:20\nrate this from 1 - 5 : \n'))
            if B>5 or B<1:
                print( 'Invalid value, Please enter correct value')
                print( '\n\nplease rate this proposal from 1 - 5 :  \n1 being strongly agree \n2 being agree \n3 being neutral \n4 being disagree \n5 being strongly disagree')
                continue
            else:
                if B == 1:
                    TB1 += 1
                elif B == 2:
                    TB2 += 1
                elif B == 3:
                    TB3 += 1
                elif B == 4:
                    TB4 += 1
                else:
                    TB5 += 1
                B_sum_T += B
                break
        while True:
            C = int(input( 'the third option is : \nC Start: 08:40-Finish: 15:40\nrate this from 1 - 5 : \n'))
            if C>5 or C<1:
                print( 'Invalid value, Please enter correct value')
                print( '\n\nplease rate this proposal from 1 - 5 :  \n1 being strongly agree \n2 being agree \n3 being neutral \n4 being disagree \n5 being strongly disagree')
                continue
            else:
                if C == 1:
                    TC1 += 1
                elif C == 2:
                    TC2 += 1
                elif C == 3:
                    TC3 += 1
                elif C == 4:
                    TC4 += 1
                else:
                    TC5 += 1
                C_sum_T += C
                break
        while True:
            D = int(input( 'the fourth option is : \nD Start: 09:00- Finish: 16:00\nrate this from 1 - 5 : \n'))
            if D>5 or D<1:
                print( 'Invalid value, Please enter correct value')
                print( '\n\nplease rate this proposal from 1 - 5 :  \n1 being strongly agree \n2 being agree \n3 being neutral \n4 being disagree \n5 being strongly disagree')
                continue
            else:
                if D == 1:
                    TD1 += 1
                elif D == 2:
                    TD2 += 1
                elif D == 3:
                    TD3 += 1
                elif D == 4:
                    TD4 += 1
                else:
                    TD5 += 1
                D_sum_T += D
                break
        while True:
            E = int(input( 'the final option is : \nE Start: 09:30-Finish: 16:30\nrate this from 1 - 5 : \n'))
            if E>5 or E<1:
                print( 'Invalid value, Please enter correct value')
                print( '\n\nplease rate this proposal from 1 - 5 :  \n1 being strongly agree \n2 being agree \n3 being neutral \n4 being disagree \n5 being strongly disagree')
                continue
            else:
                if E == 1:
                    TE1 += 1
                elif E == 2:
                    TE2 += 1
                elif E == 3:
                    TE3 += 1
                elif E == 4:
                    TE4 += 1
                else:
                    TE5 += 1
                E_sum_T += E
                break

        d_T_res = {id:{'A': A ,'B':B,'C':C,'D':D,'E':E}}
        T_response.append(d_T_res)

    elif id.startswith('S') or id.startswith('s'):

        while True:
            A = int(input( 'the first option is : \nA Start: 08:00- Finish: 15:00\nrate this from 1 - 5 : \n'))
            if A>5 or A<1:
                print( 'Invalid value, Please enter correct value')
                print( '\n\nplease rate this proposal from 1 - 5 :  \n1 being strongly agree \n2 being agree \n3 being neutral \n4 being disagree \n5 being strongly disagree')
                continue
            else:
                if A == 1:
                    SA1 += 1
                elif A == 2:
                    SA2 += 1
                elif A == 3:
                    SA3 += 1
                elif A == 4:
                    SA4 += 1
                else:
                    SA5 += 1
                A_sum_S += A
                break
        while True:
            B = int(input( 'the second option is : \nB Start: 08:20-Finish: 15:20\nrate this from 1 - 5 : \n'))
            if B>5 or B<1:
                print( 'Invalid value, Please enter correct value')
                print( '\n\nplease rate this proposal from 1 - 5 :  \n1 being strongly agree \n2 being agree \n3 being neutral \n4 being disagree \n5 being strongly disagree')
                continue
            else:
                if B == 1:
                    SB1 += 1
                elif B == 2:
                    SB2 += 1
                elif B == 3:
                    SB3 += 1
                elif B == 4:
                    SB4 += 1
                else:
                    SB5 += 1
                B_sum_S += B
                break
        while True:
            C = int(input( 'the third option is : \nC Start: 08:40-Finish: 15:40\nrate this from 1 - 5 : \n'))
            if C>5 or C<1:
                print( 'Invalid value, Please enter correct value')
                print( '\n\nplease rate this proposal from 1 - 5 :  \n1 being strongly agree \n2 being agree \n3 being neutral \n4 being disagree \n5 being strongly disagree')
                continue
            else:
                if C == 1:
                    SC1 += 1
                elif C == 2:
                    SC2 += 1
                elif C == 3:
                    SC3 += 1
                elif C == 4:
                    SC4 += 1
                else:
                    SC5 += 1
                C_sum_S += C
                break
        while True:
            D = int(input( 'the fourth option is : \nD Start: 09:00- Finish: 16:00\nrate this from 1 - 5 : \n'))
            if D>5 or D<1:
                print( 'Invalid value, Please enter correct value')
                print( '\n\nplease rate this proposal from 1 - 5 :  \n1 being strongly agree \n2 being agree \n3 being neutral \n4 being disagree \n5 being strongly disagree')
                continue
            else:
                if D == 1:
                    SD1 += 1
                elif D == 2:
                    SD2 += 1
                elif D == 3:
                    SD3 += 1
                elif D == 4:
                    SD4 += 1
                else:
                    SD5 += 1
                D_sum_S += D
                break
        while True:
            E = int(input( 'the final option is : \nE Start: 09:30-Finish: 16:30\nrate this from 1 - 5 : \n'))
            if E>5 or E<1:
                print( 'Invalid value, Please enter correct value')
                print( '\n\nplease rate this proposal from 1 - 5 :  \n1 being strongly agree \n2 being agree \n3 being neutral \n4 being disagree \n5 being strongly disagree')
                continue
            else:
                if E == 1:
                    SE1 += 1
                elif E == 2:
                    SE2 += 1
                elif E == 3:
                    SE3 += 1
                elif E == 4:
                    SE4 += 1
                else:
                    SE5 += 1
                E_sum_S += E
                break
        d_S_res = {id:{'A': A ,'B': B ,'C': C ,'D': D ,'E': E }}
        S_response.append(d_S_res)

    else:
        print( 'invalid ID \nPlease check if you have mistyped it or enter another ID')
        continue
    cont=input( 'would you like to enter another response?(y/n)')
    if cont == 'y':
        continue
    else:
        Tally_T = {A:[TA1,TA2,TA3,TA4,TA5],B:[TB1,TB2,TB3,TB4,TB5],C:[TC1,TC2,TC3,TC4,TC5],D:[TD1,TD2,TD3,TD4,TD5],E:[TE1,TE2,TE3,TE4,TE5]}
        Tally_S = {A:[SA1,SA2,SA3,SA4,SA5],B:[SB1,SB2,SB3,SB4,SB5],C:[SC1,SC2,SC3,SC4,SC5],D:[SD1,SD2,SD3,SD4,SD5],E:[SE1,SE2,SE3,SE4,SE5]}
        total_S = [A_sum_S ,B_sum_S ,C_sum_S ,D_sum_S ,E_sum_S]
        total_T = [A_sum_T ,B_sum_T ,C_sum_T ,D_sum_T ,E_sum_T]
        break

#the totalling results

print('Thank you for your response, the results are given below.')

print( 'Teacher response results : \nResults for option A - Start: 08:00- Finish: 15:00 :',total_T[0])
print( '\nResults for option B - Start: 08:20- Finish: 15:20 :',total_T[1])
print( '\nResults for option C - Start: 08:40- Finish: 15:40 :',total_T[2])
print( '\nResults for option D - Start: 09:00- Finish: 16:00 :',total_T[3])
print( '\nResults for option E - Start: 09:20- Finish: 16:20 :',total_T[4])

print( 'Student response results : \nResults for option A - Start: 08:00- Finish: 15:00 :',total_S[0])
print( '\nResults for option B - Start: 08:20- Finish: 15:20 :',total_S[1])
print( '\nResults for option C - Start: 08:40- Finish: 15:40 :',total_S[2])
print( '\nResults for option D - Start: 09:00- Finish: 16:00 :',total_S[3])
print( '\nResults for option E - Start: 09:20- Finish: 16:20 :',total_S[4])

print( 'Total response results : \n',' Results for option A - Start: 08:00- Finish: 15:00 :',total_S[0] + total_T[0])
print( '\nResults for option B - Start: 08:20- Finish: 15:20 :',total_S[1] + total_T[1])
print( '\nResults for option C - Start: 08:40- Finish: 15:40 :',total_S[2] + total_T[2])
print( '\nResults for option D - Start: 09:00- Finish: 16:00 :',total_S[3] + total_T[3])
print( '\nResults for option E - Start: 09:20- Finish: 16:20 :',total_S[4] + total_T[4])

#tallying starts from here

print( 'Teacher tally results : \nTally results for option A - Start: 08:00- Finish: 15:00 :\n1)',Tally_T[A][0],'\n2)',Tally_T[A][1],'\n3)',Tally_T[A][2], '\n4)',Tally_T[A][3],'\n5)',Tally_T[A][4])
print( '\nTally results for option B - Start: 08:20- Finish: 15:20 :\n1)',Tally_T[B][0],'\n2)',Tally_T[B][1],'\n3)',Tally_T[B][2], '\n4)',Tally_T[B][3],'\n5)',Tally_T[B][4])
print( '\nTally results for option C - Start: 08:40- Finish: 15:40 :\n1)',Tally_T[C][0],'\n2)',Tally_T[C][1],'\n3)',Tally_T[C][2], '\n4)',Tally_T[C][3],'\n5)',Tally_T[C][4])
print( '\nTally results for option D - Start: 09:00- Finish: 16:00 :\n1)',Tally_T[D][0],'\n2)',Tally_T[D][1],'\n3)',Tally_T[D][2], '\n4)',Tally_T[D][3],'\n5)',Tally_T[D][4])
print( '\nTally results for option E - Start: 09:20- Finish: 16:20 :\n1)',Tally_T[E][0],'\n2)',Tally_T[E][1],'\n3)',Tally_T[E][2], '\n4)',Tally_T[E][3],'\n5)',Tally_T[E][4])

print( 'Student tally results : \nTally results for option A - Start: 08:00- Finish: 15:00 :\n1)',Tally_S[A][0],'\n2)',Tally_S[A][1],'\n3)',Tally_S[A][2], '\n4)',Tally_S[A][3],'\n5)',Tally_S[A][4])
print( '\nTally results for option B - Start: 08:20- Finish: 15:20 :\n1)',Tally_S[B][0],'\n2)',Tally_S[B][1],'\n3)',Tally_S[B][2], '\n4)',Tally_S[B][3],'\n5)',Tally_S[B][4])
print( '\nTally results for option C - Start: 08:40- Finish: 15:40 :\n1)',Tally_S[C][0],'\n2)',Tally_S[C][1],'\n3)',Tally_S[C][2], '\n4)',Tally_S[C][3],'\n5)',Tally_S[C][4])
print( '\nTally results for option D - Start: 09:00- Finish: 16:00 :\n1)',Tally_S[D][0],'\n2)',Tally_S[D][1],'\n3)',Tally_S[D][2], '\n4)',Tally_S[D][3],'\n5)',Tally_S[D][4])
print( '\nTally results for option E - Start: 09:20- Finish: 16:20 :\n1)',Tally_S[E][0],'\n2)',Tally_S[E][1],'\n3)',Tally_S[E][2], '\n4)',Tally_S[E][3],'\n5)',Tally_S[E][4])

print( 'Total tally results : \nTally results for option A - Start: 08:00- Finish: 15:00 :\n1)',Tally_T[A][0] + Tally_S[A][0],'\n2)',Tally_T[A][1] + Tally_S[A][1],'\n3)',Tally_T[A][2] + Tally_S[A][2], '\n4)',Tally_T[A][3] + Tally_S[A][3],'\n5)',Tally_T[A][4] + Tally_S[A][4])
print( '\nTally results for option B - Start: 08:20- Finish: 15:20 :\n1)',Tally_T[B][0] + Tally_S[B][0],'\n2)',Tally_T[B][1] + Tally_S[B][1],'\n3)',Tally_T[B][2] + Tally_S[B][2], '\n4)',Tally_T[B][3] + Tally_S[B][3],'\n5)',Tally_T[B][4] + Tally_S[B][4])
print( '\nTally results for option C - Start: 08:40- Finish: 15:40 :\n1)',Tally_T[C][0] + Tally_S[C][0],'\n2)',Tally_T[C][1] + Tally_S[C][1],'\n3)',Tally_T[C][2] + Tally_S[C][2], '\n4)',Tally_T[C][3] + Tally_S[C][3],'\n5)',Tally_T[C][4] + Tally_S[C][4])
print( '\nTally results for option D - Start: 09:00- Finish: 16:00 :\n1)',Tally_T[D][0] + Tally_S[D][0],'\n2)',Tally_T[D][1] + Tally_S[D][1],'\n3)',Tally_T[D][2] + Tally_S[D][2], '\n4)',Tally_T[D][3] + Tally_S[D][3],'\n5)',Tally_T[D][4] + Tally_S[D][4])
print( '\nTally results for option E - Start: 09:20- Finish: 16:20 :\n1)',Tally_T[E][0] + Tally_S[E][0],'\n2)',Tally_T[E][1] + Tally_S[E][1],'\n3)',Tally_T[E][2] + Tally_S[E][2], '\n4)',Tally_T[E][3] + Tally_S[E][3],'\n5)',Tally_T[E][4] + Tally_S[E][4])

print( 'that is the end of the results, Thankyou for using python decider')
