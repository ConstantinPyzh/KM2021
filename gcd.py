import sys

def NOD(x, y):
    if x%y == 0:
        print("Greatest Common Divisor: "+str(y))
    else:
        NOD(y,x%y)

def NOK(x, y):
    gcd=(x*y)/NOD(x, y)
    print("Smallest Common Multiple: "+str(gcd))
    
while True:
    print("Enter numbers as A B. Enter Ex to exit")
    a=input("enter first number: ")
    b=input("enter second number: ")
    
    if str(a) or str(b) == "Ex":
        break
    if type(a) != int and type(b) != int:
        print("Error! Number must be integer! Try again")
    if a > b:
        greater = a
        smaller = b
    else:
        greater = b
        smaller = a
    NOD(greater, smaller)
    NOK(greater, smaller)
    
        
        
                
                
