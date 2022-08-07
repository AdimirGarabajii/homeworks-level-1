import random


data = [1, 3, 5, 19, 33,6]

#maximal = max(data)
#print(maximal)

maximal = data[0]
for i in range(len(data)):
    if data[i] > maximal:
        maximal = data[i]
print(maximal)

minimal = data[0]
for random in range(len(data)):
    if data[random] < minimal:
        minimal = data[random]
print(minimal)

exists = int(input())
for i in range(len(data)):
    if data[i] == exists:
        print(True)



