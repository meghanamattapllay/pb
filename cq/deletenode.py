class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def insert(root,data):
    if not root:
        return Node(data)
    if data<root.data:
        root.left=insert(root.left,data)
    else:
        root.right=insert(root.right,data)
    return root
def delete(root,key):
    if not root:
        return None
    if key<root.data:
        root.left=delete(root.left,key)
    elif key>root.data:
        root.right=delete(root.right,key)
    else:
        if not root.left:
            return root.right
        if not root.right:
            return root.left
        x=root.right
        while x.left:
            x=x.left
        root.data=x.data
        root.right=delete(root.right,x.data)
    return root
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data,end=" ")
        inorder(root.right)
a=list(map(int,input().split()))
key=int(input())
root=None
for x in a:
    root=insert(root,x)
root=delete(root,key)
inorder(root)