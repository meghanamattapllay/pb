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
def leftView(root):
    if not root:
        return
    q=[root]
    while q:
        n=len(q)
        for i in range(n):
            x=q.pop(0)
            if i==0:
                print(x.data,end=" ")
            if x.left:
                q.append(x.left)
            if x.right:
                q.append(x.right)
a=list(map(int,input().split()))
root=build(a)
leftView(root)