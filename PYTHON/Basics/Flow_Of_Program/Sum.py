# Keep taking numbers as inputs till the user enters ‘x’, after that print sum of all.
cont = True
total = 0
print("Enter 'x' to exit!\n")
while cont:
    number = input("Enter Value: ")

    if number.isdigit():
        total += int(number)
    elif number == "x":
        cont = False


print(f"Sum: {total}")

