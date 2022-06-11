import string
import random


alphabets = list(string.ascii_letters)
digits = list (string.digits)
characters = list (string.ascii_letters + string.digits + "@")

def generate_random_password():
    length = int (input("Şifre Uzunluğu: "))

    alphabets_count = int(input("Ne kadar harf: "))
    digits_count = int(input("Ne kadar rakam: "))

    characters_count = alphabets_count + digits_count 

    if characters_count > length:
        print("Karakterlerin toplam sayısı şifre uzunluğundan büyük")
        return

    password = []

    for i in range(alphabets_count):
            password.append(random.choice(alphabets))


    for i in range(digits_count):
            password.append(random.choice(digits))

    if characters_count < length:
        random.shuffle(characters)
        for i in range(length - characters_count):
            password.append(random.choice(characters))


    random.shuffle(password)

    print("".join(password))



generate_random_password()

