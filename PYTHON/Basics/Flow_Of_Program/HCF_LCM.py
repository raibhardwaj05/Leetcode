# Take 2 numbers as inputs and find their HCF and LCM.
def hcf_lcm(num1, num2):
    a = num1
    b = num2
    while num2 > 0:
        remainder = num1 % num2
        num1 = num2
        num2 = remainder

    hcf = num1
    print(f"HCF of {a, b} is {hcf}")

    lcm = int((a * b)/hcf)
    print(f"LCM of {a, b} is {lcm}")

hcf_lcm(48, 18)