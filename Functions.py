# Q6. Even or Odd Function

def check_even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"
num = int(input("Enter a number: "))
result = check_even_odd(num)
print("The number is:", result)


# Q7. Factorial Function

def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact
num = int(input("Enter a number: "))
print("Factorial is:", factorial(num))


# Q8. Largest of Three

def largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))
print("Largest number is:", largest(x, y, z))


# Q9. Count Vowels

def count_vowels(text):
    count = 0
    vowels = "aeiouAEIOU"
    
    for ch in text:
        if ch in vowels:
            count += 1
    return count
string = input("Enter a string: ")
print("Number of vowels:", count_vowels(string))

# Q10. Simple Calculator

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

print("1.Add 2.Subtract 3.Multiply 4.Divide")
choice = int(input("Enter choice (1-4): "))

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == 1:
    print("Result:", add(num1, num2))
elif choice == 2:
    print("Result:", sub(num1, num2))
elif choice == 3:
    print("Result:", mul(num1, num2))
elif choice == 4:
    print("Result:", div(num1, num2))
else:
    print("Invalid Choice")
