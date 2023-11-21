#Write a program in Python to check whether an integer is Armstrong number or not using list comprension
num = int(input("enter any number:"))
digits = [int(digit) for digit in str(num)]
count = len(digits)
sum = sum([digit ** count for digit in digits])
if num == sum:
    print("given",num, "is an armstrong number:")
else:
    print("given",num,"is not armstrong number")


#Write a program in Python to find greatest among three integers 
def find_max(a,b,c):
    return max(a,b,c)
print(find_max(23, 24, 29))
print(find_max(45, 33, 47))
print(find_max(12, 12, 11))


#Write a program to reverse an integer in Python
def reverse_number(n):
    reversed_number = 0
    while n > 0:
        last_digit = n % 10
        reversed_number = reversed_number * 10 + last_digit
        n = n // 10
    return reversed_number
number = int(input("Enter a number:"))
print("Reversed number: ", reverse_number(number))

#Write a program in Python to check whether a number is palindrome or not using iterative method
n = int(input("enter any number:"))
reverse,temp=0,n
while temp!=0:
    reverse=reverse*10 + temp%10;
    temp=temp//10;
if reverse==n:
    print("number is palindrome:")
else:
    print("number is not palindrome")


#Write a program in Python to print the Fibonacci series using iterative method
def fib(number):
    count = 0
    first = 0
    second = 1
    temp = 0
    while count <= number:
        print(first)
        temp = first + second
        first = second
        second = temp
        count = count + 1
fib(6)


#Write a program in Python to find sum of digits of a number using recursion
num = int(input("Enter a number: "))
def sum(n):
    if n <= 1:
        return n
    else:
        return n + sum(n-1)
    print("The sum is: ", sum(num))









