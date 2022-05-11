def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def run():
    # try:
    #     num = int(input('Ingresa un número: '))
    #     print(divisors(num))
    #     print('Terminó mi programa')
    # except:
    #     print('Debes ingresar un número')

    num = input('Ingresa un número: ')
    assert num.isnumeric(), 'Debes ingresar un número'
    print(divisors(int(num)))
    print('Terminó mi programa')


if __name__ == '__main__':
    run()