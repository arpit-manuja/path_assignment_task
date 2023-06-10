

factorial = lambda x : 1 if x==0 else x * factorial(x-1)

num = int(input("Enter the number for which you want to find factorial"))


print(factorial(num))
 
