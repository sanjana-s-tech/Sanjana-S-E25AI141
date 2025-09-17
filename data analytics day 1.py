import re
# Password Strength Checker using String Manipulation
def check_password_strength(password):
    length = len(password)
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    special_characters = "!@#$%^&*()-+?_=,<>/"

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_characters:
            has_special = True

    score = 0
    if length >= 8:
        score += 1
    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_digit:
        score += 1
    if has_special:
        score += 1

    if score == 5:
        return "Strong password"
    elif 3 <= score < 5:
        return "Medium password"
    else:
        return "Weak password"

# User input
password = input("Enter your password: ")
result = check_password_strength(password)
print("Password Strength:",result)
