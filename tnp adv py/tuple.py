t = (1, "a", 3.5, 7, "hello")

nums = [x for x in t if isinstance(x, (int, float))]
print("Numeric values:", nums)

try:
    t[0] = 100
except TypeError:
    print("Tuple cannot be modified")

t2 = (9, 10)
print("Concatenated:", t + t2)