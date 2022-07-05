import datetime
from tracemalloc import stop

#for year in range(1900, 2022):
    
year_born        = int(input('Введите год вашего рождения: '))
year_actual      = datetime.datetime.today().year
your_age_today   = year_actual - year_born

if year_born < 1900 or year_born > year_actual:
    stop [year_born]

if your_age_today == 0:
    print('Добро пожаловать в этот мир, новорожденный')
    
if your_age_today <= 3:
    print('Вы совсем кроха, вам всего', your_age_today)

elif your_age_today >= 4 and your_age_today <= 9:
    print('Как мило, вы ребенок, вам всего', your_age_today)

elif your_age_today >= 10 and your_age_today <= 15:
    print('Подросток, начало пути, вам уже',your_age_today)

elif your_age_today >= 16 and your_age_today <= 18:
    print('Вы юны вам',your_age_today)

elif your_age_today >= 19 and your_age_today <= 50:
    print('Вы взрослый состоявшийся, вам',your_age_today)

else:
    print('Вы мудрец, вам целых',your_age_today)
