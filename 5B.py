def is_power_of_two(n,count):
    if n == 1:
        return True
    elif n > 0:
        if n % 2 == 0:
            return is_power_of_two(n/2, count+1)
        else:
            return False
parity_position = []
parity_value = []
code = list(input("enter the code:"))
code = [int(x) for x in code]
for i in range(len(code)):
    if is_power_of_two(i, 0):
        parity_position.append(i)
for parity in parity_position:
    value = 0
    for i in range(parity-1, len(code), 2*parity):
        for j in range(0, parity):
            value += code[j+i]
    parity_value.append((value-code[parity-1]) % 2)
for i in range(len(parity_position)):
    print(f"p{i+1} = {parity_value[i]}")
