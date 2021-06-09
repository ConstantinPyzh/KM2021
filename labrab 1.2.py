import sys

def fibo(n, a, b, i=0):
    if i == n:
        print(str(n)+"th Fibonacci number is: "+str(a))
    else:
        i += 1
        fibo(n, b, a+b, i)

while True:
    print("If you want to quit, enter exit")
    b=int(sys.argv[1])
    if str(a) == "exit":
        break
    if b:
        fibo(b, 0, 1)
    else:
        a=int(input("Enter number: "))
        fibo(a, 0, 1)


