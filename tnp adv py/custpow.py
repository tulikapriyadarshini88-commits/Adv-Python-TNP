def power(base, exp):
    result = 1
    for i in range(exp):
        result *= base
    return result

print(power(2, 3))