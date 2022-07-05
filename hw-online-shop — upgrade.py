
# start online shop



from unittest import result


client_name              = input('Как к вам обращаться?: ')
print('Здравствуйте,',client_name,'!')
slect_food               = input('Вы желаете заказать еду (yes/no)?')
if slect_food            == 'yes':
    print('У нас очень большой выбор!')


# my order
    
    pizza_amount             = int(input('Введите количество пицц: '))
    pizza_price              = 98

    if pizza_amount > 5:
        print('max 5')
        while pizza_amount >5:
            if pizza_amount <= 5:
                break
            

    lasagne_amount           = int(input('Введите количество лазаний: '))
    lasagne_price            = 80

    burger_amount            = int(input('Введите количество бургеров: '))
    burger_price             = 75

    french_fries_amount      = int(input('Введите количество картошек фри: '))
    french_fries_price       = 30



# conditions for delivery
    delivery_free_limit = 500.0

    delivery_wanted_str      = input('Вы желаете доставку ( yes/no) ? ')
    delivery_price           = 60
    client_is_vip_str        = input('Вы являетесь VIP клиентом (yes/no) ? ')
    if delivery_wanted_str   == 'yes':
        client_address        = input('Введите адрес доставки ')

# order cost
    order_cost               = pizza_amount * pizza_price + lasagne_amount * lasagne_price\
                         + burger_amount * burger_price + french_fries_amount * french_fries_price
    

    if order_cost < 500 and delivery_wanted_str == 'yes' and client_is_vip_str != 'yes':
        print('Сумма вашего заказа =' ,order_cost, 'л. по адресу',client_address,'для бесплатной доставки добавьте товар на'\
            ,delivery_free_limit - order_cost, 'л. или оплатите доставку =',delivery_price, 'л.')


    elif order_cost > 500 and delivery_wanted_str == 'yes' and client_is_vip_str != 'yes':
        print('Сумма вашего заказа =' ,order_cost, 'л. по адресу',client_address,' доставка бесплатная')

    elif client_is_vip_str == 'yes' and delivery_wanted_str == 'yes':
        print('Сумма вашего заказа =' ,order_cost, 'л. по адресу',client_address)

    else:
        print('Сумма вашего заказа =' ,order_cost, 'л')
    print('Хорошего вечера',client_name,'!')
