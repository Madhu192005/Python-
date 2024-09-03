import re
def check_password_strength(password):
    checks={
        "length": len(password)>=.8,
        "uppercase":bool(re.search(r'[A-Z]',password)),
        "lowercase":bool(re.search(r'[a-z]',password)),
        "digit": bool(re.search(r'\d',password)),
        "special":bool(re.search(r'[!@#$%^&*(),.?:{}|<>]',password))
        }
    strength = sum(checks.values())
    strength_messages = [
        "very weak password",
        "weak password",
        "Fair password",
        "Moderately strong password",
        "Strong password"
        ]
    return strength_messages[strength]
password=input("Enter your password: ")
print(check_password_strength(password))
