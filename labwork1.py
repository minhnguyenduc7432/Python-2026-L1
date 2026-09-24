import math

def exercise_1():
    radius = float(input("Enter circle radius? "))
    area = 3.14 * radius ** 2
    print(f"Circle area = {area}")

def exercise_2():
    c = float(input("Enter the temperature in Celsius? "))
    f = c * 9/5 + 32
    print(f"{c} (C) = {f} (F)")

def exercise_3():
    n = int(input("Enter a number? "))
    if n < 2:
        print(f"{n} is a NOT prime number")
        return
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print(f"{n} is a NOT prime number")
            return
    print(f"{n} is a prime number")

def exercise_4():
    n = int(input("Enter a number? "))
    if n <= 0:
        print(f"{n} is a NOT perfect number")
        return
    sum_divisors = sum(i for i in range(1, n) if n % i == 0)
    if sum_divisors == n:
        print(f"{n} is a perfect number")
    else:
        print(f"{n} is a NOT perfect number")

def exercise_5():
    colors = ["Blue", "Yellow", "Black", "Red", "White"]
    favorite = input("What is your favorite color? ")
    if favorite in colors:
        print(f"Your colod is at index {colors.index(favorite)} in my list")
    else:
        print("Sorry, I could not find your color")

def exercise_6():
    range1 = list(range(7))
    range2 = list(range(1, 11, 3))
    range3 = list(range(5, 0, -1))
    range4 = list(range(6, -3, -2))
    print("range1", range1)
    print("range2", range2)
    print("range3", range3)
    print("range4", range4)

def remove_dollar_sign(s):
    return s.replace("$", "")

def exercise_7():
    s = input("Enter a string: ")
    print(remove_dollar_sign(s))

def extract_even(l):
    return [num for num in l if num % 2 == 0]

def exercise_8():
    print(extract_even([1, 4, 5, -1, 10]))

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def exercise_9():
    n = int(input("Enter a non-negative integer: "))
    print(factorial(n))

def get_divisors(n):
    return [i for i in range(1, n + 1) if n % i == 0]

def exercise_10():
    n = int(input("Enter a number: "))
    print(get_divisors(n))

def distance_between_points(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def exercise_11():
    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y1: "))
    x2 = float(input("Enter x2: "))
    y2 = float(input("Enter y2: "))
    print(distance_between_points(x1, y1, x2, y2))

def print_pattern(m, n):
    for i in range(m):
        for j in range(n):
            if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                print("*", end="   ")
            else:
                print(" ", end="   ")
        print()

def exercise_12():
    m = int(input("Enter m (rows): "))
    n = int(input("Enter n (cols): "))
    print_pattern(m, n)