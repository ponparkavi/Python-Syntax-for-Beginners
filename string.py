a="hello world!"

len(a)   #output: 12

str('25')   #output: '25'

print(type(a))  #output: <class 'str'>

name = "Python"
print(name[0])  #p
print(name[1])  #y
print(name[5])  #n
print(name[-1])   # n
print(name[-2])   # o

# ===index position====
#  P   y   t   h   o   n
#  0   1   2   3   4   5
# -6  -5  -4  -3  -2  -1

#  string[start:stop]

print(name[0:2])  #py
print(name[2:5])  #tho
print(name[:3])     # Pyt
print(name[2:])     # thon
print(name[:])      # Python
print(name[::2])    # Pto
print(name[::-1])   # nohtyP   [reverse the string]


print("Hi " * 3)  # output : Hi Hi Hi
print("Hello" + "World")  # output : HelloWorld
print("Hello" + " " + "World")  # output : Hello World
print("Hello" + str(5))  # output : Hello5

print(name.upper())  # output : PYTHON
print(name.lower())  # output : python
print(name.capitalize())  # output : Python
print(name.title())  # output : Python

h = "    hello    "
print(h)    #output:     hello
print(h.strip())   #output:hello


text = "I like Java"
print(text.replace("Java", "Python"))  #output: I like Python

print(text.split())  #output: ['I', 'like', 'Java']

jointext = text.split()
print("-".join(jointext))  #output: I-like-Java

print(text.find("Java"))  #output: 7
print(text)  # output: I like Java

print(text.find("Python"))  #output: -1


text = "banana"
print(text.count("a"))  #output: 3
print(text.count("na"))  #output: 2
print(text.startswith("ba"))  #output: True
print(text.endswith("na"))  #output: True


#checking string content 

print("123".isdigit())
# True

print("Python".isalpha())
# True

print("Python123".isalnum())
# True

print("python".islower())
# True

print("PYTHON".isupper())
# True


# !IMPORTANT!  [String are immutable]
name = "Python"
name[0] = "J"  #TypeError: 'str' object does not support item assignment

print("J"+name[1:])  #output: Jython  [This is how we can change the string]

