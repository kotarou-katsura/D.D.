
class Hamming:
    def __init__(self):
        self.get_code()
        self.parity_value = []
        self.parity_position = []
        self.list_parity_positions()
        self.find_parity_value()

    def get_code(self):
        self.code = list(input("enter the code:"))
        self.code = [int(x) for x in self.code]

    def list_parity_positions(self):
        for i in range(len(self.code)):
            if is_parity(i):
                self.parity_position.append(i)

    def print_parity(self):
        for i in range(len(self.parity_position)):
            print(f"p{pow(2,i)} = {self.parity_value[i]}")

    def find_parity_value(self):
        for parity in self.parity_position:
            value = 0
            for i in range(parity - 1, len(self.code), 2 * parity):
                for j in range(0, parity):
                    value += self.code[j + i]
            self.parity_value.append((value - self.code[parity - 1]) % 2)


def is_parity(n):
    if n == 1:
        return True
    if n > 0:
        if n % 2 == 0:
            return is_parity(n / 2)
        else:
            return False
    else:
        return False
h1=Hamming()
h1.print_parity()
