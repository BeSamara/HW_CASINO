from random import randint
from balance import money
slot = randint(1,30)
bank = money
def game():
    global bank
    print('Welcome to the Casino!\n')

    try:
        while 1:
            print(f'Your current balance: {bank}')
            com = input('Make your choice\n1 Start \n2 Exit\n')
            if com == '1':
                insrt = int(input('Choose your slot: '))
                stavka = int(input('Your offer: '))
                if insrt == slot and stavka <= bank:
                    bank += (stavka*2)
                    print('Вы угодали!')
                elif slot != insrt and stavka <= bank:
                    if bank > 0 and stavka <= bank:
                        bank -= stavka
                        print('Lost!')
                elif bank == 0:
                    print('You lost your money')
                    continue
                elif stavka > bank:
                    print('You have no money left!')
            elif com == '2':
                if bank < 1000:
                    print('You lost')
                    print('Game over')
                    print(f'Your current balance {bank}')
                    break
                elif bank > 1000:
                    print('You lost')
                    print('Game over')
                    print(f'Your current balance {bank}')
                    break
            else:
                print('Wrong number!')
    except TypeError:
        print('Something went wrong...')
    except ValueError:
        print('Numbers only!')
    except Exception:
        print('Something went wrong')