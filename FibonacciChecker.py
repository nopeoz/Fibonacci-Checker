# Fibonacci up to 100

number = input("Enter a value to check: ")
try:
    number1 = number.strip()
except AttributeError:
    # data is not a string, can't strip
    number1 = number
try:
    valid = number1.isnumeric()
except AttributeError:
    # data is an int
    valid = True

if valid is False:
    print("Please enter a positive integer!")

else:
    x = int(number)
    i = 1
    y = 1
    a = 0
    b = 0
    if x == 0:
        print(x, 'is part of the Fibonacci sequence!')
    else:

        # fibonacci pattern


        while a < x:
            b = y
            y = a + y
            a = b
            if y == x:
                print(x, 'is part of the Fibonacci sequence!')
                break
            elif y > x:
                print(x, 'is not part of the Fibonacci sequence!')
                break
        else:
            i += 1

k = input('Press anything to exit')
