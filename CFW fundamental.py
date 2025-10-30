#1 Input and Output of all basic types
'''
a=int(input())
b=float(input())
c=input()
print(f'{a}')
print(f'{b}')
print(f'{c}')
#'''

#2 Sum of two numbers
'''
a=eval(input())
b=eval(input())
print(f'Sum= {a+b}')
#'''
'''
a,b=map(eval,input().split(","))
print(f'Sum= {a+b}')
#'''

#3 Perform all arithmatic operations on two numbers
'''
a=eval(input())
b=eval(input())
print(f'Sum= {a+b:.3f}')
print(f'Difference= {a-b:.3f}')
print(f'Product= {a*b:.3f}')
print(f'Quotient= {a//b:.3f}')
print(f'Modulus= {a%b:.3f}')
#'''
'''
a,b=map(eval,input().split(","))
print(f'Sum= {a+b:.3f}')
print(f'Difference= {a-b:.3f}')
print(f'Product= {a*b:.3f}')
print(f'Quotient= {a//b:.3f}')
print(f'Modulus= {a%b:.3f}')
#'''

#4&5 Area and Perimeter of Rectangle
'''
l=eval(input())
b=eval(input())
print(f'Perimeter= {2*(l+b)}')
print(f'Area= {l*b}')
#'''
'''
l,b=map(eval,input().split(","))
print(f'Perimeter= {2*(l+b)}')
print(f'Area= {l*b}')
#'''

#6 Area, Circumference and Diameter of Circle
'''
r=eval(input())
print(f'Diameter= {r*2}')
print(f'Circumference= {2*r*3.14}')
print(f'Area= {3.14*(r**2)}')
#'''

#7 Centimeter to Meter and Kilometer
'''
c=eval(input())
print(f'{c/(10**2)} Meters')
print(f'{c/(10**5)} Kilometers')
#'''

#8 Celsius to Fahrenheit
'''
print(f'{((eval(input())*9)/5)+32:.3f} Fahrenheit')
#'''

#9 Fahrenheit to Celsius
'''
print(f'{((eval(input())-32)*5)/9:.3f} Celsius')
#'''

#10 Convert days into years, weeks and days
'''
d=int(input())
y=d//365
w=(d-(y*365))//7
d=(d-((y*365)+(w*7)))
print(f'{y} Years, {w} Weeks, {d} Days')
#'''

#11 Power of any number x^y
'''
a=eval(input())
b=eval(input())
print(f'{a**b:.3f}')
#'''
'''
a,b=map(eval,input().split(","))
print(f'{a**b:.3f}')
#'''

#12 Square Root
'''
a=eval(input())
print(f'{a**0.5:.3f}')
#'''

#13 Find 3rd angle of triangle
'''
a=eval(input())
b=eval(input())
print(f'{180-(a+b)}')
#'''
'''
a,b=map(eval,input().split(","))
print(f'{180-(a+b)}')
#'''

#14 Area of a Triangle
'''
b=eval(input())
h=eval(input())
print(f'Area= {(b*h)/2:.3f}')
#'''

#15 Area of Equilateral Triangle
'''
s=eval(input())
print(f'Area= {((3**0.5)/4)*(s**2):.3f}')
#'''

#16 Calculate total, average and percentage of five subjects marks
'''
s=0
for i in range(5):
    m=int(input())
    s+=m
print(f'Sum= {s}')
print(f'Average= {s/5:.3f}')
print(f'Percentage= {(s/500)*100:.3f}')
#'''

#17 Simple interest
'''
p,t,r=map(eval,input().split(","))
print(f'Simple Interest= {(p*t*r)/100}')
#'''

#18 Compound interest
'''
p,t,r=map(eval,input().split(","))
print(f'Compound Interest= {p*((1+(r/100))**t):.3f}')
#'''