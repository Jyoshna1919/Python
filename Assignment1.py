#membership operator using in and not in
a = "jyoshna"
string_a = "hlo jyoshna"
if (a in string_a):
    print("True")
else:
    print("False")  # using in method
a = "jyoshna"
string_a = "hlo jyoshna"
if (a not in string_a):
    print("True")
else:
    print("False") # using not in method  


#removeing spaces from string
s=" iam from Andhra pradesh "
print(len(s))
after_strip=s.strip()
print(after_strip)
print(len(after_strip))
s=" iam from karnataka "
print(len(s))
after_strip=s.rstrip()
print(after_strip)
print(len(after_strip))


#compare of two strings

a="jyoshna"
b="sai"
print(a>b)
print(b>a)
s=("$jyoshna")
s1=("$teja")
print(s==s1)
print(s<=s1)
sa="1 3 4"
sb="2 3 6"
print(sa>=sb)
print(sb>sa)
print("------------------------------------------")


#finding the substring by using index
str= "hello my name is maximus derimous python"
print(str.index('name'))
str= "hello my name is maximus dermious python"
print(str.index('m'))
str= "hello my name is maximus derimous python"
print(str.index('python'))
print("-----------------------------------")


#find the substring of rindex
str= "hello my name is maximus derimous python"
print(str.rindex('name'))
str= "hello my name is maximus derimous python"
print(str.rindex('m'))
str= "hello my name is maximus derimous python"
print(str.rindex('python'))
print("------------------------------------------")


#find the substring using find(it will show first occurence)
str= "hello my name is maximus derimous python"
print(str.find('name'))
str= "hello my name is maximus derimous python"
print(str.find('m'))
str= "hello my name is maximus derimous python"
print(str.find('python'))
print("-----------------------------------------------")


#find the substring using rfind
str= "hello my name is maximus derimous python"
print(str.rfind('name'))
str= "hello my name is maximus derimous python"
print(str.rfind('python'))
print("---------------------------------------")


#replace the string using replace method
str="i am bad at python"
print(str.replace("bad","good"))
str="iam not intelligent"
print(str.replace("not intelligent","intelligent"))
str="iam cricket player"
print(str.replace('cricket','football'))
print('--------------------------------------------')


#splitting the string
#example 1
sentence = "hi to all i am jyoshna"
split_sentence = sentence.split(" ")
print(split_sentence)
#example 2
sentence_2 = "26.45.56.5.5.4.3"
split_sentence= sentence_2.split(".")
print(split_sentence)


#joining of string
#example 1
sentence = "i am jyoshna"
join_sentence = "_".join(sentence)
print(join_sentence)
#example 2
sentence = "i am jyoshna"
join_sentence = ":".join(sentence)
print(join_sentence)

