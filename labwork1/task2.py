#!/usr/bin/python3

from random import randint
from sys import stderr


def main():
    try:
        num = int(input('Введите число: '))
        ran_num = randint(-10, 10)
        res = num / ran_num
    except ValueError:
        print('Введены неверные данные.', file=stderr)
    except EOFError:
        print('Данные не поступили.', file=stderr)
    except ZeroDivisionError:
        print('Деление на ноль.', file=stderr)
    else:
        print(res)
    return


if __name__ == "__main__":
    main()
