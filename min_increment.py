def minimum_increment(arr,k):
    total=0
    prev=arr[0]
    i=0
    n=len(arr)
    while i<n:
        j=i
        while j<n and arr[j]==arr[i]:
            j+=1
        cur=arr[i]
        if i>0 and cur<prev+k:
            inc=prev+k-cur
            total+=inc*(j-i)
            prev=cur+inc
        else:
            prev=cur
        i=j
    return total
arr=list(map(int,input("Enter array: ").split()))
k=int(input("Enter K: "))
print("Minimum total increment:",minimum_increment(arr,k))