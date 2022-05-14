user_input = input("Введите целое положительное число: ")
biggest_number = 0
index = 0
while index < len(user_input):
    if (int(user_input[index]) > int(biggest_number)):
        biggest_number = user_input[index]
    index += 1
print("Максимальная цифра в числе это:", biggest_number)
