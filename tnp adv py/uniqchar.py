s = input("Enter sentence: ")

freq = {}
for ch in s:
    if ch.isalnum():
        freq[ch] = freq.get(ch, 0) + 1

for k, v in freq.items():
    if v == 1:
        print(k, end=" ")