"""Questão 04"""
import doctest
import math


class Withdraw():
    def __init__(self):
        # total de cédulas no caixa eletrônico
        self.banknotes_caixa_elet = {
            5: 100,
            10: 10,
            20: 5,
            50: 8
        }

    def do_withdraw(self, value: int, list_backnote: list):
        """
        >>> obj = Withdraw()
        >>> obj.do_withdraw(value=70, list_backnote=[5, 10, 50])
        3
        >>> obj.do_withdraw(value=73, list_backnote=[20, 50])
        -1
        """
        count_banknotes = 0
        list_backnote.sort(reverse=True)

        try:
            while value > 0:
                for note in list_backnote:

                    if math.trunc(value / note) > 0:
                        total_backnotes = math.trunc(value / note)

                        # subtrai do total de cédulas do caixa eletrônico
                        self.banknotes_caixa_elet[note] = self.banknotes_caixa_elet[note] - total_backnotes
                        # incrementa a quantidade de cedulas
                        count_banknotes += total_backnotes
                        # subtrai do value pedido do saque
                        value -= total_backnotes * note
                        continue

                    elif value > 0:
                        return print('-1')

        except TypeError as err:
            print(f"Valor de saque inválido {value} \nERROR: {err}")

        return print(count_banknotes)


def main():
    obj = Withdraw()
    backnotes = [20, 50]
    obj.do_withdraw(value=101, list_backnote=backnotes)


if __name__ == '__main__':
    doctest.testmod()
    main()
