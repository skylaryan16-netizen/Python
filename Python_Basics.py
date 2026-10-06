# %% [markdown]
# # Python Basics

# %%
import sys
print(sys.version)

# %%
# First Class of Python

2+3


# %%
print('Hello')

# %%
print()

# %%
a = 2+3
a
b = 4+5
b

# %%


# %%
print(a)

# %%
a= 8
a

# %%
5-4

# %%
4-5

# %%
6*7

# %%
10/5

# %%
7/3

# %%
7//3

# %%
13/5

# %%
13//5

# %%
13%5

# %%
2**5

# %%
2^5

# %%
2&5

# %%
10^3

# %%
3^4

# %%
12^3

# %%
3^10

# %%
10^2

# %%
100^2

# %%
96^10

# %%
64**(1/2)

# %%
64**0.5

# %%
2+6*6-8

# %%
(2+6)*6-8

# %%
import keyword
 
# printing all keywords at once using "kwlist()"
print("The list of keyword's is : ")
print(keyword.kwlist)
print(len(keyword.kwlist))

# %%
# Variables

# %%
12 = 5

# %%
1a = 7

# %%
$a = 8

# %%
_a = 3

_a

# %%
_1a = 5

_1a

# %%
a_12 = 67

# %%
c_6473tbnllkn---^^^sav = 9
c_6473tbnllkn---^^^sav

# %%
c_6473tbnllkn---^^^ = 9
c_6473tbnllkn---^^^

# %%
c_6473tbnllkn--- = 9
c_6473tbnllkn---

# %%
c_6473tbnllkn = 9
c_6473tbnllkn

# %%
c_6473tbnllkn@@---^^^b = 9
c_6473tbnllkn@@---^^^b

# %%
#keywords

import keyword
print(keyword.kwlist)
len(keyword.kwlist)
print("\nTotal number of Keywords in Python:", len(keyword.kwlist))

# %%
import keyword

print("Total number of Keywords in Python:","\n", len(keyword.kwlist))


# %%
import keyword
print(keyword.kwlist)

print("\n 123")

# %%
a = keyword.kwlist
a

# %%
lambda = 5

# %%


# %%
print()=5

# %%
# Identifiers

_a = 10


# %%
_a

# %%
" abcdecvwevowruvbpebpvbei"

# %%
#multiline comments

#cqkhvvwjl
#cbj wljf
#v j lkf p

""" This is a 
multiline 
comment"""

# %%


# %%
# Identation

a = 25

if a>10:    
    print(a)
    print(a-20)

else:
    print("a is less than 10")

print(a+2)
    

# %%
# Print the list of first 10 numbers of number series (whole numbers) with 50 being printed after each individual number


# if { fjkblwrn;vnwekn
#   else{jlcblbvflbe}}

for i in range(10):
    print(i)
    print(50)
    
print(100)


# %%
# Print the list of first 10 numbers of number series (natural number numbers) with 50 being printed after each individual number


for i in range(1,11):
    print(i)

# %%
for i in range(-1,11):
    print(i)

# %%
# print the list of 10 numbers staring from 4.5 and having an step size of 0.5

for i in range(5,10):
    print(i-0.5)
    print(i)
    


# %%
for i in range(5,9):print(i-0.5); print(i)


# %%
# Python statements

a = 1 # single line python statement

a

# %%
# multi line statements

b = (1+2+3+
4+5+
6+7
+8+9)

c = 1+2+3+\
4+5+\
6+7+\
8+9+10


print(b)
print(c)

# %%
a= 10; b=20; c=30

print(a,b,c)

# %%
a = 10
b= 5.5
c= "DA"

print(a,b,c)

# %%
a,b,c = 20, 5.5, "DS"

print(a,b,c)


# %%
x = 3

print(id(x))

# %%
y = 3

print(id(y))

# %%
x = 5

print(id(x))

# %%
z = 2
print(id(z))

# %%
# Data Types

a = 5

b = 2.5

print(type(a))
print(type(b))


# %%
isinstance(b,int)

# %%
b = 2+5j

print(type(b))


# %%
isinstance(b,complex)

# %%
q = 

# %%
q

# %%
a = 10
a

# %%
a = True

print(type(a))

# %%
a

# %%
x = 5

# %%
x

# %%
a = 22/7
a

# %%
b = 5**0.5
b

# %%
type(b)

# %%
type(a)

# %%
# Strings

s = "This is Data Analytics Course"
type(s)


# %%
s[0]

# %%
s[-1]

# %%
s[5:15]

# %%
# Data Structures
# 1. Lists

# ordered sequence- indexable
# square brackets
# mutable
# elements are seprated by commas


a = [1,2,3,4]

b = [1,2.2,"DS"]

c = [1,2,[3,4],["DS",5.6]]

d = [1,2,[3,4],["DS",5.6], ("DA","ML")]

print(type(a), type(b), type(c))

# %%
print(a)

# %%
a[2], b[1], c[2], c[2][1],d[4][0][1] 

# %%
a[2] = 5

a

# %%
a[4] = 6

# %%
lst = ['a','b','c','b','d']
lst.index('b')

