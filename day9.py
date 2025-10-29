'''
def anagram(s):
    d=dict()
    for ch in s:
        d[ch]=d[ch]+1 if ch in d.keys() else 1
    return d
s1,s2=input().split(",")
print("Anagram" if anagram(s1)==anagram(s2) else "Not an Anagram") if len(s1)==len(s2) else print("Not an Anagram")
#'''
#print("Anagram" if sorted(input().lower())==sorted(input().lower()) else "Not an Anagram")
'''
s=input().lower()
s.replace(" ",'')
d={}
for ch in s:
    if ch in 'qwertyuiopasdfghjklzxcvbnm':
        d[ch]=1
print('Panagram' if len(d)==26 else 'Not a Panagram')
#'''
'''
s,a=input().lower(),input().lower()
m,n,d,w=len(s),len(a),dict(),dict()
for ch in a:
    d[ch]=d[ch]+1 if ch in d else 1
i,c=0,0
for j in range(m):
    w[s[j]]=w[s[j]]+1 if s[j] in w else 1
    if j-i+1==n:
        if d==w:
            c+=1
        w[s[i]]-=1
        if w[s[i]]==0:
            w.pop(s[i])
        i+=1
print(c)
#'''
#'''
s,a=input().lower(),input().lower()
m,n,d,w=len(s),len(n),dict(),dict()
for ch in a:
    d[a]=d[a]+1 if ch in d else 1
i=0
for j in range(m):
    w[s[j]]=w[s[j]]+1 if s[j] in w else 1
    if 
    j+=1
#'''