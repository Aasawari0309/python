n = int(input("Enter the number to calculate factorial: "))

def factorial(a):
    if(a<2):
        return 1
    else:
        return a * factorial(a-1)
    
    
result = factorial(n)
print("The factorial of " , n , "is : ", result)