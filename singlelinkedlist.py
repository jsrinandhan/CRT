class Node:
    def __init__(self,ele):
        self.data=ele
        self.next=None
 
class SingleLinkedList:
    def __init__(self):
        self.head=None
    
    def insertFirst(self,ele):
        new=Node(ele)
        if self.head is None:
            self.head=new
            print(f'Inserted {ele} in the empty list.\n')
            return
        new.next=self.head
        self.head=new
        print(f'Inserted {ele} at Fisrt.\n')

    def insertEnd(self,ele):
        new=Node(ele)
        if self.head is None:
            self.head=new
            print(f'Inserted {ele} in the empty list.\n')
            return
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        temp.next=new
        print(f'Inserted {ele} at End.\n')

    def insertMiddle(self,ele,pos):
        if pos==1:
            self.insertFirst(ele)
            return
        temp,c=self.head,1
        while c!=pos-1 and temp.next is not None:
            temp,c=temp.next,c+1
        new=Node(ele)
        new.next=temp.next
        temp.next=new
        print(f'Inserted {ele} at {c+1} position.\n')
        

    def deleteFirst(self):
        if self.head is None:
            print('List is Empty.\n')
            return
        if self.head.next is None:
            print(f'Deleting {self.head.data}.\n')
            self.head=None
            return
        print(f'Deleting {self.head.data} from the End.\n')
        self.head=self.head.next

    def deleteEnd(self):
        if self.head is None:
            print('List is Empty.\n')
            return
        if self.head.next is None:
            print(f'Deleting {self.head.data}.\n')
            self.head=None
            return
        temp=self.head
        while temp.next.next is not None:
            temp=temp.next
        print(f'Deleting {temp.next.data} from the End.\n')
        temp.next=None

    def deleteMiddle(self,pos):
        if pos==1:
            self.deleteFirst()
            return
        temp,c=self.head,1
        while c!=pos-1:
            if temp.next is None:
                print('Postion is Invalid.\n')
                return
            temp,c=temp.next,c+1
        print(f'Deleting {temp.next.data} from the {pos} position.\n')
        temp.next=temp.next.next

    def display(self):
        if self.head is None:
            print('Linked List is empty.\n')
            return
        temp=self.head
        while temp:
            print(temp.data,end='-->')
            temp=temp.next
        print('None.\n')

    def search(self,ele):
        if self.head is None:
            print('List is Empty')
            return
        temp,c=self.head,1
        while temp.data!=ele:
            if temp.next is None:
                print('Element not Found')
                return
            temp,c=temp.next,c+1
        print(f'{ele} is found at position {c}')

sll=SingleLinkedList()
print('1. Insert at First\n2. Insert at End\n3. Insert at Position\n4. Delete from First\n5. Delete from End\n6. Delete from Position\n7. Display\n8. Search the Element\n9. Exit\n')
while True:
    ch=int(input('Enter Your Choice: '))
    match ch:
        case 1: 
            ele=int(input('Enter the Element: '))
            sll.insertFirst(ele)
        case 2:
            ele=int(input('Enter the Element: '))
            sll.insertEnd(ele)
        case 3:
            ele=int(input('Enter the Element: '))
            ind=int(input('Enter Index: '))
            sll.insertMiddle(ele,ind)
        case 4:
            sll.deleteFirst()
        case 5:
            sll.deleteEnd()
        case 6:
            ind=int(input('Enter Index: '))
            sll.deleteMiddle(ind)
        case 7:
            sll.display()
        case 8:
            ele=int(input('Enter the Element: '))
            sll.search(ele)
        case 9:
            print('Thank You')
            exit(0)
        case _:
            print('Choose Correct Option')