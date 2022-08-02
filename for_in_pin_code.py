from os import system
system('cls')

PIN = '1234'
for tries in range(3):
    pin = input('PIN: ')
    if pin != PIN:
        print('Invalid pin')
    if pin == PIN:
        print('Welcome!')
        break
