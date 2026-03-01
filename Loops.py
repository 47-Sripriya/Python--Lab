# Q1. Sum of Digits

n = int(input("Enter a number: "))
sum_digits = 0
while n > 0:
    digit = n % 10
    sum_digits += digit
    n = n // 10
print("Sum of digits:", sum_digits)


# Q2. Reverse a Number

n = int(input("Enter a number: "))
reverse = 0
while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10
print("Reversed number:", reverse)


# Q3. Armstrong Number

n = int(input("Enter a number: "))
temp = n
sum = 0
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp = temp // 10
if sum == n:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
  
# Q4. Fibonacci Series

n = int(input("Enter how many numbers: "))
a = 0
b = 1
for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c


# Q5. Prime Count

n = int(input("Enter a number: "))
count = 0
for num in range(2, n+1):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        count += 1
print("Total prime numbers:", count)
