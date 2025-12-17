#1.
'''
n=input('Enter customer name: ')
ad=input('Enter customer address: ')
am=int(input('Enter amount: '))
ty=input('Enter device (Laptop or Desktop): ').lower()
t=am
if am>100000:
    if ty=="laptop":
        t-=(10/100)*am
    elif ty=="desktop":
        t-=(15/100)*am
elif 57000<am<=100000:
    if ty=="laptop":
        t-=(7.5/100)*am
    elif ty=="desktop":
        t-=(10/100)*am
elif 25000<am<=57000:
    if ty=="laptop":
        t-=(5/100)*am
    elif ty=="desktop":
        t-=(7.5/100)*am
elif am<=25000 and ty=="desktop":
    t-=(5/100)*am
print('\nName: ',n)
print('Address: ',ad)
print('Amount: ',am)
print('Amount after Discount: ',t)
#'''

#2.
'''
class CloudStorage:
    def __init__(self,acc=0,sp=0):
        self.acc=acc
        self.sp=sp
        self.bill=0
    def accept(self):
        self.acc=int(input("Enter account number: "))
        self.sp=int(input("Enter storage space purchased (GB): "))
    def calculate(self):
        sp=self.sp
        if sp<=15:
            self.bill=sp * 15
        elif sp<=30:
            self.bill=(15*15)+(sp-15)*13
        else:
            self.bill=(15*15)+(15*13)+(sp-30)*11
    def display(self):
        print("\nAccount Number: ",self.acc)
        print("Storage Space: ",self.sp,)
        print("Bill Amount: ",self.bill)
cs=CloudStorage()
cs.accept()
cs.calculate()
cs.display()
#'''

#3
'''
import math
def area(a=None,b=None,c=None,h=None,d1=None,d2=None):
    if a is not None and b is not None and c is not None and h is None and d1 is None:
        s=(a+b+c)/2
        return math.sqrt(s*(s-a)*(s-b)*(s-c))
    if a is not None and b is not None and h is not None:
        return 0.5*h*(a+b)
    if d1 is not None and d2 is not None:
        return 0.5*d1*d2
print("Area of Scalene Triangle:",area(18,9,10))
print("Area of Trapezium:",area(17,15,h=9))
print("Area of Rhombus:",area(d1=12,d2=11))
#'''

#4
'''
s=int(input('Enter Sales amount'))
if s>100000:
    c=(25/100)*s
elif 80000<s<=100000:
    c=(22.5/100)*s
elif 60000<s<=80000:
    c=(20/100)*s
elif 40000<s<=60000:
    c=(15/100)*s
elif s<=40000:
    c=(25/100)*s
print('Commission of salesman:',c)
#'''

#5
'''
class Sales:
    def __init__(self,n,c):
        self.c=c
        self.n=n
        self.a=0

    def calculate(self):
        co=self.c
        if 20000<c<=30000:
            d=(10/100)*c
        elif 30000<c<=40000:
            d=(15/100)*c
        elif 40000<c<=50000:
            d=(18/100)*c
        elif c>50000:
            d=(20/100)*c
        else:
            print("Laptop price too low for discount.")
            return
        a=c-d
        a-=0.05*a
        a+=0.12*a
        self.a=a

    def display(self):
        print("Name:",self.n)
        print("Laptop Cost:",self.c)
        print("Laptop Cost after discount:",round(self.a,2))

n=input("Enter customer name: ")
c=float(input("Enter laptop cost: "))
s=Sales(n,c)
s.calculate()
s.display()
#'''

#6
'''
c=int(input("Enter the amount of no of liters of water consumed: "))
if c<=60:
    t=0
elif 60<c<=120:
    t=300
elif 120<c<=220:
    t=500
elif 220<c<=350:
    t=800
else:
    t=1200
print("Tax Ammount",t)
#'''

