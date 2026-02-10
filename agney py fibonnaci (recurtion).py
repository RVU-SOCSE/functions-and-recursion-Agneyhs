#1RUA25BCA0008
#AGNEY HS
#fibonnaci of a number using recurtion

def fibonnaci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonnaci(n - 1)+fibonnaci(n - 2)

    num = int(input("enter the number"))
    for i in range(num):
        print(fibonnaci(i),end="")
