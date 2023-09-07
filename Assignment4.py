#1. add a key to dictionary 
dict1={}
print(dict1)
dict1[0]=10
print(dict1)
dict[1]=20
dict[2]=30
print(dict1)


#2.check wheather a given key is already exits in dict
myDict = {'a': 'apple', 'b': 'Banana' , 'o': 'Orange', 'm': 'Mango'}
print("Dictionary : ", myDict)
key= input("please enter the key you want to search for: ")
if key in myDict:
    print("\nkey Exits in this Dictionary")
    print("key = ",key, " and value = ", myDict[key])
else:
    print("\nkey Does not Exists in this Dictionary")


#3. python program to iterate over dictionaries using for loops
d = {'X': 10, 'y': 20, 'z': 30}
for dict_key, dict_value in d.items():
    print(dict_key,'->',dict_value)


#4. python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys
dic={}
for i in range(1,16):
    dic[i]=1**3
print(dic)



#5.converting string to dictionary
string="marolix technology"
letter_count={}
for char in string:
    if char in letter_count:
        letter_count[char]+=1
    else:
        letter_count[char]=1
print(letter_count)


#6. python program to sum all the items in a dictionary.
dict={'orange':20,'banana':30,'apple':40}
print(sum(dict.values()))


#7. python program to combine two dictionary by adding values for common keys.
dict1 = {'a': 100, 'b': 200, 'c':300}
dict2 = {'a': 300, 'b': 200, 'd':400}
for key in dict2:
    if key in dict1:
        dict2[key]=dict2[key]+ dict1[key]
print(dict2)


#8. python program to access dictionary keys element by index.
dict={'cricket':50,'volleyball':20,'basketball':30}
print(dict.keys())
for i in dict:
    print(i)



#9. python program to remove a key from a dictionary.
dict={'circket':50,'volleyball':20,'basketball':30}
print(dict.popitem())
print(len(dict))
print(dict.pop('volleyball'))
print(dict)


#10. python script to merge two python dictionaries.d
dict={'cricket':50,'volleyball':25,'baskrtball':35}
dict1={'orange':20,'banana':30,'apple':20}
dict2=dict1.copy()
dict2.update(dict)
print(dict2)
