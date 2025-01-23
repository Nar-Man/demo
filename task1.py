import random
import string

def generate_password(length):
    if length < 6:
        raise ValueError("Password length must be at least 6 characters.")
    digits = "0123456789"  
    lowercase = string.ascii_lowercase 
    uppercase = string.ascii_uppercase 
    special   = string.punctuation

    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special)
    ]
    all_chars = digits+lowercase+uppercase+special
    password += random.choices(all_chars, k = length -len(password))
    random.shuffle(password)
    password = ''.join(password)

    assert any(i.isdigit() for i in password)
    assert any(i.islower() for i in password)
    assert any(i.isupper() for i in password)
    assert any(i in special for i in password)
        

    return password

password = generate_password(10)
print(password)