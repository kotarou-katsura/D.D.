
class Hamming:
    def __init__(self):
        self.get_code()
        self.parity_value = []
        self.parity_position = []
        self.error_index_b = 0
        self.error_index_d = 0
        self.list_parity_positions()
        self.find_parity_value()


    def get_code(self):
        self.code = list(input("enter the code:"))
        self.code = [int(x) for x in self.code]
        if len(self.code)!=16:
            print("the length is not valid!")
            self.get_code();

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

    def find_error(self):
        for i in range(len(self.parity_position) - 1, -1, -1):
            if self.code[self.parity_position[i] - 1] != self.parity_value[i]:
                self.error_index_b += 1
            if i != 0:
                self.error_index_b *= 10
        self.error_index_d = int(str(self.error_index_b), 2)
        print(f"the error find in position {self.error_index_d}")
        print("the corrected code is:", end=" ")
        print("the corrected code is:", end=" ")
        for i in range(len(self.code)):
            if i == self.error_index_b - 1:
                if self.code[i] == 0:
                    self.code[i] = 1
                else:
                    self.code[i] = 0
            print(self.code[i], end="")


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
h1.find_error()
