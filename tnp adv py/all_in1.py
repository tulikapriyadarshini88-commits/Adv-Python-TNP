# Input statement
# Decision-making statements
# Control statements 

num = int(input("Enter a number: "))   # Input statement

if num > 0:                           # Decision-making (if)
    print("Number is Positive")

elif num == 0:                        # Decision-making (elif)
    print("Number is Zero")

else:                                 # Decision-making (else)
    print("Number is Negative")


print("\nPrinting numbers from 1 to", num)

for i in range(1, num + 1):           # Loop (control statement)
    
    if i == 5:
        continue                      # Control statement (skip 5)

    if i == 10:
        break                         # Control statement (stop loop at 10)

    print(i)