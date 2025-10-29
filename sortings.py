#selection sort
'''
l=eval(input())
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]>l[j] :
            l[i],l[j]=l[j],l[i]
print(*l)
#'''

#bubble sort
'''
l=eval(input())
for i in range(len(l)-1):
    for j in range(len(l)-i-1):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
print(*l)
#'''

#insertion sort
#'''
l=eval(input())
for i in range(len(l)-1):
    for j in range(len(l)-i-1):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
print(*l)
#'''