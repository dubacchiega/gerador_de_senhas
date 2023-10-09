import string as s
from secrets import SystemRandom as Sr


def password_gen(key):
    random = Sr()
    letters = s.ascii_letters
    numbers = s.digits
    punctuation = s.punctuation

    all_together = letters + numbers + punctuation
    password = random.choices(all_together, k=key)

    password = ''.join(password)
    return password


password1 = password_gen(8)
print(password1)

password2 = password_gen(12)
print(password2)
