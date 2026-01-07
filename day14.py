class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

root=None

def level(root):
    s=[]
    s.append(root)
    while len(s)!=0:
        x=len(s)
        l=[]
        for i in range(x):
            t=s.pop(0)
            l.append(t.data)
            if t.left:
                s.append(t.left)
            if t.right:
                s.append(t.right)
        print(l)

def vertical(root):
    s=[]
    s.append(root)
    while len(s)!=0:
        x=len(s)
        l=[]
        for i in range(x):
            t=s.pop(0)
            l.append(t.data)
            if t.left:
                s.append(t.left)
            if t.right:
                s.append(t.right)
        print(l)

root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.right.left=Node(6)
root.right.right=Node(7)
level(root)
vertical(root)