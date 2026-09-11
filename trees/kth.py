tree=[]
def build(index,st,ed,arr):
    if st==ed:
        tree[index]=arr[st]
        return
    mid=(st+ed)//2
    build(2*index+1,st,mid,arr)
    build(2*index+2,mid+1,ed,arr)
    tree[index]=tree[2*index+1]+tree[2*index+2]
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
    tree[index]=tree[2*index+1]+tree[2*index+2]
def kth(index,st,ed,k):
    if st==ed:
        return st
    mid=(st+ed)//2
    left=tree[2*index+1]
    if k<=left:
        return kth(2*index+1,st,mid,k)
    return kth(2*index+2,mid+1,ed,k-left)
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
        k=data[1]
        if tree[0]<k:
            print(-1)
        else:
            print(kth(0,0,n-1,k))