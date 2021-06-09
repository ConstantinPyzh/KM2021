import sys

def fibo(n, a, b, i=0):
    if i == n:
        print(str(n)+"th Fibonacci number is: "+str(a))
    else:
        i += 1
        fibo(n, b, a+b, i)

while True:
    print("If you want to quit, enter exit")
    if len(sys.argv) => 1:
        a = sys.argv[1]
    else:
        a = input("Enter Fibonacci number: ")
    if str(a) == "exit":
        break
    fibo(int(a), 0, 1)
    


