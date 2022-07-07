

from http import client


service_price               = 150   # USD

client_cash_amount          = int(input('Введите наличные MDL: '))
client_cash_amount_USD      = client_cash_amount / 19       # USD = 19 MDL


if client_cash_amount_USD >= service_price:
    print('Оплата наличными прошла успешно')
else:
    print('У вас недостаточно средств для оплаты данной услуги!')
    client_card_amount_USD  = int(input('Введите сумму USD на вашей карте: '))
    if client_card_amount_USD >= service_price:
        print('Оплата с карты прошла успешно')
    else:
        print('У вас недостаточно на карте средств для оплаты данной услуги!')
        client_crypto_amount_BTC = int(input('Введите сумму BTC: '))
        client_crypto_amount_BTC_to_USD  =  client_crypto_amount_BTC * 20883
        if client_crypto_amount_BTC_to_USD >= service_price:
            print('Оплата BTC прошла успешно')
        else:
            print('У вас недостаточно средств для оплаты данной услуги!')
            client_cash_card_amount_ans = input('Вы желаете оплатить частично с карты и наличными? yes/no: ')
            if client_cash_card_amount_ans == 'yes' and client_cash_amount_USD + client_card_amount_USD >= service_price:
                print('Оплата наличными и с карты прошла успешно')
            else:
                print('У вас недостаточно средств для оплаты данной услуги!')

                    