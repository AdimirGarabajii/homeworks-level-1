#Изменить код так чтобы можно было указать место корабля с клавиатуры

#Переменную small_ship изменить на big_ship - большой корабль, т. е. - координата большого корабля

#Изменить код if/else так чтобы если бы big_ship = 5 - результат выглядел бы так

small_ship = int(input())
big_ship   = int(input())
big_ship   -= 1

for x in range(1,11):
    if x == small_ship:
        print( "⛵", end="" )
    else:
        print( "~", end="" )

print('\n')
for x in range(1,11):
    if x == big_ship:
        print('w⛴w', end='')
    else:
        print( "~", end="" )
     
