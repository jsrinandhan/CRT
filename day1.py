'''
import math as m
n=int(input())
d=int(m.log10(n))
print(f'{((n%(10**d))*10)+(n//(10**d))}')
print(f'{((n%10)*(10**d))+(n//10)}')
print(f'{((n%10)*(10**d))+(((n%(10**d))//10)*10)+(n//(10**d))}')
#'''