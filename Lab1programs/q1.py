'''def countdown(n):
    print(n)    
    if n>0:
        return countdown(n-1)
    elif n==0:
        return 0
n=int(input("Enter the number of counts:"))
countdown(n)
print("Lauch")'''
'''def CI(p,n):
    if n==0:
        return 1
    else:
        return (CI(p,n-1))*p
    
P=int(input("Enter the principal growth :"))
N=int(input("Enter number of years:"))
print(CI(P,N))'''
'''def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return fact(n-1)*n
N=int(input("Enter the number whose factorial has to be calculated :"))
print(fact(N))'''
'''def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
N=int(input("Enter the number of ele,ents of fibanocci series are to be displayed :"))
for i in range(N):
    print(fib(i), end=" ")'''
def search(arr, target, i):
    if i >= len(arr):
        return -1 
    if arr[i] == target:
        return i + 1
    else:
        return search(arr, target, i + 1)

A = [1, 2, 3, 4]
print(search(A, 2, 0))  

