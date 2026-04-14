#Program to find the sum of 'n' natural numbers forward iteration/looping
n = int(input("Enter the 'n' value: "))
if n < 1:
    print("Please enter a natural number")
else:
    s = 0                                                 #For Reverse iteration/Backward looping, s = n
    for i in range(n+1):                           #for i in range(n-1, 0, -1)
        s += i
    print("The sum of first", n, "natural numbers is", s)


#Better approach s = n * (n + 1) // 2

#Recursion
#def sum_n(n):
#    if n == 0:
#       return 0
#    return n + sum_n(n-1)    
