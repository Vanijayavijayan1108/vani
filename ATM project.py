# ATM project
card = input('Enter your card number: ')
pin = input('Enter your pin number : ')


def validate(card, pin):
    if card == '123456' and pin == '9847':
        return 'valid'
    elif pin != '9847':
        return 'pin is invalid'
    elif card != '123456':
        return 'card is invalid'


def bank_details(bank_atm, card, pin):
    print('Welcome to ', bank_atm, 'ATM')
    print('INSERT YOUR ATM CARD \nENTER YOUR PIN NUMBER')
    return validate(card, pin)


amount = 10000
limit = 3
total = 40000
bank_atm = 'SBI'

for x in range(limit):
    value = bank_details(bank_atm, card, pin)
    if value == 'valid':
        print(value)
        print("You're balance amount is ", total)
        print('\n')
        i = 1000
        count = 1
        while i <= amount:
            print('Count number ', count, ' : ', i)
            i += 1000
            count += 1
    else:
        print(value)
        break
    print('___________________________')
print('Thanks for using this ATM')
