def check_password(s):
    if len(s) < 8:
        return False

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    for c in s:
        if c.isupper():
            has_upper = True
        elif c.islower():
            has_lower = True
        elif c.isdigit():
            has_digit = True
        elif c in string.punctuation:
            has_special = True

    return has_upper and has_lower and has_digit and has_special

user_ps = input("Enter a strong password: ")
if check_password(user_ps):
    print("Password Accepted.")
else:
    print("The passwors does NOT meet all the criteria.")