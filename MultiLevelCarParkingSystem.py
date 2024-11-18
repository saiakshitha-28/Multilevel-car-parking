#method to print the vehicle slots in structured manner
def print_slots(total_capacity):
    for i in range(len(total_capacity)):
        print("\nFloor ", i+1, ' =>')
        for j in range(len(total_capacity[0])):
            for k in range(len(total_capacity[0][0])):
                print(total_capacity[i][j][k].center(10), end=' ')
            print()


#method if user enters 'in' 
def in_method(t,r,c,f,x):
    for i in range(f):
        for j in range(r):
            for k in range(c):
                if t[i][j][k]=='free':
                    print(f'Parking slot is allocated for your vehicle.{x} at :\nRow={j+1}\nColumn={k+1}\nfloor={i+1}')
                    t[i][j][k]=f'vehicle{x}'#######The major issue is here why is it changing all the values
                    return True
    print(f'All the parking slots are FULL, can\'t park vehicle.{x}')
    return False
def out_method(t,r,c,f,x):
    for i in range(f):
        for j in range(r):
            for k in range(c):
                if t[i][j][k]==f'vehicle{x}':
                    t[i][j][k]='free'
                    return

def check(prompt):
    while True:
        try:
            val=int(input(prompt))
            return val
        except:
            print("Enter correct input")

#_main_
r=check('Enter the maximum number of rows in your parking area : ')
c=check('Enter the maximum number of columns in your parking area : ')
f=check('How many floors do you have for parking? : ')
    
total_capacity=[[[ 'free' for k in range(c)] for j in range(r)] for i in range(f)]

print('\n\tEnter \'in\' to park a new vehicle')
print('\tEnter \'out.vehicle<number>\' to unpark a parked vehicle with its number')
print('\tEnter \'--display-slots\' to see the available slots in a 3D-list format')
print('\tEnter \'close\' to terminate the program')

process=input()
#waits for the user input
#out interface
vno=0#used for naming every vehice comes to park
vnolist=[]#used to store the history of the parked vehicles
while process!='close':
    if process=='in':
        check=in_method(total_capacity,r,c,f,vno+1)
        if check==True:
            #if the parking slot is available, allocated
            vno+=1
            vnolist.append(vno)#m the vehicle name into the record of current parked vehicles
    elif process=='--display-slots':
        print("\n\tDataBase -> ",)
        print_slots(total_capacity)
    else:
        vehiclenumber=process.replace('out.vehicle','')
        try:
            #vehicle number is generated here
            vehiclenumber=int(vehiclenumber)
            #checking if that vehicle number exists or not
            if vehiclenumber in vnolist:
                #vehicle is already parked now get it removed
                vnolist.remove(vehiclenumber)#removing that particular vehicle from the record of current parked vehicles
                #pass to the method to make changes in the list
                out_method(total_capacity,r,c,f,vehiclenumber)
                print(f'Vehicle.{vehiclenumber} is unparked successfully')
            else:
                #if user tries to remove the vehicle which is not parked
                print('The vehicle does\'nt exist to be unparked')
        except ValueError:
            print('Enter the correct input')
    process = input('\n')
print('The process is terminated successfully')
if vnolist!=[]:
    print("\tALERT!",end=' ')
    print("Below vehicle/s are yet to be unparked")
    #for i in range(len(vnolist)):
        #print(f'\tVehicle({vnolist[i]})')
    print_slots(total_capacity)
