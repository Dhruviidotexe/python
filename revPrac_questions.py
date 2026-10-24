a= 10
b= 20
type(a)
c= a+b
d= a-b
e= a*b
f= a/b
g= a//b
print(c)
print(d)
print(e)
print(f)
print(g)
h= a==b
print(h)

## ____________________________ 

a= 10
b=5
c= a==b
d= a>=b
e= a<=b
f= a!=b
print(c)
print(d)
print(e)
print(f)

## ____________________________ 

i_n = 123
f_n= 1.23
a_n= i_n + f_n
print(a_n)
type(f_n)
type(i_n)
type(a_n)

## ____________________________ 


a='12'
c= 12
type(a)
b= int(a)
print(type(b))

## ____________________________ 

# Display "hello world"
print("hello world")

## ____________________________ 

# print your name, college name and course name
print("Name= Dhruvi Verma")
print("College Name= Pes University")
print("Course: MCA")

## ____________________________ 

# Perform all the sirthmetic operations on A and B without taking input
A= 10
B= 50
print("Addition of these numbers: ", A+B)
print("substraction of these numbers: ", A-B)
print("Multiplication of these numbers: ", A*B)
print("Division of these numbers: ", A/B)
print("square of these numbers: ", A**B)
print("Modulus of these numbers: ", A%B)

## ____________________________ 

# Find which number is greater
a= 10
b= 20
print(a>b)
print(a<b)
print(a==b)
print(a!=b)
print(a>=b)
print(a<=b)

## ____________________________ 


#declare name of two students and also declare their marks, then compare their marks.
student1= "Dhruvi"
student2= "dhairya"
marks1= 20
marks2= 21
print(marks1<marks2)

## ____________________________ 

# Logical Operators
print(True or False)
print(False or True)
print(True or True)
print(False or False)

## ____________________________ 

print(12 & 5)
print(12 | 5)
print(5>>2)
print(5<<1)

a,b = 12,5
print(bin(a))
print(bin(b))

print(5 & 3)
print(bool(5) and bool(3))

## ____________________________ 

# Calculating the simple interest
p= float(input("principal : "))
r= float(input("Rate of Interest: "))
t= float(input("Time: "))
print("SIMPLE INTEREST: ", p*r*t/100)

## ____________________________

a=input("firstvalue: ")
b=input("secondvalue: ")
temp= a
a=b
b= temp
print("After swap:", a,b)

## ____________________________

# membership operators
a=[1,2,3,4,5]
print(5 in a)
print(10 not in a)

## ____________________________

word='python'
print('y' in word)
print('j' not in word)

## ____________________________

students=["arun", "ravi", "meena"]
name=input("students name: ")
print(name in students)

## ____________________________

# Identity Operator
a=[1,2,3]
a=b
print(a is b)

## ____________________________

x=[10,20]
y=[10,20]
print(x==y)
print(x is y)

## ____________________________

value= 10
print(value is not None)
print(value is None)
value= None
print(value is None)

## ____________________________

a=[1,2]
b=a
print(a is b)
print(a is not b)

## ____________________________

a,b= 12,4
print(a=b-2*b/2)

## ____________________________

print((2+ 3) * 4)

## ____________________________

n = int(input("numbers: "))
print(n > 0 and n% 2== 0 and n<100)

## ____________________________

n = int(input("numbers: "))
a=n%2==0
b=n%2==0
print((a or b) and not (a and b))

## ____________________________


ch = input("Enter one character: ").lower()
print(len(ch) == 1 and ch in "aeiou")

## ____________________________

x=5
y=10
print(x+y)

## ____________________________

x='15'
print(int(x)+ 20)

## ____________________________

x= 3.5
y= 4.7
z= print(int(x)+ int(y))

## ____________________________

name= "dhruvi"
print(name.capitalize())
print(name.upper())
print(name.lower())
print(name.isalnum())
print(name.islower())
print(name.isdigit())

## ____________________________


print("banana".count("a"))

## ____________________________

a={5,8,6,4}
print(a)

## ____________________________

a= [1,2,3,4,5]
print(a)
b=[1,2,3,8,5,6,4]
print(a)

## ____________________________

a= [1,2,3,4,5]
print(a)
b=[1,2,3,8,5,6,4]
print(a)
print(a + b)

## ____________________________

list = ["abc", 1.2, 1]
print(list)

## ____________________________

