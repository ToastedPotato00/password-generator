import random
variable = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
pass_length = int(input("masukan panjang password yang di mau "))
password = []
for i in range (pass_length):
    random_key = random.randrange(0, 72)
    password_data = variable[random_key]
    password.append(password_data)
x = "".join(password)
print(x)
