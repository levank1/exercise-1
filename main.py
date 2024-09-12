
# --------------exercise 1--------------
number1 = int(input("Please enter number 1: "))
number2 = int(input("Please enter number 2: "))
number3 = int(input("Please enter number 3: "))

print('Sum of this numbers are : ', number1+ number2 + number3)

# --------------exercise2--------------

side_length = int(input('Please enter length of the side of the cube : '))
v = side_length ** 3
s = 6 * (side_length ** 2)
print("V :", v , " S :", s)


# --------------exercise 3--------------


monitor = float(input("Please enter monitor price : "))
systemBlock = float(input("Please enter system block price : "))
keyboard = float(input("Please enter keyboard price : "))
mouse = float(input("Please enter mouse price : "))

totalPrice = monitor + systemBlock + keyboard + mouse

print("Total Price :", totalPrice);

