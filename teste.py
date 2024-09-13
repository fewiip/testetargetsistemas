num = int(input("insira o numero\n"))

def testFibonacci(num):
    temp = 0
    while fib(temp) <= num :
        if fib(temp) == num :
            print("pertence")
            return True
        temp = temp + 1
    print("nao pertence")
    return False
    
def fib(x):
    if x == 0:
        return 0
    if x == 1 :
        return 1
    if x == 2 :
        return 1
    else : 
        return fib(x-1) + fib(x -2)            

testFibonacci(num)




