#1 Create a function to calculate average of 3 number
# def avg_num(a,b,c):
#     av=((a+b+c)/3)
#     print(av)
#     return av
# avg_num(3,2,4)

#2 Write a function to print the length of a list. (List is the parameter)
# city=["Delhi", "Noida", "Ghazipur"]
# def lst_len(list):
#     print(len(list))
#     return list
# lst_len(city)

#3 Write a function to print the elements of a list in a single line
# place=["Delhi", "Noida", "Ghazipur"]
# def pr_lst(line):
#     print(line)
#     return(line)
# pr_lst(place)

#4 Write a function to find the factorial of n. (n is parameter)
# def fact_n(n):
#     fact=1
#     g =1
#     while g<=n:
#         fact *= g
#         g += 1
#     print("Factorial is:",fact)
# fact_n(5)

#5 Write a function to convert USD to INR
# def us_ir(u):
#     ir=u*96
#     print(u,"USD","=",ir,"INR")
#     return(ir)
# us_ir(10)

#6 Write a function to check whether entered number is odd or even
# def odd_evn():
#     x=int(input("Enter your number:"))
#     if x%2 ==0:
#         print("Entered number is Even")
#     else:
#         print("Entered number is odd")
# odd_evn()

#7 Write a function to print n to 1 backwads
# n=int(input("Enter number for recursion:"))
# def rec_fn(n):
#     if (n==0):
#         return
#     print(n)
#     rec_fn(n-1)
# rec_fn(n)

#8 Write a function to return n!
# def fact_n(f):
#     if (f == 0 or f==1):
#         return 1
#     else:
#         return f * fact_n(f-1)
# print(fact_n(5))

#9 Write a recursive function to calculate the sum of first n natural numbers
# def sum_n(c):
#     if (c==0):
#         return 0
#     return sum_n(c-1) + c
# print(sum_n(5))

#10 Write a recursive function to print all elements in a list (Hint:- use list and index as parameter)
def list_prt (list, idx=0):
    if (idx == len(list)):
        return
    print(list[idx])
    list_prt(list,idx+1)
    return
frt=["apple", "orange", "banana"]
list_prt(frt)