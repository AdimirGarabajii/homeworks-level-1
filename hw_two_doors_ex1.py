



PIN_DOOR_1       = '0320'
PIN_DOOR_2       = '9900'

pin_door_1       = input('Enter PINCODE 1: ')
lock_1_open      = pin_door_1 == PIN_DOOR_1

if lock_1_open:
    print('Entered the building!')

    pin_door_2   = input('Enter PINCODE 2: ')
    lock_2_open  = pin_door_2 == PIN_DOOR_2

    if lock_2_open:
        print('Entered the FLAT!')

    else:
        print('ERROR PINCODE 2')
else:
    print('ERROR PINCODE 1')
