def start():
    while True:
        user_from = int(input("\n1. Celsius\n2. Fahrenheit\n3. Kelvin\nConvert from: "))
        if user_from == 1:
            from_c()
            break
        elif user_from == 2:
            from_f()
            break
        elif user_from == 3:
            from_k()
            break
        else:
            print("Invalid input! Try again...")


def from_c():
    while True:
        user_to = int(input("\n1. Fahrenheit\n2. Kelvin\nConvert to: "))
        if user_to == 1:
            print(f"{user_num} °C = {(user_num * 9 / 5) + 32} °F")
            break
        elif user_to == 2:
            print(f"{user_num} °C = {user_num + 273.15} K")
            break
        else:
            print("Invalid input! Try again...")


def from_f():
    while True:
        user_to = int(input("\n1. Celsius\n2. Kelvin\nConvert to: "))
        if user_to == 1:
            print(f"{user_num} °F = {(user_num - 32) * 5 / 9} °C")
            break
        elif user_to == 2:
            print(f"{user_num} °F = {(user_num - 32) * 5 / 9 + 273.15} K")
            break
        else:
            print("Invalid input! Try again...")


def from_k():
    while True:
        user_to = int(input("\n1. Celsius\n2. Fahrenheit\nConvert to: "))
        if user_to == 1:
            print(f"{user_num} K = {user_num - 273.15} °C")
            break
        elif user_to == 2:
            print(f"{user_num} K = {(user_num - 273.15) * 9 / 5 + 32} °F")
            break
        else:
            print("Invalid input! Try again...")


user_num = float(input("Enter temperature you want to convert: "))
if __name__ == '__main__':
    start()
