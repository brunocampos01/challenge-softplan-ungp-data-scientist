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

    def do_withdraw(self, valor: int, list_backnote: list):
        """
        >>> obj = Withdraw()
        >>> obj.do_withdraw(valor=70, list_backnote=[5, 10, 50])
        3
        >>> obj.do_withdraw(valor=73, list_backnote=[20, 50])
        -1
        """
        count_banknotes = 0
        list_backnote.sort(reverse=True)

        while valor > 0:
            for note in list_backnote:

                if math.trunc(valor / note) > 0:
                    total_backnotes = math.trunc(valor / note)

                    # subtrai do total de cédulas do caixa eletrônico
                    self.banknotes_caixa_elet[note] = self.banknotes_caixa_elet[note] - total_backnotes
                    # incrementa a quantidade de cedulas
                    count_banknotes += total_backnotes
                    # subtrai do valor pedido do saque
                    valor -= total_backnotes * note
                    continue

                elif valor > 0:
                    return print('-1')

        return print(count_banknotes)


def main():
    obj = Withdraw()
    backnotes = [20, 50]
    obj.do_withdraw(valor=701, list_backnote=backnotes)


if __name__ == '__main__':
    doctest.testmod()  # automatically validate the embedded tests
    main()
