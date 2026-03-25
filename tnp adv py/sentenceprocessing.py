s = input("Enter a sentence: ")

vowels = "aeiouAEIOU"
v = c = 0

for ch in s:
    if ch.isalpha():
        if ch in vowels:
            v += 1
        else:
            c += 1

print("Vowels:", v)
print("Consonants:", c)
print("Reverse:", s[::-1])
print("Underscore:", s.replace(" ", "_"))
print("Capitalized:", s.title())