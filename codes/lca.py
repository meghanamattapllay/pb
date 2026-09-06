class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def build(a):
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
def lca(root,a,b):
    if not root:
        return None
    if root.data==a or root.data==b:
        return root
    left=lca(root.left,a,b)
    right=lca(root.right,a,b)
    if left and right:
        return root
    return left if left else right

a=list(map(int,input().split()))
x,y=map(int,input().split())
root=build(a)
ans=lca(root,x,y)
print(ans.data)