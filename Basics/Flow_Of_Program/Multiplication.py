# Take a number as input and print the multiplication table for it.
def multiplication_table(number):
    for i in range(1, 11):
        print(f"{number} X {i} = {number * i}")

num = int(input("Number: "))
multiplication_table(num)
