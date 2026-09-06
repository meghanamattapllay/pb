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
def inorder(root,a):
    if root:
        inorder(root.left,a)
        a.append(root.data)
        inorder(root.right,a)
a=list(map(int,input().split()))
k=int(input())
root=None
for x in a:
    root=insert(root,x)
arr=[]
inorder(root,arr)
print("Kth Smallest:",arr[k-1])
print("Kth Largest:",arr[-k])