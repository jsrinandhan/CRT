class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

class DoubleLinkedList:
    def __init__(self):
        self.head=None
    
    def insertFirst(self,ele):
        new=Node(ele)
        if self.head is None:
            self.head=new
            print(f'{ele} inserted in the Empty List.\n')
            return
        self.head.prev=new
        new.next=self.head
        self.head=new
        print(f'Inserted {ele} at Fisrt.\n')

    def insertLast(self,ele):
        new=Node(ele)
        if self.head is None:
            self.head=new
            print(f'{ele} inserted in the Empty List.\n')
            return
        curr=self.head
        while curr.next is not None:
            curr=curr.next
        curr.next=new
        new.prev=curr
        print(f'Inserted {ele} at Last.\n')

    def insertPos(self,ele,pos):
        if pos==1:
            self.insertFirst(ele)
            return
        new,curr=Node(ele),self.head
        for i in range(pos-2):
            if curr.next is None:
                break
            curr=curr.next
        new.next=curr.next
        new.prev=curr
        if curr.next is not None:
            curr.next.prev=new
        curr.next=new
        print(f'Inserted {ele} at {pos} position.\n')

    def deleteFirst(self):
        if self.head is None:
            print('List is Empty.\n')
            return
        if self.head.next is None:
            print(f'Deleting {self.head.data}.\n')
            self.head=None
            return
        print(f'Deleting {self.head.data} from the First.\n')
        self.head=self.head.next
        self.head.prev=None

        
    def deleteLast(self):
        if self.head is None:
            print('List is Empty.\n')
            return
        if self.head.next is None:
            print(f'Deleting {self.head.data}.\n')
            self.head=None
            return
        curr=self.head
        while curr.next is not None:
            curr=curr.next
        print(f'Deleting {curr.data} from the Last.\n')
        curr.prev.next=None

    def deletePos(self,pos):
        if pos==1:
            self.deleteFirst()
            return
        if self.head is None:
            print('List is Empty.\n')
            return
        curr=self.head
        for i in range(pos-1):
            if curr.next is None:
                print('Postion is Invalid.\n')
                return
            curr=curr.next
        curr.prev.next=curr.next
        if curr.next is not None:
            curr.next.prev=curr.prev
        print(f'Deleting {curr.data} from the {pos} position.\n')

    def display(self):
        if self.head is None:
            print('Linked List is empty.\n')
            return
        curr=self.head
        while curr:
            print(curr.data,end='<-->')
            curr=curr.next
        print('None.\n')

    def search(self,ele):
        if self.head is None:
            print('List is Empty')
            return
        curr,c=self.head,1
        while curr.data!=ele:
            if curr.next is None:
                print(f'{ele} is Not Found')
                return
            curr,c=curr.next,c+1
        print(f'{ele} is found at position {c}')

dll=DoubleLinkedList()    
print('1. Insert at First\n2. Insert at Last\n3. Insert at Position\n4. Delete from First\n5. Delete from Last\n6. Delete from Position\n7. Display\n8. Search the Element\n9. Exit\n')
while True:
    ch=int(input('Enter Your Choice: '))
    match ch:
        case 1: 
            ele=int(input('Enter the Element: '))
            dll.insertFirst(ele)
        case 2:
            ele=int(input('Enter the Element: '))
            dll.insertLast(ele)
        case 3:
            ele=int(input('Enter the Element: '))
            pos=int(input('Enter Position: '))
            dll.insertPos(ele,pos)
        case 4:
            dll.deleteFirst()
        case 5:
            dll.deleteLast()
        case 6:
            pos=int(input('Enter Position: '))
            dll.deletePos(pos)
        case 7:
            dll.display()
        case 8:
            ele=int(input('Enter the Element: '))
            dll.search(ele)
        case 9:
            print('Thank You!')
            exit(0)
        case _:
            print('Invalid Option, Choose Correct Option.\n')