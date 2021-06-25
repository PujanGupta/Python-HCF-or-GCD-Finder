def findHCF(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
        
    for i in range(1, smaller + 1):
        if ((x % i == 0) and (y % i == 0)):
            hcf = i
        else:
            continue
        
    return hcf

while True:
    Num1 = int(input("Number 1: "))
    Num2 = int(input("Number 2: "))
    
    print(f"The HCF or GCD of {str(Num1)} and {str(Num2)} is {str(findHCF(Num1, Num2))}")