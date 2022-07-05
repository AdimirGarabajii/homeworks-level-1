


period_s = int(input('Введите время в секундах: '))

period_dd = period_s//86400
rest_dd = period_s - period_dd * 86400

period_hh = rest_dd//3600
rest_hh = rest_dd - period_hh * 3600

period_mm = rest_hh // 60
rest_mm = rest_hh - period_mm * 60

period_ss = rest_mm


print(period_s, 's = d:' ,period_dd, ' h:' ,period_hh, ' m:' ,period_mm, ' s:' ,period_ss)