# %%
d = [1,2,[3,4],["DS",5.6], ("DA","ML"),"AB","AB"]

d.index("AB")

# %%
# 2. Tuples

# ordered sequence- indexable
# parenthesis ()
# elements are seprated by commas
# immutable

t = (1, 2.2, "DS")
t1 = (1,2,3)
t2 = ("DA","DS","ML")
t3 = (1,2,("DS","ML"),[4.5,6])


# %%
t[1]

# %%
t2[2]

# %%
t[2] = "DA"

# %%
t1[2], t2[1], t3[2], t3[3][0]

# %%
t4 = (1,2,("DS","ML"),(4.5,6),[7,8])

t4[4][1]

# %%
t4[4] = [9,10]

# %%
t4[4][0]=9
t4[4][1]=10

t4

# %%
d = [1,2,[3,4],["DS",5.6], ("DA","ML")]

# %%
d[4][1] = "Data"

# %%
d[4] = ("Data","Machine")

d

# %%
# 3. Set

# unordered Sequence- unindexable
# {}
# saves only unnique vales, if repetions in input will save only one instance of the repititve element


a = {10,20,40,50}

# %%
print(type(a))

# %%
print(a)

# %%
a[2]

# %%
b = {10,20,40,50, 15, 25, 10, 20}

print(b)

# %%
# 4. Dictionary

# unordered sequence - non indexable
# {}
# Data is saved in Key- Value pair
# Values can be access through keys
# keys should be unique - to avoid data loss

d = {'a':'apple','b':"banana", 'c': 'chickoo'}

# %%
print(d)

# %%
d['a']

# %%
d['a'] = 123
print(d)

# %%
print(d['b'])

# %%
list = [1,2,3,4,5]

if 5 in list:
    print(5)
    
    
list[3]    

# %%
for i in range(2,-10,-3):
    print(i)

# %%
d['a']

# %%
d['apple']

# %%
e = {'a':'apple','b':"banana", 'c': 'chickoo', 'a':'mango'}

# %%
e['a']

# %%
f = {'a':'apple','b':"banana", 'c': 'chickoo', 'a':'mango', 'a': 'orange'}

# %%
f['a']

# %%
print(f)

# %%
# conversion of data types 

# int -> float, string
# float -> string, int
# string -> int, float

# how to take input  from user
# output formatting

# types of operators and their details

# %%
a = 5
print(a)

# %%
b = float(a)
b

# %%
id(a)

# %%
id(b)

# %%
c = 6
c

# %%
d =7
d

# %%
type(a)

# %%
id(c)

# %%
id(d)

# %%
str(a)

# %%
b = 6.6
print(b)

# %%
type(b)

# %%
int(b)

# %%
str(b)

# %%
c = 'abc'
print(c)

# %%
int(c)

# %%
d = '123'
print(d)


# %%
int(d)

# %%
float(d)

# %%
e = '12.56'
e

# %%
int(e)

# %%
f = float(e)
f

# %%
int(f)

# %%
g = int(float(e))
g

# %%
z= True
y = False

print(type(z))
print(type(y))

# %%
str(z)

# %%
user = 'Satish'
lines = 100

print("Congratulations " + user + "! You just wrote" + " " + str(lines) + " " + "lines of Code")

# %%
print(1+2+3)

# %%
print("congratulations",user,"You just wrote",lines,"lines of code")

# %%
print(4+5)

# %%
a= [1,2,3,4,1,2]

type(a)

# %%
S = set(a)
print(S)
print(type(S))

# %%
b = list(S)
print(b)

# %%
a = list(set(a))
print(a)

# %%
t = tuple(a)
print(t)
print(type(t))

# %%
t2 = ()

type(t2)

# %%
s1 = "Hello"

list(s1)

# %%
tuple(S)

# %%
# taking input from user for addtion of two numbers

num1 = input("Enter an integer:")
num2 = input("Enter an integer:")


a = int(float(num1))
b = int(float(num2))

result = a + b

#result = num1 + num2

print(result)

# %%
num1 = int(float(input("Enter an integer:")))
num2 = int(float(input("Enter an integer:")))

result = num1 + num2

print(result)

# %%
num1 = float(input("Enter an integer:"))
num2 = float(input("Enter an integer:"))

result = num1 + num2

print(result)

# %%
num1 = float(input("Enter an integer:"))
num2 = float(input("Enter an integer:"))

result = num1/num2

print(result)

# %%

num1 = int(input("Enter an integer:"))
num2 = int(input("Enter an integer:"))

result = num1/num2

print(result)

# %%
#Output formatting

print("Hello World")

# %%
a = 5
b= 10.5

print(a,b)

print("The value of a is", a)
print("The value of b is", b)
print("The value of a and b are", a, "and", b)

print("The value of a and b are "+ str(a)+ " and "+str(b))


# %%
a = 5
b = 10
print("The value of a is {0} and b is {1}".format(a,b))
print("The value of a is {1} and b is {0}".format(a,b))


# %%
a = 5
b = 10

