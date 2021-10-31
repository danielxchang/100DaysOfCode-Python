for num in range(1, 101):
    fizz = "Fizz"
    buzz = "Buzz"
    div_3 = num % 3 == 0
    div_5 = num % 5 == 0
    if div_3 and div_5:
        print(fizz + buzz)
    elif div_3:
        print(fizz)
    elif div_5:
        print(buzz)
    else:
        print(num)
