# data
plane_altitude   = int(input('Введите высоту : '))     
plane_speed      = int(input('Введите скорость самолета: '))      
fre_runway       = int(input('Введите наличие свободных полосы : '))
wind_speed       = int(input('Введите скорость ветра: '))       
wind_direction   = input('Введите направление ветра N, E,  S,  W, : ')
plane_direction  = input('Введите курс самолета N, E, S,  W, : ')
fuel_tank        = float(input('Введите остаток топлива в %: '))         
tehnical_error   = input('Наличие поломок True или False: ')

N = 1
E = 2
S = 3
W = 4

# logic
can_land = plane_altitude < 700 and plane_altitude > 100\
           and plane_speed < 500 and plane_speed > 200\
           and fre_runway >= 1\
           and wind_speed < 100 and wind_direction != plane_direction\
           and fuel_tank > 1\
           or tehnical_error


# view
print("Can the plane land? ",'Высота -',plane_altitude,' meters ',\
    'скорость самолета: ',plane_speed,'km/h','полоса: ',fre_runway,\
    'скорость ветра: ',wind_speed,'km/h','направление ветра: ',wind_direction,\
    'курс самолета: ',plane_direction,'наличие топлива: ',fuel_tank,'%',\
    'наличие поломок: ',tehnical_error,'разрешение на посадку', can_land )
