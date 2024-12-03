#to print the sum of all numbers between m and n (both included), using foor loops (m and n are user -defined inputs)
# m=int(input("enter the number from which you want to calculate the sum:"))
# n=int(input("enter the number upto which you want to calculate the sum:"))
# sum=0
# for i in range(m,n+1):
#     sum=sum+i
    
# print("sum:",sum)

#To take two numbers from the user and check if one number perfectly divides the other.
# m=int(input("enter the number 1 :"))
# n=int(input("enter the number 2:"))
# if m%n==0:
#     print(f"{n} divides {m} perfectly ")
# elif n%m==0:
#     print(f"{m} divides{n} perfectly")
# else:
#     print("neither of the two number divides the other number perfectly")

#  To print the area and perimeter of a circle if the diameter is given by the user.
# import math
# diameter=int(input("enter the diameter of circle "))
# perimeter=math.pi*diameter
# area=(math.pi*diameter**2)/4
# print("perimeter of circle is:",perimeter)
# print("area of circle is:",area)

# To print the factorial of a number given by the user.
# n=int(input("enter the number of which you want to calculate factorial:"))
# factorial=1
# for i in range(1,n+1):
#     factorial*=i
# print("factorial",factorial)

#print the pattern 
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j , end="")
    print()