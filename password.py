import random
import string

lower = string.ascii_lowercase
upper = string.ascii_uppercase
symbols = "~!@#$%^&*()+|}{?"
numbers = "0123456789"
all_chars = lower + upper + symbols + numbers

while True:
    print("Choose your option:\n\t1) Create a password\n\t2) Exit")
    choice = input("Choose your option: ")

    if choice == "1":
        length = int(input("Length of password: "))
        password = "".join(random.sample(all_chars, length))
        print("Your password:", password)

    elif choice == "2":
        break

    else:
        print("Your choice is wron")