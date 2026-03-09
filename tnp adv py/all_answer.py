if True:
    print("Indentation example")


# 6. if statement
x = 10
if x > 5:
    print("x > 5")

# 7. if-else
if x % 2 == 0:
    print("Even")
else:
    print("Odd")

# 8. if-elif-else
marks = 70
if marks >= 90:
    print("A")
elif marks >= 60:
    print("B")
else:
    print("C")

# 9. Nested if-else
num = 15
if num > 0:
    if num % 2 == 0:
        print("Positive Even")
    else:
        print("Positive Odd")

# 11. Loops
# while loop
i = 1
while i <= 3:
    print("While:", i)
    i += 1
else:
    print("While ended")

# for loop
for i in range(1, 4):
    print("For:", i)

# for with else
for i in range(3):
    print(i)
else:
    print("For ended")

# for with sequence
for ch in "Python":
    print(ch)

# nested for loop
for i in range(2):
    for j in range(2):
        print(i, j)

# 12. break & continue
for i in range(1, 6):
    if i == 3:
        continue
    if i == 5:
        break
    print(i)
# 13–18. Functions

def greet():
    print("Hello")

greet()

def add(a, b):
    return a + b

print(add(5, 3))

# 19–21. Scope

g = 10  # global
def show():
    print(g)

show()

def outer():
    x = 5
    def inner():
        nonlocal x
        x += 1
        print(x)
    inner()

outer()


# 22. Passing collection
def show_list(lst):
    for i in lst:
        print(i)

show_list([1, 2, 3])

# 23. Types of arguments
def demo(a, b=2):
    print(a, b)

demo(5)
demo(5, 10)

# 24. Variable length arguments
def total(*nums):
    return sum(nums)

print(total(1, 2, 3))

# 25. Nested function
def outer_fun():
    def inner_fun():
        print("Inner")
    inner_fun()

outer_fun()

# 26. Recursive function
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))

# 27. Function as argument
def square(x):
    return x * x

def apply(func, val):
    return func(val)

print(apply(square, 4))


# 30. Sum, subtraction, multiplication
def operations(a, b):
    return a + b, a - b, a * b

print(operations(10, 5))

# 31. Attendance
def attendance(roll):
    present = [1, 2, 3]
    return "Present" if roll in present else "Absent"

print(attendance(2))

# 32. Maximum of three
def max_three(a, b, c):
    return max(a, b, c)

# 33. Even or odd
def even_odd(n):
    return "Even" if n % 2 == 0 else "Odd"

# 34. Vowels and consonants
def count_vowels(word):
    v = c = 0
    for ch in word:
        if ch in "aeiouAEIOU":
            v += 1
        else:
            c += 1
    return v, c

# 35. Factorial
def fact(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f

# 36. Lowercase to uppercase
def to_upper(word):
    return word.upper()

# 37. Area of circle
def area_circle(r):
    return 3.14 * r * r
# 42. Factorial using if-else
n = 5
if n < 0:
    print("Invalid")
else:
    print(fact(n))

# 43. Reverse number
num = 123
rev = 0
while num > 0:
    rev = rev * 10 + num % 10
    num //= 10
print(rev)

# 44. Descending natural numbers
n = 5
while n > 0:
    print(n)
    n -= 1

# 45. First 7 multiples of 7
for i in range(1, 8):
    print(7 * i)

# 46. Square list
lst = [1, 2, 3, 4]
sq = []
for i in lst:
    sq.append(i * i)
print(sq)

# 47. Positive & Negative
nums = [1, -2, 3, -4]
pos, neg = [], []
for i in nums:
    if i >= 0:
        pos.append(i)
    else:
        neg.append(i)
print(pos, neg)

# 48. Even & Odd list
even, odd = [], []
for i in nums:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print(even, odd)

# 49. Prime number
n = int(input("Enter number: "))
prime = True
for i in range(2, n):
    if n % i == 0:
        prime = False
        break
print("Prime" if prime and n > 1 else "Not Prime")

# 50. Pythagorean Triplets
limit = 20
for a in range(1, limit):
    for b in range(a, limit):
        for c in range(b, limit):
            if a*a + b*b == c*c:
                print(a, b, c)