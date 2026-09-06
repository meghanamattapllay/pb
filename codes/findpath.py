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
def findpath(root,target,path):
    if not root:
        return False
    path.append(root.data)
    if root.data==target:
        return True
    if findpath(root.left,target,path) or findpath(root.right,target,path):
        return True
    path.pop()
    return False
a=list(map(int,input().split()))
target=int(input())
root=build(a)
ans=[]
findpath(root,target,ans)
print(*ans)