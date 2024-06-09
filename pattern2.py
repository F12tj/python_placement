# n=int(input("enter the n value"))
# m=10
# while m:
#     m=m-1
#     for i in range (0,n+1):
#         for j in range (0,i+1):
#             print("*", end=" ")
#         print()


#     for i in range (0,n+1):
#         for j in range (0,n-i):
#             print("*", end=" ")
#         print()



#     for i in range(0,n):
#         for j in range(0,n):
#             if j<(n-i) :
#                 print(" ",end=" ")
#             elif j>=(n-i):
#                 print("*",end=" ")
#         print(" ")

#     for i in range(0,n):
#         for j in range(0,n):
#             if j>=(i) :
#                 print("*",end=" ")
#             elif j<=(i):
#                 print(" ",end=" ")
#         print(" ")

# def print_india():
#     pattern = [
#         "i  n n     n  dddd    i  a a a a ",
#         "i  n  n    n  d   d   i  a     a ",
#         "i  n   n   n  d    d  i  a a a a ",
#         "i  n    n  n  d   d   i  a     a ",
#         "i  n     n n  dddd    i  a     a "
#     ]
    
#     for line in pattern:
#         print(line)

# print_india()
#
# n=int(input("enter the value"))
# for i in range(n):
#     for j in range(n):
#         if i==0:
#             print("*",end=" ")
#         elif i==n-1:
#             print("*",end=" ")
#         elif j==n-1:
#             print("*",end=" ")
#         elif j==0:
#             print("*",end=" ")
#         else:
#             print(" ", end=" ")
#     print(" ")

#printing a hollow box
# for i in range(n):
#     for j in range(n):
#         if i == 0 or i == n - 1:
#             print("*", end=" ")
#         elif j == 0 or j == n - 1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()


#print a char in pattern
# n=int(input("enter the n value"))
# a=input("enter the string value")
# for i in range (n):
#     for j in range (n):
#         print(a,end=" ")
#     print()


#number from 1 to n incrementally in pattern
n=int(input("enter the n value"))
a=int(input("enter the initial value"))
for i in range (n):
    for j in range (n):
        print(a,end=" ")
        a=a+1
    print()