lst = ["hello", "madam", "python", "racecar"]

lst.sort(key=len)
print("Sorted:", lst)

pal = [x for x in lst if x == x[::-1]]
print("Palindromes:", pal)

new = [x.replace(" ", "-") for x in lst]
print("Replaced:", new)