details = {}
no = 0
rejected_no = 0
accepted = []
rejected = []
while True:
    pd_list = []
    no+=1
    print('\n\n')
    p_length = int(input('Enter Length of the Parcel: '))
    if p_length>80:
        print('\n\n')
        print('Parcel REJECTED\nParcel Length is more than 80 cm.')
        rejected_no = 1
    print('\n\n')
    p_breadth = int(input('Enter Breadth of the Parcel: '))
    if p_breadth>80:
        print('\n\n')
        print('Parcel REJECTED\nParcel Breadth is more than 80 cm.')
        rejected_no = 1
    print('\n\n')
    p_height = int(input('Enter Height of the Parcel: '))
    if p_height>80:
        print('\n\n')
        print('Parcel REJECTED\nParcel Height is more than 80 cm.')
        rejected_no = 1
    print('\n\n')
    
    
    p_d_sum = p_length+p_height+p_breadth
    if p_d_sum >= 200:
        print('Parcel REJECTED\nSum of Parcel Dimension is more than 200 cm.')
        rejected_no = 1
        print('\n\n')
    
    
    p_weight = int(input('Enter Weight of the Parcel: '))
    if 1 > p_weight > 10:
        print('Parcel REJECTED\nWeight should be Less than 10 Kg and 1 Kg.')
        rejected_no = 1
        print('\n\n')
        
    if p_weight <= 5:
        cost=10
    else:
        cost=10+(p_weight-5)
        
    pd_list.append([p_length,p_breadth,p_height,p_weight,cost])

    if rejected_no == 1:
        rejected.append(pd_list)
        print('\n\nThe Parcel has been Rejected for the following reasons:\n')
        if p_length>80:
            print('Parcel Length is more than 80 cm.')
        if p_breadth>80:
            print('Parcel Breadth is more than 80 cm.')
        if p_height>80:
            print('Parcel Height is more than 80 cm.')
        if p_d_sum >= 200:
            print('Sum of Parcel Dimension is more than 200 cm.')
        if 1< p_weight > 10:
            print('Weight should be Less than 10 Kg and 1 Kg.')
    else:
        print('The Parcel has been Accepted.')
        accepted.append(pd_list)
        details[no] = pd_list
    
    print('\n\n')
    print('Cost: ',cost)
        
    print('\n\n')
    
    add_parcel = input('Do you want to Add parcel? (y/n)')
    if add_parcel == 'y':
        print(details,accepted,rejected)
        continue
    else:
        break
tot=0
for i in accepted:
    tot+=accepted[4]
print('Total Cost: ',tot)