#!/usr/bin/python3

from sys import stderr

def main():
    try:
        num = float(input('Введите число, корень которого хотите найти: '))
        if num < 0:
            raise Exception('Получено отрицательное число.')
    except EOFError:
        print('Данные не поступили.', file=stderr)
    except ValueError:
        print('Введены неверные данные.', file=stderr)
    except Exception as e:
        print(e, file=stderr)
    else:
        print(round((num ** 0.5), 3))
    return


if __name__ == "__main__":
    main()
