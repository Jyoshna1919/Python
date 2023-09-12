# Recursion examples

def tri_recursion(k):
    if(k>0):
        result = k+tri_recursion(k-1)
        print(result)
    else:
        result=0
    return result
print("\n\nrecursion Example Results")
tri_recursion(5)


def sum(list):
    sum=0
    for i in range(len(list)):
        sum=sum+list[i]
    return sum
print(sum([5,7,6,8,9]))

def factorial(x):
    if x==1:
        return 1
    else:
        return x * factorial(x-1)
print(factorial(3000))                 #OP:maximum recursion depth exceeded

#lamda function
x=lambda a: a+10
print(x(5))

x=lambda a,b:a**b
print(f'square of x is{x(5,6)}')

x=lambda num: num*5
print(x(5))

#Filter() Functions

def find_even(num):
    return num%2 ==0

numbers=[1,2,3,4,5,6,7,8]
even_list=list(filter(find_even, numbers))
print(even_list)

def find_odd(num):
    return num%2 !=0

numbers=[1,2,3,4,5,6,7,8]
odd_list=list(filter(find_odd, numbers))
print(odd_list)

def sum(num)
    return num==0

numbers=[1,2,3,4,5,6,7,8]
new_list=filter(lambda(num: num+numbers))
print(newlist(5))


def check(letter):
    list_of_vowels=['a','e','i','o','u']
    if letter in list_of_vowels:
        return True
    else:
        return False
letters=['u','a','q','c','i','d','z','p','e']
filter_object=filter(check,letters)
print("the of returned object is:",type(filter_object))
filtered_list=list(filter_object)
print("the list of vowels:",filtered_list)


    
