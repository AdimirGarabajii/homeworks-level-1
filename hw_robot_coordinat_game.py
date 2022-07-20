from os import system

#  a - moove left
#  b - moove right



length   = 20
roboX    = 5
bombX    = 8
hp       = 100
battery  = 100
hearts   = 16
score    = 0
chargestation = 20

while True:
    system('cls')
    if roboX == hearts:
        hp += 25
    if roboX == 11:
        score += 1
    if roboX == chargestation:
        battery += 50
    if bombX == roboX:
        hp -= 25
        if hp <= 0: 
            print("❌❌❌game over!❌❌❌")
            break
    ######## DRAWING THE MAP #######
    x = 1
    print('\n')

    while x <= length:
        if x == roboX:
            print('🤖', end ='')   # \n
        elif x == 8:
            print('💣', end ='') 
        elif x == hearts:
            print('💗', end ='')
        elif x == 11:
            print('💰', end ='')
        elif x == chargestation:
            print('🔋' , end ='')
        else:
            print('▬', end ='')   # \n
        x += 1
    print('\n')

    print ('health =',hp, '\n')
    print('energy =', battery, '\n')
    print('score =', score, '\n')

    direction = input('a/d')
    battery -= 5
    if direction == 'a':
        roboX -= 1
    if direction == 'd':
        roboX += 1
    if direction == 'x':
        system('cls')
        print("Thanks")
        break
    if battery == 0:
        print('low battery')
        break
    if roboX == 0 or roboX == 21:
        print('map error')
        break