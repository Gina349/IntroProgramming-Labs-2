n = int(input("Please type a number...\n"))
    
def fibonacci(n):

    Phi = ((1 + 5**0.5)/2)
    phi = ((1 - 5**0.5)/2)

    return ((Phi**n - (phi)**n) / 5**0.5)

print (int((fibonacci(n))))

