#Python Program to add two number using recursion
number = int(input("Enter the Number:"))
sum = 0
for value in range(1, number + 1):
    sum = sum + value
print(sum)



#Python Program to merge two arrays
array1 = [1,2,3,4]
array2 = [5,6,7,8]
for item in array2:
    array1.append(item)
print(array1)



#Python Program to find sum of array elements
number = int(input("Enter the Number: "))
sum = 0
for value in range(1, number +1):
    sum = sum + value
print(sum)



#4.average of givem num
numbers = [1, 2, 34, 56, 7, 23, 23, 12, 1, 2, 3, 34, 56]
sumOfNums = 0
count = 0
for number in numbers:
    sumOfNums += number
    count += 1
average = sumOfNums / count
print("The list of numbers is:", numbers)
print("The average of all the numbers is:", average)



#5.swap two numbers without using third variable
n1=int(input('enter number 1'))
n2=int(input('enter number 2'))
print('numbers before swapping',n1,n2)
n1,n2=n2,n1
print('swapped numbers= ',n1,n2)



#6. print prime factors of a given number
def prime(num):
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count+=1
    return (True if (count==2) else False)

num=int(input('enter your number'))
for i in range(1,num+1):
    if num%i==0 and prime(i):
        print(i)


#7.python program to print fibonocci numbers using iterative method
num=int(input('enter your number of fabnoccis series'))
n1,n2=0,1
for i in range(num+1):
    if i<2:
        print(i)
    else:
        print(n1+n2)
        n1,n2=n2,n1+n2



#8.Anagrams
string1=input("enter any string")
string2=input("enter any string")
if len(string1)!= (string2):
    print("this is anagrams")
else:
    if sorted(string1) == sorted(string2):
       print("this is anagrams")
    else:
        print("this is not anagrams")


#9.printing specialcharacters,digits,alphabets
string=input("enter any string=")
alphabets=0
digits=0
special_characters=0
for i in string:
    if i.isalpha():
        alphabets+=1
    elif i.isdigit():
        digits+=1
    else:
        special_characters+=1
print("alphabets",alphabets,"digits",digits,"special_characters")
