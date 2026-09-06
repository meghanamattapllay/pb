class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def build(pre,inorder):
    if not pre:
        return None
    root=Node(pre[0])
    i=inorder.index(pre[0])
    root.left=build(pre[1:i+1],inorder[:i])
    root.right=build(pre[i+1:],inorder[i+1:])
    return root
def preorder(root):
    if root:
        print(root.data,end=" ")
        preorder(root.left)
        preorder(root.right)
pre=list(map(int,input().split()))
ino=list(map(int,input().split()))
root=build(pre,ino)
preorder(root)
