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
def height(root):
    if not root:
        return 0
    l=height(root.left)
    r=height(root.right)
    if abs(l-r)>1:
        return -1
    return max(l,r)+1
a=list(map(int,input().split()))
root=None
for x in a:
    root=insert(root,x)
if height(root)==-1:
    print("Not Balanced")
else:
    print("Balanced")