'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class SingleLinkedList:
    def __init__(self):
        self.head=None
    
    def insertFirst(self,ele):
        new=Node(ele)
        if self.head is None:
            self.head=new
            return
        new.next=self.head
        self.head=new

    def insertEnd(self,ele):
        new=Node(ele)
        if self.head is None:
            self.head=new
            return
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        temp.next=new

    def display(self):
        if self.head is None:
            print('Linked List is empty.\n')
            return
        temp=self.head
        while temp:
            print(temp.data,end='-->')
            temp=temp.next
        print('None.\n')

    def rotateR(self):
        if self.head is None:
            print('List is Empty.\n')
            return
        if self.head.next is None:
            print('Only one element in the list.\n')
            return
        curr=self.head
        while curr.next.next is not None:
            curr=curr.next
        curr.next.next=self.head
        self.head=curr.next
        curr.next=None
#'''
        

#1.Prime Number
'''
def check(ele):
    c=0
    if ele==0 or ele==1:
        return True
    for i in range(2,int(ele**0.5)+1):
        if ele%i==0:
            if i==ele/i:
                c+=1
            else:
                c+=2
        if c>0:
            return False
    return True

sll=SingleLinkedList()
while input('Do you want enter data: ').lower()=='y':
    ele=int(input('Enter number: '))
    if check(ele):
        sll.insertFirst(ele)
    else:
        sll.insertEnd(ele)
    sll.display()
#'''

#2.Rotate
'''
sll=SingleLinkedList()
n=int(input())
for i in range(n):
    sll.insertFirst(int(input('Enter a Number: ')))
k=int(input('Number of Rotations: '))
for i in range(k):
    sll.rotateR()
    sll.display()
#'''

#3 BST
#'''
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class BinaryTree:
    def __init__(self):
        self.root=None
    
    def insert(self,ele):
        new=Node(ele)
        if self.root is None:
            self.root=new
            return
        l=[self.root]
        while l:
            curr=l.pop(0)
            if curr.left is None:
                curr.left=new
                return
            l.append(curr.left)
            if curr.right is None:
                curr.right=new
                return
            l.append(curr.right)
    
    def preOrder(self):
        if self.root is None:
            print('NO elements')
            return
        l=[self.root]
        while l:
            curr=l.pop()
            print(curr.data,end=',')
            if curr.right is not None:
                l.append(curr.right)
            if curr.left is not None:
                l.append(curr.left)

bt=BinaryTree()
while input('Do you want to enter: ').lower()=='y':
    bt.insert(int(input('Enter a Number: ')))
bt.preOrder()
#'''