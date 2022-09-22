num = input("enter the range: ")

try:
    num = int(num) + 1
    for index in range(1, num):
        if index % 3 == 0 and index % 5 == 0:
            print("FizzBuzz")
        elif index % 3 == 0:
            print("Fizz")
        elif index % 3 == 0:
            print("Buzz")
        else:
            print(index)
except ValueError:
    print("please try again and enter a number")
