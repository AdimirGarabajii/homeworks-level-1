food_1_name      = 'Pizza'
food_1_price     = 100   
food_1_available = 5
food_1_quantity  = int(input('How many ' + food_1_name + ' do you want ? '))

if food_1_available < food_1_quantity:
    print('max 5')

else:
    food_1_cost = food_1_quantity * food_1_price

    food_2_name         = 'Salad'
    food_2_price        = 75
    food_2_available    = 10
    food_2_quantity  = int(input('How many ' + food_2_name + ' do you want ? '))

    if food_2_available < food_2_quantity:
        print('max 10')

    else:
        food_2_cost = food_2_quantity * food_2_price

        food_3_name         = 'Cofee'
        food_3_price        = 25
        food_3_available    = 50
        food_3_quantity  = int(input('How many ' + food_3_name + ' do you want ? '))

        if food_3_available < food_3_quantity:
            print('max 50')

        else:
            food_3_cost = food_3_quantity * food_3_price

            delivery_free_limit      = 1000
            delivery_wanted          = input('Do you want to delivery ( yes/no) ? ')
            delivery_price           = 150
            if delivery_wanted       == 'yes':
                client_address       = input('Your address ')
            order_cost           = food_1_cost + food_2_cost + food_3_cost   

            if order_cost >= 1000 and delivery_wanted =='yes':
                print('Your amount =', order_cost, 'MDL, free delivery to',client_address)
                
            elif order_cost < 1000 and delivery_wanted == 'yes':
                print('Your amount =', order_cost, 'MDL, delivery to',client_address, delivery_price, ' MDL')

            else:
                print('Your amount =', order_cost, 'MDL')

        
