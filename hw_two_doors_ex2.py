
for i in range(0, 3):
    

    PIN_DOOR_1       = '0320'
    PIN_DOOR_2       = '9900'

    pin_door_1       = input('Enter PINCODE 1: ')
    lock_1_open      = pin_door_1 == PIN_DOOR_1

    pin_door_2   = input('Enter PINCODE 2: ')
    lock_2_open  = pin_door_2 == PIN_DOOR_2

    if lock_1_open and lock_2_open:
        print('Entered the FLAT!')
        break

    if lock_1_open == False:
        print('PINCODE 1 incorrect!')

    if lock_2_open == False:
        print('PINCODE 2 incorrect!')