print("The value of a is [] and b is []".format(a,b))
print("The value of a is {0} and b is {1}".format(a,b))
print("The value of a is {1} and b is {0}".format(a,b))


# %%
a = 5
b = 10
print("The value of a is {a} and b is {b}")
print("The value of a is {1} and b is {0}".format(a,b))


# %%
print("Hello {name}, Good {greeting}".format(name = "Satish", greeting = "Morning"))

# %%
# operators

# 1) Arithmatic Operators -> +,-,*,/,%, //, **
# 2) comparison operators -> >, <,>=, <= , == , != 
# 3) logical Operators -> and, or ,not
# 4) Assignment Operator -> =, +=, -=, *= , /=, **= 
# 5) Bitwise Operators -> & (and), | (or), ~(not), bitwise XOR,bitwise left shit, bitwise right shift


# Binary of 10 =  2^3+2^2+2^1+2^0
#  14              1   1   1   0
#  15              1   1  1   1


# 6) Identity Operator -> is, is not

# 7) Membership Operator -> in, not in


# %%
a = [1,6,3,4,5,2,10,9,8,7]

m=0
n= 0

for i in a:
    if i < 6:
        print(i)
        m += 1
        
    else:
        n +=1  
        
print("No. of items < 6:",m)
print("No. of items >= 6:",n)

# %%
b = ["Mayank","Parth","Abhishek","mayur","Lalit"]

m = []
n = []

p = 0
q = 0

for i in b:
    if (i[0] == "M") or (i[0] == "m") : 
        p = p+1
        m.append(i) 
        
        
    else:
        q = q+1
        n.append(i)
        
        
print(m, p)
print(n,q)
            


# %%
b = ["Mayank","Parth","Abhishek","Mayur","Lalit"]

m=0
n= 0

for i in b:
    if i[0] == "M":
        print(i)
        m += 1
        
    else:
        n +=1  
        
print("No. of names strating with M:",m)
print("No. of names not strating with M:",n)

# %%
# Control flow statement:  

# 1) if- else, if- elif- else

# If statements:
 # Syntax: 
     #if test expression:
        #statement(s)
        
# If - else statement:
# Syntax:
    #if test expression:
        #statement(s)
        
    #else:
           #statement(s)
        
# If -elif- else statement:
# Syntax:
    #if test expression:
        #statement(s)
        
    #elif test expression:
         #statement(s)
        
    #else:
           #statement(s)

# %%
num = float(input("Enter an integer:"))

if num >0:
    print("Positive Number")
    
elif num == 0:
    print("Neither Negative nor Positive")
        
else:
    print("Negative Number")

# %%
a 

# %%
# 2) While loop

# Syntax:
#    while text_expression:
#          Body of while


#important: index increment should always be given with while loop to stop the loop at required position- 
#else it will go into infinite loop

# %%
a = [1,6,3,4,5,2,10,9,8,7]

for i in a:
    if i<3:
        print(i,"less than 3")
        
    elif i<6:
        print(i,"less than 6")
        
    elif i<9:
        print(i,"less than 9")
        
        
    else:
        print(i,"The number is 10")



# %%
# write a program to check if a number is prime or not and what are its factors

num = int(input("Enter an integer:"))

isdivisible = False;


for i in range(2, int((num**0.5)+1)):
        if num % i == 0:
            isdivisible = True
            
    
if  isdivisible == True:
    
    print("Not_Prime")
    
    
else:
    print("Prime")



# %%
# write a program to check if a number is prime or not and what are its factors


num = int(input("Enter an integer:"))

isdivisible = False;

i = 2;

while i < ((num**0.5)+1):
    if num % i == 0:
        isdivisible = True
        print("{} is divisbile by {}".format(num,i))
        break
    
    i = i+1
        
if isdivisible == True:
    print("{} is not a prime number".format(num))
    
else:
    print("{} is a prime number".format(num))
    

    

# %%
# 3) For loop;

# for- else loop

# break statement

# continue statement

# %%
# 3) For Loop - helps us in tranversale( to iterate over a data sequence)

# Syntax:

# for ele in sequence:
#       body of for



# we can use else with for as well, but it is optional

# break statements effect on for-else loop

# %%
num = [1,2,3]
j = 0 
for i in num:
    print(i)
    j += i
    
else:
    print(j)
    print("No number left")

# %%
num = [1,3,2,5]

for i in num:
    print(i)
    if i % 2 ==0:
        break
    
else:
    print("No number left")
    


# %%
import time

start = time.time()

num1 = 10
num2 = 50


for n in range(num1, num2 + 1):
    isdivisible = False 
    for i in range(2, int((n**0.5)+1)):
        if n%i == 0:
            isdivisible = True
            
    if isdivisible == False:
        print(n)
            
end = time.time()

print(end-start)

# %%
num1 = 10
num2 = 50


for n in range(num1, num2 + 1):
    isdivisible = False 
    for i in range(2, int((n**0.5)+1)):
        if n%i == 0:
            isdivisible = True
            break
            
    if isdivisible == False:
        print(n)
            
           

# %%


# %%
# To display prime numbers within an interval

