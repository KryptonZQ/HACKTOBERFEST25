print("hello world")

"""to check python version
import sys
print(sys.version)
"""
#variables
x = 5
y = "hello sai!"
print(y , x)

#casting for speecifying data type
x = int(4)
y = str("sai")
z = float(4)
s = x + z
print (s)

#type() function
print(type(s))

#multiple value assign to multiple variables
x , y , z = "orange" , "apple", "papaya"
print(x,y,z)

#one value to multiple variables
x = y = z = "alphanso mango"
print(x)
print(y)
print(z)

#unpack a collection 
fruits = ["raspberry" , "gauva" , "mango"]
x, y, z = fruits
print(x)
print(y)
print(z)

# + operator adds for int and concatenate for string
print( 20 + 12)
print("sai" + "deshmane")

#global variable
x = "awesome"
def myfunction():
    print("python is" + x);

myfunction

#local & global having same name , variable unside func called as local 
x = "awesome"
def myfunc():
    x = "fantastic"
    print("python is" + x)

myfunc()
print("python is" + x)

#but we declare variable as global inside a function
def myfunct():
    global x
    x = "damnnnnnn"
myfunct()
print("python is " + x)

#we can also change global variable (here awesome is overwrite by fantasticcc)
x = "awesome"
def myfun():
    global x
    x = "fantasticcccc"
myfun()
print("python is" + x)

#boolean type
sai = True
print(sai)
print(type(sai))

#list
x = ["sai" , "vishu" , "vishwa"]
print (x)
print(x[2])

#tuple(immutable)
x = ("sai" , "vishu", "vishwa")
print(x)
print(x[0])

#range
y = 8
x = range(y)
print(x)
print(type(x))

#dictionary
x = {"name" : "john" , "age" : 36}
print(x)
print(type(x))

#set
x = {"apple" , "banana" , "cherry"}
print(x)
print(type(x))

#frozenset

x = frozenset({"apple" , "banana", "watermelon"})
print(x)
print(type(x))

x = 1   #int
x = 1.0 #float
x = 1j  #complex

#e indicates power of 10, number contaoning is float
x = 10e1
print(x)

#complex with j as imaginary part
x = 3+5j
print(x)
print(type(x))


#type conversion 
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

#random module
import random
print(random.randrange(1, 100))

#multiline string 
a = """hey im sai and i jst 143<3 mauuu """
print(a)
print(len(a))

#check if certain character or phrase is in string or not using keyword 'in'
txt = ["sai" , "vishu", "vishwa"]
if "sai" in txt:
    print(True)
    
#To check if a certain phrase or character is NOT present in a string, 
# we can use the keyword not in
txt = ["sai" , "vishu", "vishwa"]
if "vishwajeet" not in txt:
    print(False)
    
#slicing char at 11 not included means printed from index 6 to 10 only
b = "hello world"      
print(b[6:11])
print(b[:6]) #print from start idx i.e 0 to 5
print(b[2:]) #print from idx 2 to end

#-11 -10-9 -8 -7 -6 -5 -4 -3 -2 -1           
#  h  e  l  l  o  w  o  r  l  d  !
#  0  1  2  3  4  5  6  7  8  9  10 11

b = "hello world!"
print(b[-5:-2])

#upper()
a = "sai"
print(a.upper())

#lower()
a = "sai"
print(a.lower())

# strip() method removes any whitespace from the beginning or the end
a = "  sai  "
print(a.strip())

#replace() method replaces a string with another string
a = "sai"
print(a.replace("sai" ,"vishu"))

#split() method splits the string into substrings if it finds instances of the separato
a = "Hello, World!"
print(a.split(","))

# we can combine strings and numbers by using f-strings or the format() method!
age = 21
txt = f"my age is {age}"
print(txt)

#A placeholder can contain variables, operations, functions, and
# modifiers to format the value.
#Add a placeholder for the price variable
price = 59
txt = f"the price is {price}"
print(txt)

#Display the price with 2 decimals, colon : followed by a legal formatting type, like .2f
price = 59
txt = f"the price is {price :.2f}"
print(txt)

# placeholder can contain Python code, like math operations
txt = f"the price is {20 * 20}"
print(txt)

# to insert characters the are illegeal in a string,use an escape character
#1. \"
txt = "sai is a \"viking\" "
print(txt)

# 2.\' 
# txt = 'sai is a \'viking\' '
print(txt)

#3.\\ (enters one backslash)
txt = "this will insert one\\ backslash"
print(txt)

#4.\n (for new line)
txt = "sai is \n viking"
print(txt)

#5.\r (Carriage Return)
txt = "Hello\rworld!"
print(txt)

#6.\t (Tab)
txt = "hello \t world"
print(txt)

#7.\b (Backspace)
txt = "hello \b world"
print(txt)

#8.\f (Form Feed)
txt = "hello \f world"
print(txt)

#A backslash followed by an 'x' and a hex number represents a hex value:
txt = "\x48\x65\x6c\x6c\x6f"
print(txt) 

#string methods

#count() Returns the number of times a specified value occurs in a string
txt = "hello world!"
print(txt.count('l'))

#ccasefold() Converts string into lower case
txt = "HELLO world!"
print(txt.casefold())

#endswith() Returns true if the string ends with the specified value
txt = "hello world!"
print(txt.endswith('!'))

#find()	Searches the string for a specified value and returns the position of where it was found
txt = "hello world!"
print(txt.find('o'))

#index()	Searches the string for a specified value and returns the position of where it was found
txt = "hello world!"
print(txt.index('o'))

#isdecimal() Returns True if all characters in the string are decimals
txt = "hello world!"
print(txt.isdecimal())

#more methods based on string check on w23 school

#boolean 
print(10 > 9)
print(10 < 9)
print(10 == 9)

#bool() function allows you to evaluate any value, and give you True or False in return,
print(bool("hello"))
print(bool(15))

#evalute the two variables
x = "hello"
y = 15
print(bool("hello"))
print(bool(15))

#Almost any value is evaluated to True if it has some sort of content.
#Any string is True, except empty strings.
#Any number is True, except 0.
#Any list, tuple, set, and dictionary are True, except empty ones.

#The following will return True:
print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))

#The following will return False:
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

#One more value, or object in this case, evaluates to False, and that is if you have 
# an object that is made from a class with a __len__ function that returns 0 or False
class myclass():
    def __len__(self):
        return 0
myobj = myclass()
print(bool(myobj))

#Print the answer of a function:
def myFunction() :
  return True
print(myFunction())

#Print "YES!" if the function returns True, otherwise print "NO!":
def myFunction() :
  return True
if myFunction():
  print("YES!")
else:
  print("NO!")
  
#Check if an object is an integer or not:
x = 200
print(isinstance(x, int))

a = "hello world"
print(a[1])

for x in "hello world":
    print (x)
    
a = "hello world"
print(len(a))

#Print only if "free" is present
txt = "sai"
list = txt
if 'a' in txt:
  print(txt.index('a'))
  
#Check if "expensive" is NOT present in the following text
txt = "i am sai"
print("sai" not in txt)
if "vishwa" not in txt:
    print("vishwa in not present")