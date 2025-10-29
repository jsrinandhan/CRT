#1 print day of week name using switch case
'''
n=int(input())
match n:
    case 1: print("Monday")
    case 2: print("Tuesday")
    case 3: print("Wednesday")
    case 4: print("Thursday")
    case 5: print("Friday")
    case 6: print("Saturday")
    case 7: print("Sunday")
    case _: print("Invalid")
#'''

#2 print number of days in month using switch case
'''
n=int(input())
match n:
    case 1|3|5|7|8|10|12:
        print("31 days")
    case 4|6|9|11:
        print("30 days")
    case 2:
        print("28 days")
    case _:
        print("Invalid month number")
#'''

#3 alphabet is vowel or consonant using switch case
'''
a=input().lower()
match a:
    case 'a'|'e'|'i'|'o'|'u': print("Vowel")
    case _: print("Consonent")
#'''

#4 maximum between two numbers using switch case
'''
a,b=map(eval,input().split(","))
match m>n:
    case True: print(m)
    case False: print(n)
#'''

#5 number is even or odd using switch case
'''
a=int(input())
match a%2==0:
    case True: print("Even")
    case False: print("Odd")
#'''

#6 number is positive, negative or zero
'''
a=int(input())
match a>0:
    case True: print("Positive")
    case False: print("Negitive")
#'''

#7 find roots of a quadratic equation using switch case
'''
a,b,c=map(int,input().split(","))
d=((b**2)-(4*a*c))**0.5
match d>0:
    case True:
        r1=((-b-d)/(2*a))
        r2=((-b+d)/(2*a))
#'''

#8 Simple Calculator using switch case
'''
a,b=map(eval,input().split(","))
o=input()
match o:
    case '+': print(a+b)
    case '-': print(a-b)
    case '*': print(a*b)
    case '/': print(a/b)
    case '%': print(a%b)
#'''