# let interval be between 10 and 50, both are inclusive

num1 = 2
num2 = 50
print("Prime numbers between {0} and {1} are:".format(num1,num2))

#if num1 < num2:
#     a = num1
#   b = num2
# else a = num2, b = num1


for n in range(num1, num2 +1):
    if n > 1:
        isdivisible = False;
        for i in range(2,n):
            if n % i == 0:
                isdivisible = True;
        if not isdivisible:
            print(n)
        
    

# %%
# Break and Continue

# can alter the flow of a control loop

# %%
# continue example

lst = [1,2,3,4,5]

for i in lst:
    if i%2 != 0:
        print(i)
    


# %%
lst = [1,2,3,4,5]

for i in lst:
    if i%2 == 0:
        continue
    else:
        print(i)
    

# %%
lst = [1,2,3,4,5,6,7,8,9]

for i in lst:
    if i%2 == 0:
        continue
    print(i)
    
else:
    print("list end")


# %%
# Lists

# empty list    
lst = []

lst1 = [1,2,3,4,5,6]

len(lst1)

# %%
lst1[6] = 7

lst1

# %%
# append list

lst1.append(7)

lst1

# %%
lst1.append(8,9,10)

lst1

# %%
lst1.append([8,9,10])

lst1

# %%
# To display prime numbers & Not prime numbers separetely within an interval

# let interval be between 10 and 50, both are inclusive

num1 = 2
num2 = 50

#if num1 < num2:
#     a = num1
#   b = num2
# else a = num2, b = num1


prime= []
not_prime = []


for n in range(num1, num2 +1):
    if n > 1:
        isdivisible = False;
        for i in range(2,n):
            if n % i == 0:
                not_prime.append(n)
                isdivisible = True;
                
        if not isdivisible:
            prime.append(n)
            
            
not_prime = list(set(not_prime))
print("Prime numbers between {0} and {1} are:".format(num1,num2),prime)
print("Composite numbers between {0} and {1} are:".format(num1,num2), not_prime)

# %%
#insert

lst1 = [1,2,3,4,5,6]

lst1.insert(7,8)

# %%
lst1

# %%
lst1[6]

# %%
lst1 = [1,2,3,4,5,6]

lst2 = [7,8,9]

for i in lst2:
    lst1.append(i)
    
print(lst1)

# %%
lst1 = [1,2,3,4,5,6,7]

lst2 = [7,8,9]

lst3 =[10,11,12]

lst1.insert(7,8)


print(lst1)

# %%
# remove
lst1.remove(7)

lst1

# %%
lst1.remove(8,9)

lst1

# %%

lst1 = [1,2,4,3,2,5]

lst1.remove(2)

# %%
lst1

# %%
#extend
lst1 =[1,2,3,4,5,6]
lst2 =[7,8,9]

lst1.extend(lst2)

lst1

# %%
# Delete

lst = ['one', 'two','three','four','five']

del lst[1]

print(lst)

# %%

lst = ['one', 'two','three','four','five']

del lst[lst.index("three")]

print(lst)



# %%
# pop

a =lst.pop(2)
print(a)
print(lst)

# %%
lst.pop(2)

print(lst)

# %%
# reverse

lst = ['one', 'two','three','four','five']

lst.reverse()

print(lst)

# %%
lst[0]

# %%
# sorted
lst2 = [3,6,2,8,5,8,0,1]

lst3 = sorted(lst2)

print(lst3)
lst2

# %%
lst4 = sorted(lst2)

print(lst4)

# %%
lst4.reverse()
lst4

# %%
lst6 = [3,6,2,8,5,8,0,1]

sorted(lst6)

# %%
lst6

# %%
lst5 = sorted(lst2, reverse = True)

print(lst5)

# %%
# sort
lst2.sort()
print(lst2)

# %%
# split
s = "one, two, three, four, five,six"

abc = list(s)
print(abc)

slst = s.split(', ')

print(slst)

# %%
slst[-2]

# %%
slst[1:3]

# %%
slst[0:4:2]

# %%
lst1 =[1,2,3,4,5,6]
lst2 =[7,8,9]


lst3 = lst1 +lst2

print(lst3)

# %%
lst1 =[1,2,3,4,5,6]

lst2 = []

for i in lst1:
    i +=1
    lst2.append(i)
    
print(lst2)

# %%


# %%
lst1.index(2)

# %%
num1 = 10
num2 = 50
lst =[]

for n in range(num1, num2 + 1):
    isdivisible = False 
    for i in range(2, int((n**0.5)+1)):
        if n%i == 0:
            isdivisible = True
            break
            
    if isdivisible == False:
        lst.append(n)
            
print(lst)  

# %%
num = [1,2,3,4,5,6,1,3,5,3,7]

# frequency of 1 in lst

num.count(5)


# %%
list2 =[2,4,6,8,10]

if 4 in list2:
    print(4)

# %%
list1 = [1,2,3,4,5,6]
list2 =[2,4,6,8,10]

for i in list1:
    if i in list2:
        print(i)
        
        


# %%
# list comprehension

square=[]
for i in range(11):
    square.append(i**2)
