



consume = [
    #L/100km
    # 10-20 km/h      50-60 km/h      100-120 km/h      150-200 km/h
    [2.0,              3.0,             4.0,             5.0],  # 1.2l
    [3.0,              4.0,             6.0,             8.0],  #2.0l
    [10.0,             15.0,           20.0,            25.0]   #8.0l
]
col_labels = ['10-20 km/h','50-60 km/h','100-120 km/h','150-200 km/h']
row_labels = [
    '1.2l',
    '2.0l',
    '8.0l',
]
print(end='    ')
for ci in range(len(consume[0])):
    print(f'|{col_labels[ci]:>12}|', end='')
print()
for ri in range(len(consume)):
    print(row_labels[ri], end='')
    for ci in range(len(consume[0])):
        print(f'| {consume[ri][ci]:11.1f}|', end='')
    print()