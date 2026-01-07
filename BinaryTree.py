
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class BinaryTree:
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
            queue.append(curr.left)
            if curr.right is None:
                curr.right=new
                print(f'Inserted {ele} at right of {curr.data}.\n')
                return
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

    def preOrder(self):
        if self.root is None:
            print('No elements in the Tree.\n')
            return
        stack=[self.root]
        while stack:
            curr=stack.pop()
            print(curr.data,end=' ')
            if curr.right is not None:
                stack.append(curr.right)
            if curr.left is not None:
                stack.append(curr.left)
        print()
            
    def postOrder(self):
        if self.root is None:
            print('No elements in the Tree.\n')
            return
        stack1=[self.root]
        stack2=[]
        while stack1:
            curr=stack1.pop()
            stack2.append(curr)
            if curr.left is not None:
                stack1.append(curr.left)
            if curr.right is not None:
                stack1.append(curr.right)
        print(*[node.data for node in stack2[::-1]])

    def inOrder(self):
        if self.root is None:
            print('No elements in the Tree.\n')
            return
        stack=[]
        curr=self.root
        while stack or curr:
            while curr is not None:
                stack.append(curr)
                curr=curr.left
            curr=stack.pop()
            print(curr.data, end=' ')
            curr=curr.right

    def deleteNode(self,ele):
        if self.root is None:
            print('No elements in the Tree.\n')
            return
        queue=[self.root]
        while queue:
            curr=queue.pop(0)
            if curr.left and curr.left.data==ele:
                curr.left=None
                print(f'Deleted {ele}.\n')
                return
            if curr.right and curr.right.data==ele:
                curr.right=None
                print(f'Deleted {ele}.\n')
                return
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        print(f'{ele} is not found.\n')

    def delete(self,ele):
        if self.root is None:
            print('No elements in the Tree.\n')
            return
        if self.root.data==ele:
            if self.root.left:
                temp=self.root.right
                self.root=self.root.left
                curr=self.root
                while curr.right:
                    curr=curr.right
                curr.right=temp
            else:
                self.root=self.root.right
            print(f'Deleted {ele}.\n')
            return
        queue=[self.root]
        while queue:
            curr=queue.pop(0)
            if curr.left and curr.left.data==ele:
                curr.left=curr.left.right
                print(f'Deleted {ele}.\n')
                return
            if curr.right and curr.right.data==ele:
                curr.right=curr.right.left
                print(f'Deleted {ele}.\n')
                return
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        print(f'{ele} is not found.\n')

    def leafNode(self):
        s=[]
        s.append(self.root)
        while len(s)!=0:
            t=s.pop(0)
            if t.left is None and t.right is None:
                print(t.data,end=' ')
            if t.left:
                s.append(t.left)
            if t.right:
                s.append(t.right)
        print()

    def search(self,ele):
        if self.root is None:
            print('No elements in the Tree.\n')
            return
        curr=self.root
        queue=[curr]
        while queue:
            curr=queue.pop(0)
            if curr.data==ele:
                print(f'{ele} is found.\n')
                return
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)         
        print(f'{ele} is not found.\n')

    def levelOrder(self):
        s=[]
        s.append(self.root)
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
        print()

    def verticalOrder(self):
        d=dict()
        s=[[self.root,0]]
        while len(s)!=0:
            t=s.pop(0)
            if t[1] in d.keys():
                d[t[1]].append(t[0].data)
            else:
                d[t[1]]=[t[0].data]
            if t[0].left:
                s.append([t[0].left,t[1]-1])
            if t[0].right:
                s.append([t[0].right,t[1]+1])
        for i in sorted(d.keys()):
            print(d[i])
        print()

    def topView(self):
        d=dict()
        s=[]
        s.append([self.root,0])
        while len(s)!=0:
            t=s.pop(0)
            if t[1] not in d.keys():
                d[t[1]]=t[0].data
            if t[0].left:
                s.append([t[0].left,t[1]-1])
            if t[0].right:
                s.append([t[0].right,t[1]+1])
        for i in sorted(d.keys()):
            print(d[i],end=' ')
        print()
    
    def bottomView(self):
        s=[[self.root,0]]
        d=dict()
        while len(s)!=0:
            t=s.pop(0)
            d[t[1]]=t[0].data
            if t[0].left:
                s.append([t[0].left,t[1]-1])
            if t[0].right:
                s.append([t[0].right,t[1]+1])
        for i in sorted(d.keys()):
            print(d[i],end=' ')
        print()

    def height(self,node):
        if node is None:
            return 0
        l=self.height(node.left)
        r=self.height(node.right)
        return 1+max(l,r)

    def noofnodes(self,node):
        if node is None:
            return 0
        l=self.noofnodes(node.left)
        r=self.noofnodes(node.right)
        return 1+l+r
        
    def longestdiameter(self,node):
        global md
        if node is None:
            return 0
        l=self.longestdiameter(node.left)
        r=self.longestdiameter(node.right)
        h=1+max(l,r)
        d=1+l+r
        if d>md:
            md=d
        return h
    
    def maxdiametersum(self,node):
        global ms
        if node is None:
            return 0
        l=self.maxdiametersum(node.left)
        r=self.maxdiametersum(node.right)
        ms=max(ms,node.data+l+r)
        return md

bt=BinaryTree()
print('1. Insert Element\n2. Display Elements\n3. Preorder\n4. Inorder\n5. Postorder\n6. Search Element\n7. Delete Element\n8. Leaf Nodes\n9. Level Order\n10. Vertical Order\n11. Top View\n12. Bottom View\n13. Height\n14. No of Nodes\n15. Longest Diameter\n16. Exit\n')
while True:
    ch=int(input('Enter your Choice: '))
    match ch:
        case 1:
            bt.insertNode(int(input('Enter the Element: ')))
        case 2:
            bt.display()
        case 3:
            bt.preOrder()
        case 4:
            bt.inOrder()
        case 5:
            bt.postOrder()
        case 6:
            bt.search(int(input('Enter the Element: ')))
        case 7:
            bt.deleteNode(int(input('Enter the Element: ')))
        case 8:
            bt.leafNode()
        case 9:
            bt.levelOrder()
        case 10:
            bt.verticalOrder()
        case 11:
            bt.topView()
        case 12:
            bt.bottomView()
        case 13:
            print(f'Height: {bt.height(bt.root)}\n')
        case 14:
            print(f'No of Nodes: {bt.noofnodes(bt.root)}\n')
        case 15:
            md=0
            bt.longestdiameter(bt.root)
            print(f'Longest Diameter: {md}\n')
        case 16:
            print('Thank You!')
        case _:
            print('Invalid Choice,Choose Correct Option.\n')