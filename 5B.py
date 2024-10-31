def is_power_of_two(n,count):
    if n == 1:
        return True
    elif n > 0:
        if n % 2 == 0:
            return is_power_of_two(n/2, count+1)
        else:
            return False
parity_position = []
code = list(input("enter the code:"))
code = [int(x) for x in code]
for i in range(len(code)):
    if is_power_of_two(i, 0):
        parity_position.append(i)