print(square)

# %%
# list comprehension

sqr = [ i**2 for i in range(11)]
print(sqr)

# %%
lst = [-1,-2,3,-4,-5]

positive=[]
for i in lst:
    positive.append(abs(i))
    
print(positive)


# %%
lst = [-1,-2,3,-4,-5]

positive1=[abs(i) for i in lst]
positive1

# %%
lst2 = [1,-3,5,7,-8,-2,6]
lst4 =[]

for i in lst2:
    if i>0:
        lst4.append(i)
        
print(lst4)


# %%
lst2 = [1,-3,5,7,-8,-2,6]


lst3 = [i for i in lst2 if i >0]
print(lst3)

# %%
list1 = range(11)

list2=[]

for i in list1:
    list2.append((i,i**2))

print(list1)
print(list2)

# %%
list3 = [(i,i**2) for i in range(11)]

print(list3)

# %%
list3 = [i for i in range(11)]
list3

# %%
list3 = [(i,i**2) for i in list1]
print(list3)

# %%
#tuples 

t = ('Data'*4, 'Data'*4)

print(t)

# %%
len(t)

# %%
t[1]

# %%
type(t)

# %%
t = (('Data',) *4)

print(t)

# %%
del t[2]

# %%
del t

# %%
t

# %%
t = (1,2,3,4,58,9,1,2,4,7,5,4)

t.count(1)

# %%
t.index(58)

# %%
p = t.index(1)

# %%
t.index(1,(p+1))

# %%
print(1 in t)

# %%
1 in t

# %%
10 in t

# %%
max(t)

# %%
min(t)

# %%
sum(t)

# %%
#Sets

S = set()

print(S)

# %%
s = {1,3}

s.add(2)

print(s)

# %%
s.add(5,6,7)

print(s)

# %%
s.update([5,6,7])
print(s)

# %%
s.update([8,9], {10,11,12})

print(s)

# %%
a= [12,14]

b = {15,16,17}

s.update(a,b)

print(s)

# %%
#delete element from set
# discard function

s.discard(17)

print(s)


# %%
s.pop()
print(s)

# %%
s.pop()
print(s)

# %%
s.clear()

# %%
s

# %%
s.update(1,2)
s

# %%
# Python Set operations

s1 = {1,2,3,4,5}
s2 = {3,4,5,6,7}

# %%
# Union of sets
# using Bitwise OR(|)
print(s1 | s2)

# %%
print(s1.union(s2))

# %%
# Intersection of sets
# using Bitwise AND(&)
print(s1 & s2)

# %%
print(s1.intersection(s2))

# %%
# Set Difference

print(s1-s2)

# %%
print(s2-s1)

# %%
print(s1.difference(s2))

# %%
# symmetric Difference  (^)

print(s1^s2)


# %%
print(s1.symmetric_difference(s2))

# %%
# finding subsets suing 'issubset()' function
s1 = {1,2,3,4,5}
s3 = {1,2}

s3.issubset(s1)


# %%
s4 = frozenset()

# %%
s4

# %%
type(s4)

# %%
a = {1, 2, 3}
b = frozenset([3, 4, 5])

print(a.union(b))
print(a.intersection(b))
print(a.difference(b))


# %%
a = {1,2,3}
b= frozenset(a)
print(b)
c = b
b = set(b)
print(b)

print(c)


# %%
# dictonary

dict = {"name":"Amit", "age":27, "address": "Pune"}
dict

# %%
dict['name']

# %%
dict['name'] = 'Akshay'

# %%
dict

# %%
dict['Degree'] = 'MBA'

# %%
dict

# %%
dict.pop('Degree')

dict

# %%
# for removing arbitary/ random key-value
dict.popitem()

dict

# %%
del dict['name']

dict

# %%
dict.clear()

dict

# %%
del dict

# %%
dict

# %%
d = {"name":["Amit","ajay"], "age":27, "address": "Pune"}
d

# %%
d['name']

# %%
# loops in dictionary

d = {'a':1, 'b':2, 'c':3}

for i in d:
    print(i,d[i]**2)

# %%
d.items()

# %%
a = d.items()
a

# %%
for i in d.items():
    print(i)

# %%
d={1:"apple",2:"banana",3:"republic"}

for i,j in d.items():
    print([i,j])

# %%
for i in d.keys():
    print(i)

# %%
for j in d.values():
    print(j)

# %%
t = (i for i in range(10))
t

# %%
print(t)

# %%
# dictionary comprehensions

#print only pairs where the value is greater than 2

d = {'a':1, 'b':2, 'c':3, 'd': 4}

new_d = {k:v for k,v in d.items() if v > 2}

print(new_d)


# %%
list = [1,2,3,4]

list.reverse()
list

# %%
a= 'abcd'

# print(a.reverse())

# b =list(a)

# b = a.split()


b = []

for i in a:
    b.append(i)

print(b)

c = b.reverse()
print(c)




# %%
d ="abcdef"

d[::-1]

# %%
#Assignment
# write a python program to check weather a given string is a palindrome

# palindrome ->  eg. 'madam', 'Nayan', 'naman','radar'




