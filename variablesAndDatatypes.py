x = 2+3*6
print(x)   #output: 20

print('Alice''Bob')   #output:AliceBob
print('Alice'+'Bob')   #output:AliceBob
print('John'*3)     #output:JohnJohnJohn

variable_2 = "alphabet then numbers"

# single line comment
# multi line 
# comment

s = 5  #initialization 
print("hello world",s)  #output: hello world 5

name = input("Enter your name: ")  #user input
print("Hello", name)  #output: Hello <name>

print("hello, {}".format(name))  #output: hello, <name>  [Another way of printing]


print(f'hello, {name}')  #output: hello, <name>  [Another way of printing]

# built-in data types:

# 1.Numeric
    # int
    # float  [23.08]
    # complex [3+4j]
#2. Boolean
    # bool [true,false]
#3. Sequence
    # str ['hello' 0r "hello" or '''hello''']
    # list     [value1, value2, value3]  
    # tuple    (value1, value2, value3)  
    # range      range(1, 6)
# 4.Set
    # set      {10, 20, 30, 20}
    # frozenset      frozenset([10, 20, 30]) {immutable set}
# 5.Mapping
    # dict          variable = {key1: value1,key2: value2}
# 6.Binary
    # bytes          immutable binary data.  
    # bytearray     bytes, but mutable
    # memoryview   Provides a view of binary data without copying it.
# 7.None
    # NoneType      no value / absence of a value.


str('25')   #output: '25'
int(7.779)   #output: 7
int(True)
# Output: 1

int(False)
# Output: 0

float(7)   #output: 7.0
float('7.779')   #output: 7.779
float(True) #output: 1.0
float(False) #output: 0.0


bool(1)  #output: True
bool(0)  #output: False
bool('')  #output: False
bool('hello')  #output: True
bool(25)  #output: True
bool(-5)  #output: True

list("Python")
# Output: ['P', 'y', 't', 'h', 'o', 'n']
list((1, 2, 3))
# Output: [1, 2, 3]
print(list({1, 2, 3}))
# Output: [1, 2, 3]


tuple([1, 2, 3])
# Output: (1, 2, 3)
tuple("ABC")
# Output: ('A', 'B', 'C')


set([1, 2, 2, 3])
# Output: {1, 2, 3}


dict(a=10, b=20)
# Output: {'a': 10, 'b': 20}

frozenset([1, 2, 3])
# Output: frozenset({1, 2, 3})
