import random

def generate_password(length):
    if length < 6:
        print("Password length must be at least 6 characters.")
        return None
    digits = "0123456789"  
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    symbols  = "!@#$%^&*()"
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(symbols)
    ]
    all_chars = digits+lowercase+uppercase+symbols
    
    password += random.choices(all_chars, k=length - 4)
    random.shuffle(password)
    password = ''.join(password)
    assert any(i.isdigit() for i in password)
    assert any(i.islower() for i in password)
    assert any(i.isupper() for i in password)
    assert any(i in symbols for i in password)
    
    return ''.join(password)

def validate_password(password):
    errors = []
    if len(password) < 6:
        errors.append("Password must be at least 6 characters long.")
    if not any(i.isupper() for i in password):
        errors.append("Password must contain at least one uppercase letter.")
    if not any(i.islower() for i in password):
        errors.append("Password must contain at least one lowercase letter.")
    if not any(i.isdigit() for i in password):
        errors.append("Password must contain at least one digit.")
    if not any(i in "!@#$%^&*()" for i in password):
        errors.append("Password must contain at least one character (!@#$%^&*()).")

    return errors