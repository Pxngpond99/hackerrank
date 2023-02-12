def FizzBuzz(x):
    if int(x) % 3 == 0 and int(x) % 5 == 0:
        return "FizzBuzz"
    elif int(x) % 3 == 0:
        return "Fizz"
    elif int(x) % 5 == 0:
        return "Buzz"