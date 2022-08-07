number = int(input("please inter a six-digit number:"))
a = (number % 100)//10
b = (number % 100000)//10000
sum_digits= a+b
print("The sum of the second and fifth digits of the number is:", sum_digits)