class KolkoKrzyz:
    def __init__(self, znak: str = '0'):
        if znak not in ('O', 'X'):
            raise ValueError("Znakiem może być tylko O lub X!")
        self.__kratka = [[' ', ' ', ' '],
                         [' ', ' ', ' '],
                         [' ', ' ', ' ']]
        self.__znak = znak
        self.__kolo = True
        self.__krzyz = False
        self.__win = False
        if znak == 'O':
            self.__kolo = False
            self.__krzyz = True
        self._checkwin()

    def __str__(self):
        napis = ""
        for i in range(3):
            for j in range(3):
                napis += "|"
                napis += self.__kratka[i][j]
            napis += '|\n'
        return napis

    @staticmethod
    def help():
        print("|1|2|3|\n|4|5|6|\n|7|8|9|")

    def _checkwin(self):
        for i in range(3):
            for j in range(3):
                if self.__kratka[i][0] == self.__kratka[i][1] == self.__kratka[i][2] != ' ' or \
                        self.__kratka[0][j] == self.__kratka[1][j] == self.__kratka[2][j] != ' ' or \
                        self.__kratka[0][0] == self.__kratka[1][1] == self.__kratka[2][2] != ' ' or \
                        self.__kratka[0][2] == self.__kratka[1][1] == self.__kratka[2][0] != ' ':
                    print(f'Wygral {self.__kratka[0][j]}!!!')
                    self.__win = True
                    break

    def o(self, number: int):
        if not self.__win:
            number -= 1
            if self.__kratka[number // 3][number % 3] != ' ' or number > 8 or number < 0:
                print("Nieprawidłowa wartość!")
                return 0
            if (self.__kratka[0]).count('X') + (self.__kratka[1]).count('X') + (self.__kratka[2]).count('X') \
                    == (self.__kratka[0]).count('O') + (self.__kratka[1]).count('O') + (self.__kratka[2]).count(
                'O') + bool(self.__kolo):
                self.__kratka[number // 3][number % 3] = "O"
                self._checkwin()
            else:
                print("Nie twoj ruch!!!")

        self._checkwin()

    def x(self, number):
        if not self.__win:
            number -= 1
            if self.__kratka[number // 3][number % 3] != ' ' or number > 8 or number < 0:
                print("Nieprawidłowa wartość!")
                return 0
            if (self.__kratka[0]).count('X') + (self.__kratka[1]).count('X') + (self.__kratka[2]).count(
                    'X') + bool(self.__krzyz) == (self.__kratka[0]).count('O') + (self.__kratka[1]).count('O') + (
                    self.__kratka[2]).count('O'):
                self.__kratka[number // 3][number % 3] = "X"
            else:
                print("Nie twoj ruch!!!")
        self._checkwin()


def main():
    k1 = KolkoKrzyz('X')
    KolkoKrzyz.help()
    k1.x(5)
    k1.o(2)
    print(k1)
    k1.x(6)
    print(k1)
    k1.o(3)
    print(k1)
    k1.x(9)
    print(k1)
    k1.o(1)
    print(k1)


if __name__ == '__main__':
    main()
