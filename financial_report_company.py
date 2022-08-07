

profit = [
    [1000.00, 2000.00, 3000.00, 1000.00],
    [4000.00, 5000.00, 6000.00, 1000.00],
    [7000.00, 8000.00, 9000.00, 1000.00]

]

for yi in range(len(profit)):
    #s = profit[yi][0] + profit[yi][1] + profit[yi][2] + profit[yi][3]
    s = sum(profit[yi])
    avg = s / 4

    profit[yi].append(avg)
#print(profit)

for yi in range(len(profit)):
    maximum_profit = max(profit[yi])
    profit[yi].append(maximum_profit)
#print(maximum_profit)



for yi in range(len(profit)):
    print(f"year {yi+1%3} |\
    {profit[yi][0]:9.2f} |\
    {profit[yi][1]:9.2f} |\
    {profit[yi][2]:9.2f} |\
    {profit[yi][3]:9.2f} |\
      |avg -{profit[yi][4]: 9.2f} ||\
      |max -{profit[yi][5]: 9.2f} ||")
print()