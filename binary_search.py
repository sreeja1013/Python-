a=[]
n=int(input("enter the number of elements"))
for i in range(0,n):
    e=int(input("enter a number"))
    a.append(e)
low=0
high=n
item=int(input("enter the item to be searched"))
flag=1
while(low<high):
    mid=(low+high)//2
    if(a[mid]==item):
        print("The item is found on",mid+1)
        break
    elif(item>a[mid]):
        low=mid+1
    elif(item<a[mid]):
        high=mid-1
if(low>high):
    print("not found")
