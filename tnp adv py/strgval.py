s = input("Enter string: ")

print("Palindrome" if s == s[::-1] else "Not palindrome")

v = c = d = sp = 0
for ch in s:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            v += 1
        else:
            c += 1
    elif ch.isdigit():
        d += 1
    else:
        sp += 1

print(v, c, d, sp)