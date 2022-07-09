from sqlite3 import connect


PARKING_PLACES = 7
FREE_PLACE = 3

print("#"*PARKING_PLACES*5)

for place_index in range(1, PARKING_PLACES):
    print("| X |", end="")
    
    if place_index ==2:
        print("|   |", end="")
        
        
print("\n","#"*PARKING_PLACES*5, sep="")