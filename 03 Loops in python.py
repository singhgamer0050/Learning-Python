#1 Print number from 1 to 100
i=1
while i<=100:
    print(i)
    i+=1

#2 Print number from 100 to 1
j=100
while j>=1:
    print(j)
    j-=1

#3 Print the multiplication table of number n
n =int(input("Enter your number"))
i=1
while i<=10:
    print(i*n)
    i+=1

#4 Print element of following list using loop [1,4,9,16,25,36,49,64,81,100]
i=1
while i<=10:
    print(i**2)
    i+=1

                # OR

num=[1,4,9,16,25,36,49,64,81,100]
ind=0
while ind< len(num):
    print(num[ind])
    ind+=1

#5 search for number x in this tuple using loop : (1,4,9,16,25,36,49,64,81,100)
tup=(1,4,9,16,25,36,49,64,81,100)
x=int(input("Enter what you want from List:"))
k=1
while k < len(tup):
    if(tup[k]==x):
        print("Found at index:",k)
    else:
        print("Not found at index:",k)
    k+=1

#6 Print the Elements of the folloeing list [1,4,9,16,25,36,49,64,81,100]
lst=[1,4,9,16,25,36,49,64,81,100]
for el in lst:
    print(el)
else:
    print("End")

#7 Search for the number x in this tupple using loop (1,4,9,16,25,36,49,64,81,100)
tp=(1,4,9,16,25,36,49,64,81,100)
q=int(input("Enter what you want from tp:"))
t=0
for e in tp:
    if e==q:
        print(e)
        print("Found at index",t)
    t+=1

#8 Print number from 1 to 100 using Range 
y=1
for y in range(1,101,1):
    print(y)
    y+=1

#9 Print number from 100 to 1 using Range
z=100
for z in range(100,0,-1):
    print(z)
    z-=1

#10 Print the multiplication table of n using range
b=int(input("Enter the number for table:"))
for p in range(1,11,1):
    print(b*p)
    p+=1

#11 To find the sum of first n number using For loop
c=int(input("Enter the number till you want sum:"))
sum =0
for d in range (c+1):
    sum += d
print("Total sum is:",sum)

#12 To find the sum of first n number While For loop
c=int(input("Enter the number till you want sum:"))
sum =0
e=1
while e<=c:
    sum += e
    e += 1
print("Total sum is:",sum)

#13 Write a program to find the factorial of first n number using  loop
f=int(input("Enter the number for factorial:"))
fact=1
g =1
while g<=f:
    fact *= g
    g += 1
print("Factorial is:",fact)

#Print * patern
print("Star Pattern")
for i in range(1, 5):
    print("*" * i)