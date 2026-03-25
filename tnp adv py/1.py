#1. Largest element in a list
lst = [10, 25, 5, 40]
largest = lst[0]
for i in lst:
    if i > largest:
        largest = i
print("Largest:", largest)

#2. Even or Odd
num = 7
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

#3. Reverse string (without slicing)
s = "hello"
rev = ""
for char in s:
    rev = char + rev
print(rev)

#4. Count vowels
s = "education"
count = 0
for char in s:
    if char in "aeiouAEIOU":
        count += 1
print("Vowels:", count)

#5. Sum of digits
num = 1234
sum_digits = 0
while num > 0:
    sum_digits += num % 10
    num //= 10
print("Sum:", sum_digits)

#6. Palindrome string
s = "madam"
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

#7. Fibonacci sequence
n = 5
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b

#8. Swap without third variable
a = 5
b = 10
a, b = b, a
print(a, b)

#9. Count words
s = "Hello world python"
words = s.split()
print("Word count:", len(words))

#10. Min and Max in list
lst = [4, 2, 9, 1]
print("Min:", min(lst))
print("Max:", max(lst))

#11. Second largest
lst = [10, 20, 5, 8]
lst.sort()
print("Second largest:", lst[-2])

#12. Remove duplicates (no set)
lst = [1, 2, 2, 3]
new = []
for i in lst:
    if i not in new:
        new.append(i)
print(new)

#13. Frequency of elements
lst = [1, 2, 2, 3]
freq = {}
for i in lst:
    freq[i] = freq.get(i, 0) + 1
print(freq)

#14. Merge two sorted lists
a = [1, 3, 5]
b = [2, 4, 6]
print(sorted(a + b))

#15. Intersection of lists
a = [1, 2, 3]
b = [2, 3, 4]
res = []
for i in a:
    if i in b:
        res.append(i)
print(res)

#16. Rotate list by k
lst = [1, 2, 3, 4, 5]
k = 2
k = k % len(lst)
print(lst[-k:] + lst[:-k])

#17. Anagram check
s1 = "listen"
s2 = "silent"
if sorted(s1) == sorted(s2):
    print("Anagram")
else:
    print("Not Anagram")

#18. First non-repeating character
s = "aabbcde"
for char in s:
    if s.count(char) == 1:
        print("First non-repeating:", char)
        break

#19. Flatten nested list
nested = [[1, 2], [3, 4], [5]]
flat = []
for sub in nested:
    for i in sub:
        flat.append(i)
print(flat)

#20. Pairs with given sum
lst = [1, 2, 3, 4]
target = 5
for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        if lst[i] + lst[j] == target:
            print(lst[i], lst[j])

#21. Right triangle pattern
n = 5
for i in range(1, n+1):
    print("*" * i)

#22. Pyramid pattern
n = 5
for i in range(1, n+1):
    print(" "*(n-i) + "*"*(2*i-1))

#23. Prime numbers in range
start, end = 1, 20
for num in range(start, end+1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num, end=" ")

#24. Armstrong number
num = 153
temp = num
sum_val = 0
digits = len(str(num))

while temp > 0:
    digit = temp % 10
    sum_val += digit ** digits
    temp //= 10

if sum_val == num:
    print("Armstrong")
else:
    print("Not Armstrong")