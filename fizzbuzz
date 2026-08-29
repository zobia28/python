print("Welcome to FizzBuzz!")

def fizzbuzz(number):
    result = ""
    if number % 3 == 0:
        result += "Fizz"
    if number % 7 == 0:
        result += "Buzz"
    if result == "":
        if "3" in str(number):
            result = "Almost Fizz"
        else:
            result = str(number)
    return result

limit = int(input())

# Play FizzBuzz
for i in range(1, limit + 1):
    print(fizzbuzz(i))
