#Python Program to count occurrence of a given characters in string
string = input("enter your own String : ")
char = input(" enter your own Character :")
string2 =''
length = len(string)
for i in range(length):
    if(string[i] == char):
        string2 = string[0:i] + string[i+1:length]
print("Original String: ",string)
print("Final String: ",string2)


#Python program to check a String is palindrome or not
def is_palindrome(s):
    s = s.lower()
    reversed_s=s[::-1]
    return s == reversed_s
print(is_palindrome('racecar'))
print(is_palindrome('python'))

#Python program to check given character is digit or not
ch=input("Enter Your Own Character : ")
if(ch.isdigit()):
    print("The Given Character ", ch, "is a Digit")
else:
    print("The Given Character ", ch, "is Not a Digit")


#Python program to count alphabets, digits and special characters
str1 = input("Please Enter Your Own String : ")
alphabets = digits = special = 0
for i in range(len(str1)):
    if((str1[i] >= 'a' and str1[i] <= 'z') or (str1[i] >= 'A' and str1[i] <= 'Z')):
        alphabets = alphabets + 1
    elif(str1[i] >'0' and str1[i] <= '9'):
        digits = digits + 1
    else:
        special = special +1
print("\nTotal Number of Alphabets in this String : ", alphabets)
print("Total Number of Digits in this String : ", digits)
print("Total Number of Special Characters in this String : ", special)



#Python program to find sum of n numbers
number = int(input("Enter the Number: "))
sum = 0
for value in range(1, number + 1):
    sum = sum + value
print(sum)


#Python program to copy one string to another string
str1 = input("please Enter Your Own String : ")
str2 = str1
str3 = str1[:]
print("The Final String : Str2 = ", str2)
print("The Final String : str3==", str3)



#Python program to delete vowels in a given string
def removeVowels(s):
    res = ''
    s = s.lower()
    print(s)
    for i in s:
        if(i != 'a' and i != 'e' and i !='i' and i !='o' and i != 'u'):
            res = res + i
    print(res)
inputTest = input("Enter a string")
removeVowels(inputTest)



#Python program to concatenate two strings
str1 = input("Enter the First String : ")
str2 = input("Enter the Second string : ")
concat1 = str1 + str2
print("The Final String After Python Concatenation = ", concat1)
concat2 = str1 + ' ' + str2
print("The Final After String Concatenation with Space = ", concat2)


#Python Program to sort string in ascending order and descending order
s = 'acedbgf'
s_list=list(s)
print(s_list)

#Sorting in ascending order:
a_sort=sorted(s_list)
a_str=''.join(a_sort)
print(a_str)

#sorting in decending order:
d_sort=sorted(s_list,reversed=True)
d_str=''.join(d_sort)
print(d_str)


#Python program to print the highest frequency character in string
string = input("enter the your own string = ")
chardict = {}
for num in string:
    keys = chardict.keys()
    if num in keys:
        chardict[num] = chardict[num] + 1
    else:
        chardict[num] = 1
print(chardict)