a = 'madam1'
b = 'radar'


if a == a[::-1]:
    print('the input is palindrome')
    
else:
    print('The input is not palindrome')


# %%
a[::-1]

# %%
a = 'madam'
j = 0
for i in range(1,len(a)+1):
    if a[-i] == a[i-1]:
        j = j+1
       
    
print(j)  

if j == len(a):
    print("The input is Palindrome")
    
else:
    print("Not Palindrome")

    

# %%
a = ['q','r','s']
b = ['q','r','s']

if a == b:
    print("Yes")
    
else:
    print("No")
    

# %%
# Assignment
# Python Program to sort the words of a string in Alphabatical Order
# Python Program to sort the alphabets of a string in Alphabatical Order

#  str = "Python Program to sort the words of a string in Alphabatical Order"


s = "Python Program to sort the words of a string in Alphabatical Order"

s = s.lower()
print(s)

lst = s.split()

print(lst)

lst.sort()

print(lst)

# %%
# Functions

# 1) In-Built Funtcions
# 2) User - Defined functions

# %%
# user-defined fucntions

# syntax

# def function_name(parameter):
#    '''DOC STRING'''
#      Doc string
    
#      Statement(s) - loops,continue, return, operations, break
        

# %%
b = 5
print(b)

# %%
def print_name(name,abc, xyz):
    # This function prints the given input   <--- comment
    
    '''This function prints the given input''' # <---document string
    
    x=10
    
    print("Hello" + " " + str(name) +", "+ str(abc)+", " + str(xyz))
    
    
    
a = 'Amit'# defining parameter
b = 'suraj'
c= 'alexa'

print_name(a,b,c)  # calling function
print_name('Nayan','madam','nitin') 

print(print_name.__doc__)

# %%
print(print_name.__doc__)

# %%
print(a)

# %%
print(name)

# %%
print(x)

# %%
#print sum of 3 numbers with the help for user defined function


def addition(a,b,c):
    
    '''This function is built to give sum of 3 numbers'''
    d = a+b+c
    print(d)
    
    print(a+b+c)
    
    
x = int(input("Input the first interger",))
y = int(input("Input the second interger",))
z = int(input("Input the third interger",))



addition(x,y,z)

print(100)
print(addition.__doc__)



# %%
def addition(a,b,c):
    
    '''This function is built to give sum of 3 numbers'''
    d = a+b+c
    print(d)
   
  
    
    
x = int(input("Input the first interger",))
y = int(input("Input the second interger",))
z = int(input("Input the third interger",))



addition(x,y,z)

w = addition(x,y,z)

print(w)


# %%
# Return statement

# Syntax: 
# return[expression]

# %%
def addition(a,b,c):
    
    '''This function is built to give sum of 3 numbers'''
    d = a+b+c
  
    return d
  
    
    
x = int(input("Input the first interger",))
y = int(input("Input the second interger",))
z = int(input("Input the third interger",))


w = addition(x,y,z)

print(w)


# %%
# example of return

lst = [1,2,3,4]

def get_sum(lst):
    total = 0  # initialize
    
    for i in lst:
        total = total + i
    print(total)    
    return total+1



S = get_sum(lst)

print(S)

print(total)

# %%
list =[1,2,3,4]

sum(list)

# %%
# order of execution of python statements

# def function_name():  --------4
    # function body   --------5
    # function body   --------6
    
# statement1      --------- 1

# statement2      ----------2

# function_name() ----------3

# statement3      ----------7

# statement4      ----------8
    

# %%
# program for HCF of two numbers

num1 = int(input("Enter first integer",))
num2 = int(input("Enter second integer",))

def computeHCF(a,b):
    '''This function givers HCF of two numbers'''
    
    smaller = a if b>a else b    # if esle statement in concise way
    
    hcf = 0
    for i in range(2,smaller+1):
        if (a%i == 0) and (b%i == 0):
            hcf = i
    if hcf >0:
        return hcf
    else:
        print("No Common Factors")
    

print("THE HCF of {} and {} is:{}".format(num1, num2, computeHCF(num1, num2)))

# %% [markdown]
# #### types of function arguments:
# 
# 
# 1) Positional Arg
# 
# 2) keyword Arg
# 
# 3) Default Arg
# 
# 4) Variable length Arguments
# i)keyword
# ii)non-keyword
# 
# 4) Arbitrary Arg
# 

# %%
# Positonl Arg

def power(num,exp):
    d =num**exp
    return d


x= power(10,2)
print(x)
    

# %%
# Keyword Arg

def power(num,exp):
    d =num**exp
    return d


x= power(num=10,exp = 2)
print(x)
    

# %%
# Variable-length Arguments 

# i) *args (Non-keyword variable arguments)

def total(*numbers):
    return sum(numbers)

print(total(1, 2, 3, 4))


# ii) **kwargs (Keyword variable arguments)

def profile(**details):
    for key, value in details.items():
        print(key, ":", value)

profile(name="Mayank", role="Analyst", exp=8)


# %%
#Keyword-only Arguments (Python 3+)

