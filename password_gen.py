import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
easy=input("Should password be easy or tough?\nPress e for easy and d for difficult\n")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


le_gen=random.sample(letters,nr_letters)
sy_gen=random.sample(symbols,nr_symbols)
num_gen=random.sample(numbers,nr_numbers)

if easy=="e":
    password=""
    for char in range(0,nr_letters):
        password+=random.choice(letters)
    for symbol in range(0,nr_symbols):
        password+=random.choice(symbols)
    for number in range(0,nr_numbers):
        password+=random.choice(numbers)
    print(password)

elif easy=="d":
    password_list=[]
    for char in range(0,nr_letters):
        password_list+=random.choice(letters) # or u can use append
    for symbol in range(0,nr_symbols):
        password_list+=random.choice(symbols)
    for number in range(0,nr_numbers):
        password_list+=random.choice(numbers)
# print(password_list)
    random.shuffle(password_list)
# print(password_list)

    final=""
    for char in password_list:
        final+=char

    print(final)
else:
    print("Invalid selection\n")
