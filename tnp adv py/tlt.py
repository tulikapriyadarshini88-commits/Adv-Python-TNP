t = (5, 15, 3, 20, "hi")

lst = list(t)
lst = [x for x in lst if not (isinstance(x, int) and x < 10)]

t = tuple(lst)
print("Result:", t)