#Must be passed using keywords

# Defined after *

def booking(name, *, seat):
    print(name, seat)

booking("Mayank", seat="A1")

#This will raise an error:
booking("Mayank", "A1")



# %%
# Recursive functions:


# when a function is called within its defination

# Write a python program to print factorial of a given number


def factorial(n):
    for i in range(1,n):
        n = n*i
        
    return n

fact = factorial(5)
print(fact)

# %%
# Write a python program to print factorial of a given number using recursive method

def rec_fact(n):
    
    return 1 if n==1 else (n*rec_fact(n-1))
        
 ###     5*4*3*2*1    
rfact = rec_fact(5)

print(rfact)

# %%
# Python program to display the fibonacci sequence upto nth term using recursive function

# Normal function method
def fib(n):
    
    series = []
    x, y = 0, 1
    while x < n:
        series.append(x)
        x, y = y, x + y
    return series



print(fib(10))


# %%
#recursive method

def fibonacci(num):
    
    return num  if num <=1 else fibonacci(num-1)+ fibonacci(num-2)

###   fibonacci(9)                                     +                fibonacci(8)
###   fibonacci(8)+ fibonacci(7)                             fibonacci(7)+ fibonacci(6)

n = 10
fib = []

for i in range(n):
    fib.append(fibonacci(i))
    
print(fib)

# %%
# result list
numbers = ['1', '2', '3', '4', '5', '6', '7']
res = []
for i in numbers:
    # calculate square and add to the result list
       res.extend(list(str(int(i) * int(i))))
print(res)

# %% [markdown]
# #lambda functions
# 
# Lambda Function or Anonymous Function or Function without name This function works faster then conventional function
# 
# Lambda functions can take any number of arguments, but they can only have one expression.
# 
# lambda arguments: expression

# %%
#Lambda function to add two nos
f = lambda a:a+a

# %%
f(8)

# %%
add_ten = lambda a:a+10
add_ten(5)

# %%
#Lambda function with two variables.

f = lambda a,b: a*b
f(3,5)

# %%
# lambda fucntion to check for even input

# syntax: value_if_true if condition else value_if_false

check = lambda a:"Even" if a%2 ==0 else "Odd"

n = int(input("Enter an integer:"))

print(check(n))

# %%
import math

math.sqrt(16)


# %%
(18**0.5)% int(18**0.5)

# %%

check = lambda a:"Square" if (a**0.5)% 1 == 0 else "Not-Square"

n = int(input("Enter an integer:"))

print(check(n))

# %%
# Define a lambda function to categorize numbers into positive, negative and zero

categorize = lambda x: "positive" if x>0 else("zero" if x ==0 else "negative")
categorize(-10)



# %%
cat = lambda x: "positive" if x>0 "zero" elif x ==0 else "negative"

cat(-10)

# %% [markdown]
# Using Lambda with map()
# The map() function applies a given function to all items in an iterable (like a list) and returns a map object 
# (which can be converted to a list)

# %%
num = [1,2,3,4,5,6,7,8]

squared = map(lambda x: x*x, num)

print(squared)
print(list(squared))

squared

# %%
num = [1,2,3,4,5,6,7,8]

squared = map(lambda x: x*x, num)

print(squared)

type(squared)

# %%
num = [1,2,3,4,5,6,7,8]

squared = list(map(lambda x: x*x, num))

squared

# %% [markdown]
# Using Lambda with filter()
# 
# The filter() function constructs an iterator from elements of an iterable for which a function returns true and returns a filter object (which can be converted into list)

# %%
even_num = filter(lambda x: (x%2 ==0), num)

print(list(even_num))

# %%
type(even_num)

# %%
x = [1,2,3,4,5]
y = [2,4]

x+y

# %%
x = [1,2,3,4,5]
y = [2,4]

z = list(set(x)-set(y))

z


# %%
num = [1,2,3,4,5,6,7,8]


even_num1 = filter(lambda x: (x%2 ==0), num)

print(list(even_num1))

print(list(even_num1))

odd_num = list(set(num)-set(list(even_num1)))


print(odd_num)


# %%
list(even_num1)

# %%
num = [1,2,3,4,5,6,7,8]


even_num = list(filter(lambda x: (x%2 ==0), num))



odd_num = list(set(num)-set(even_num))


print(odd_num)
print(even_num)

# %% [markdown]
# Using Lambda for String Manipulation

# %%
# Convert a string to uppercase
uppercase = lambda s: s.upper()
print(uppercase('hello'))

# %%
# Reverse a string
reverse = lambda s: s[::-1]
print(reverse('hello'))

# note: The reverse() function does not work directly on strings in Python because reverse() is a method specifically 
#designed for mutable sequences, like lists. Strings in Python are immutable, meaning their contents 
#cannot be changed after they are created. However, there are alternative ways to reverse a string in Python.

# %%
#using input() function with lambda function

abc = lambda: input("Please enter your Name: ")

a = abc()

# %% [markdown]
# Enumerate function
# The enumerate() function in Python is a built-in function that allows you to iterate over a list (or other iterable) and 
# have an automatic counter. This function adds a counter to an iterable and returns it as an enumerate object. 
# This can be very useful when you need to access both the index and the value of each item in an iterable.

