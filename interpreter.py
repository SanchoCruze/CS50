answer = input("Enter equation: ")

x_num, operator, z_num = answer.strip().split()

x = int(x_num)
z = int(z_num)

if operator == "+":
    result = x + z
elif operator == "-":
    result = x - z
elif operator == "*":
    result = x * z
elif operator == "/":
    result = x / z
else:
    raise ValueError("Invalid operator")

print(f"{result:.1f}")