#7
'''
def getValue():
    a=int(input("Enter deposit amount: "))
    p=float(input("Enter time period in years: "))
    return a,p

def compute(a,p):
    if a<=100000 and p>=3:
        r=7.5
    elif a<=100000 and p<3:
        r=6.0
    elif a<=500000 and p>=3:
        r=8.25
    else:
        r=7.5
    i=(a*r*p)/100
    t=a+i
    return t

def printAmount(t):
    print("Total Amount Payable by Bank: Rs.",round(t,2))

a,p=getValue()
t=compute(a,p)
printAmount(total)
#'''

#8
'''
i=int(input("Enter the income"))
if i<=600000:
    t=(7.5/100)*i
elif 600000<i<=1000000:
    t=(7.5/100)*600000+(10/100)*(i-600000)
elif 1000000<i<=15000000:
    t=(7.5/100)*600000+((10/100)*1000000)+10000+((20/100)*(i-1000000))
else:
    t=(7.5/100)*600000+((10/100)*1000000)+10000+((20/100)*15000000)+20000+((30/100)*(i-15000000))
print("Tax amount:",t)
#'''

#9
'''
fl=int(input("Enter the floor number: "))
cl=input("Enter the class of the room: ").upper()
if fl==1:
    if cl=="A":
        ch=750
    elif cl=="B":
        ch=600
    elif cl=="C":
        ch=500
elif fl==2:
    if cl=="A":
        ch=1200
    elif cl=="B":
        ch=1000
    elif cl=="C":
        ch=300
elif fl==3:
    if cl=="A":
        ch=2500
    elif cl=="B":
        ch=1800
    elif cl=="C":
        ch=1200
print("Room charges:",ch)
#'''

#10
'''
def area(t):
    if t==1:
        r=float(input("Enter the radius of the circle: "))
        a=3.14*r*r
    elif t==2:
        s=float(input("enter the side if a square: "))
        a=s*s
    elif t==3:
        l=float(input("Enter the length of rectangle: "))
        b=float(input("enter the breadth of the rectangle: "))
        a=l*b        
    else:
        return "Enter a valid number"
    return a
print("1.Circle\n2.Square\n3.Rectangle")
t=int(input("Enter the number of the shape: "))
print(area(t))
#'''

#11
'''
n=input("Enter user name: ")
c=input("Enter user type (C/I/R): ").upper()
u=float(input("Enter KWH used: "))
b=0
if c=="C":
    if u<=1000:
        b=u*2.75
    elif u<=5000:
        b=1000*2.75+(u-1000)*3.90
    else:
        b=1000*2.75+4000*3.90+(u-5000)*4.25
elif c=="I":
    if u<=1000:
        b=u*2.75
    elif u<=4000:
        b=1000*2.75+(u-1000)*2.95
    elif u<=9000:
        b=1000*2.75+3000*2.95+(u-4000)*3.20
    else:
        b=1000*2.75+3000*2.95+5000*3.20+(u-9000)*4.50
elif c=="R"
    if u<=500:
        b=u*2.50
    elif u<=1000:
        b=500*2.50+(u-500)*3.25
    else:
        b=500*2.50+500*3.25+(u-1000)*4.15
else:
    print("Invalid user code")
print("User Name:",n)
print("User Type:",c)
print("Total KWH:",u)
print("Total Bill Amount: Rs.",round(b,2))
#'''

#12
'''
class Railways:
    def __init__(self,n="Unknown",age=0,d=0):
        self.n=n
        self.age=age
        self.d=d
        self.f=0
    def calculate_fare(self):
        age=self.age
        d=self.d
        if age<10:
            if d<10:
                self.f=5
            elif 10<=d<=50:
                self.f=20
            else:
                self.f=50
        elif 10<=age<=60:
            if d<10:
                self.f=10
            elif 10<=d<=50:
                self.f=40
            else:
                self.f=80
        else:
            if d<10:
                self.f=40
            elif 10<=d<=50:
                self.f=15
            else:
                self.f=35
    def display(self):
        print("Passenger Name:",self.n)
        print("Age :",self.age)
        print("Distance Travelled (km):",self.d,)
        print("Fare to Pay:", self.f)
n=input("Enter passenger name: ")
age=int(input("Enter age: "))
d=int(input("Enter distance traveled (km): "))
rail=Railways(n,age,d)
rail.calculate_fare()
rail.display()
#'''