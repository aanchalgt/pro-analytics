def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

while True:
    try:
        num = int(input("Enter a number: ").strip())
        break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

print(factorial(num))
