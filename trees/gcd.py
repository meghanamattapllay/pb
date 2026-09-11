import math
tree=[]
def build(index,st,ed,arr):
    if st==ed:
        tree[index]=arr[st]
        return
    mid=(st+ed)//2
    build(2*index+1,st,mid,arr)
    build(2*index+2,mid+1,ed,arr)
    tree[index]=math.gcd(tree[2*index+1],tree[2*index+2])
def update(index,st,ed,arr,x,val):
    if st==ed:
        arr[x]=val
        tree[index]=val
        return
    mid=(st+ed)//2
    if x<=mid:
        update(2*index+1,st,mid,arr,x,val)
    else:
        update(2*index+2,mid+1,ed,arr,x,val)
    tree[index]=math.gcd(tree[2*index+1],tree[2*index+2])
def query(index,st,ed,l,r):
    if l>ed or r<st:
        return 0
    if l<=st and ed<=r:
        return tree[index]
    mid=(st+ed)//2
    return math.gcd(query(2*index+1,st,mid,l,r),query(2*index+2,mid+1,ed,l,r))
n=int(input())
arr=list(map(int,input().split()))
tree=[0]*(4*n)
build(0,0,n-1,arr)
q=int(input())
for i in range(q):
    data=list(map(int,input().split()))
    if data[0]==1:
        update(0,0,n-1,arr,data[1],data[2])
    else:
        print(query(0,0,n-1,data[1],data[2]))