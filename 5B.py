def is_power_of_two(n,count):
    if n == 1:
        return True
    elif n > 0:
        if n % 2 == 0:
            return is_power_of_two(n/2, count+1)
        else:
            return False
