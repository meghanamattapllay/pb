class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def build(a):
    if not a or a[0]==-1:
        return None
    root=Node(a[0])
    q=[root]
    i=1
    while q and i<len(a):
        x=q.pop(0)
        if a[i]!=-1:
            x.left=Node(a[i])
            q.append(x.left)
        i+=1
        if i<len(a) and a[i]!=-1:
            x.right=Node(a[i])
            q.append(x.right)
        i+=1
    return root
def isBST(root,low,high):
    if not root:
        return True
    if root.data<=low or root.data>=high:
        return False
    return isBST(root.left,low,root.data) and isBST(root.right,root.data,high)
a=list(map(int,input().split()))
root=build(a)
if isBST(root,float("-inf"),float("inf")):
    print("True")
else:
    print("False")