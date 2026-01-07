#AVL Tree
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class AVLTree:
    def __init__(self):
        self.root=None

    def insertNode(self,ele):
        new=Node(ele)
        if self.root is None:
            self.root=new
            print(f'Inserted {ele} in the empty tree.\n')
            return
        queue=[self.root]
        while queue:
            curr=queue.pop(0)
            if curr.left is None:
                curr.left=new
                print(f'Inserted {ele} at left of {curr.data}.\n')
                return
            if curr.left!='n':
                queue.append(curr.left)
            if curr.right is None:
                curr.right=new
                print(f'Inserted {ele} at right of {curr.data}.\n')
                return
            if curr.right!='n':
                queue.append(curr.right)
    
    def display(self):
        if self.root is None:
            print('No elements in the Tree.\n')
            return
        queue=[self.root]
        while queue:
            curr=queue.pop(0)
            print(curr.data,end=' ')
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        print()
    
    def balanced(self,node):
        if node is None:
            return True
        l=self.height(node.left)
        r=self.height(node.right)
        if abs(l-r)>1:
            return False
        return self.balanced(node.left) and self.balanced(node.right)
    
    def height(self,node):
        if node is None:
            return 0
        l=self.height(node.left)
        r=self.height(node.right)
        return 1+max(l,r)

avl=AVLTree()
print('1.Insert\n2.Display\n3.Balanced or Not\n4.Exit\n')
while True:
    ch=int(input('Enter your Choice: '))
    match ch:
        case 1:
            avl.insertNode(input('Enter the Element: '))
        case 2:
            avl.display()
        case 3:
            if avl.balanced(avl.root):
                print('Tree is balanced.\n')
            else:
                print('Tree is not balanced.\n')
        case 4:
            print('Exit.\n')
            break
        case _:
            print('Invalid Choice.\n')