# Battery charge in minutes --> 1% for 1 minutes

x = int(input())    # strt charge %
y = int(input())    # stop charge %
i = 1//60           # minutes
if y > 100:
    print('Max 100%')
else:
    while x < y:
        x += 1          # % / minutes
        i += 1
    
    print(i,'minutes for charge to',y, '%')