# %%
abc  = [10,20,30,40,50]

# %%
for i,j in enumerate(abc,start =1):
    print(i,":",j)

# %%
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 90)]

# %%
# Use enumerate to iterate over the list with an index
for index, (name, score) in enumerate(students,start=5):
    print("Student",index,":",name,"scored", score)

# %%
# Use enumerate to iterate over the list with an index
for index, (name, score) in enumerate(students,start=0):
    print(f" Student {index} : {name} scored {score}")
    

# %%
# Use enumerate to iterate over the list with an index
for index, (name, score) in enumerate(students,start=1):
    print("Student {} : {} scored {}".format(index,name,score))

#Note: f-string (formatted strings) inside the print statement in the above example wont work with format
    

# %% [markdown]
# Zip function
# 
# The zip() function in Python is a built-in function that allows you to combine two or more iterables 
# (like lists or tuples) element-wise. It creates an iterator that aggregates elements from each of the iterables. 
# The iterator stops when the shortest input iterable is exhausted.
# The zip function returns an object (which can be converted into list)
# 

# %%
names = ["Alice", "Bob", "Charlie","David"]
scores = (85, 92, 78)

# Use zip to combine the lists
combined = zip(names, scores)

print(list(combined))

# %%
print('1 '*5)

# %%
n=10
for i in range(1,n+1):
    print("* "*i)

# %% [markdown]
# Star pattern questions

# %%
n=10
for i in range(0,n):
    for j in range(0, i+1):
        print("*",end=" ")
    print("\r")

# %%
n=10

for i in range(1,n+1):
    print('* '*i)

# %%
n=10

for i in range(0,n):
    print('* '*(n-i))

# %%
n=int(input("Enter nuber of rows:"))
for i in range(n,0,-1):
    for j in range(n-i):
        print(' ',end='')
    for j in range(i):
        print('*', end='')
    print()

# %%
n=int(input("Enter nuber of rows:"))
for i in range(0,n+1):
    print(' '*i , '*'*(n-i))

# %%
n=int(input("Enter nuber of rows:"))
for i in range(0,n):
    print(' '*i , '*'*(2*(n-i)-1))

# %%
n=int(input("Enter nuber of rows:"))
for i in range(n,0,-1):
    for j in range(n-i):
        print(' ',end='')
    

# %%
for i in range(0):
    print(i)
    

# %%
n = int(input("Enter pattern range:"))

j = n-1
i =1

for x in range(0,n):
    print(" "*j, "A "*i)
    j = j-1
    i= i+1
    

# %%
n=int(input("Enter nuber of rows:"))
for i in range(1,n+1):
    print(' '*(n-i) , 'A '*i)

# %%
n=9
i=0
while i<n:
    print(' '*(n-i-1)+'A '*(i+1))
    i+=1

# %%
n = int(input("Enter pattern range:"))

j = n
i =1

for x in range(0,n):
    print("A "*j, " "*i," A"*j)
    j = j-1
    i= i+4
    

# %% [markdown]
# ATM machine code

# %%
#global bal 
bal = 1000
k = 1
def bank_balance(trn_type, amount, bal):
    if trn_type == 1:
        print("Your Balance", bal)
    elif trn_type == 2:
        bal += amount 
        print("Your Balance after Deposit", bal)
    elif trn_type ==  3:
        if amount > bal:
            print("Insufficient balance")
            
        else:
            bal -= amount
            print("Your Balance after Withdrawal", bal)
    return bal
while k < 100:
    trn_type = int(input("Enter Selection 1. Balance, 2. Deposit, 3. Withdraw, 4. Exit:"))
    if trn_type in (1,2,3,4):    #or trn_type == 2 or trn_type == 3 or trn_type == 4:
        if trn_type == 4:
            break
        amt=0
        if trn_type in (2,3): 
            amt = int(input("Enter Amount:"))
        bal=bank_balance(trn_type, amt, bal)
        print(bal)
    else:
        print("Invalid Selection")
        
    k= k+1    

# %%
33 ==33.0

# %%
s1 ={1,2,3}
print(2*s1)

# %%
l = [1,2,3,4,5,7]
l.insert(3,6)
l

# %%
a,b,c = 1,2,3

my = a,b,c
x,y,z = my

print(x,y,z)
print(my)

# %%
def f(a,b=1,c=2):
    print(a,b,c)
    
    
f(2, c=2)
f(c=100, a= 110)

# %%

bal = 1000

trn_type = int(input("Enter Selection 1. Balance, 2. Deposit, 3. Withdraw"))
if trn_type in (1,2,3):
    amt=0
    if trn_type == 2:
        amt = int(input("Enter Amount:"))
        bal= bal + amt
        print(bal)
        
    elif trn_type ==  3:
        amt = int(input("Enter Amount:"))
        bal= bal - amt
        print(bal)
        
    else: 
        print(" Your Bank balance ", bal)
        
        
else:
    print("Invalid Selection")
    


# %%




