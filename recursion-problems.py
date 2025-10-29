#cube of an number
'''
def pow(n,p=3):
    if p==1:
        return n
    return n*pow(n,p-1)
print(pow(int(input())))
#'''
#printing n natural numbers
'''
def nat(n,f=1):
    if f>n:
        return
    print(f,end=" ")
    nat(n,f+1)
nat(int(input()))
#'''
#printing even and odd numbers
#'''
def even(l,n):
    if(l>n-1):
        return n
    if(l%2==0):
        print(l,end=" ")
    return even(l+1,n)
def odd(l,n):
    if(l>n-2):
        return n-1
    if(l%2==1):
        print(l,end=" ")
    return odd(l+1,n)
l=1
n=int(input())
print(even(l,n))
print(odd(l,n))
#'''
#reverse of a number
'''
def rev(n,r=0):
    if n==0:
        return r
    return rev(n//10,r*10+n%10)
print(rev(int(input())))
#'''
#sum of n natural numbers
'''
def snat(n,f=1):
    if f==n:
        return n
    return f+snat(n,f+1)
print(snat(int(input())))
#'''
#sum of all even and odd numbers
'''
def even(l,n):
    if(l>n-1):
        return 0
    if(l%2==0):
        return l + even(l+1,n)
    return even(l+1,n)
def odd(l,n):
    if(l>n-2):
        return 0
    if(l%2==1):
        return l + odd(l+1,n)
    return odd(l+1,n)
l=1
n=int(input())
print(even(l,n))
print(odd(l,n))
#'''
# number is palindrome or not
'''
def rev(n,r=0):
    if n==0:
        return r
    return rev(n//10,r*10+n%10)
n=int(input())
if n==rev(n):
    print(n,"is a Palindrome")
else:
    print(n,"is not a palindrome")
#'''
#sum of digits of a numbers
'''
def sum(n):
    if n==0:
        return 0
    return (n%10)+sum(n//10)
print(sum(int(input())))
#'''
#factorial of a number
'''
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
print(fact(int(input())))
#'''
