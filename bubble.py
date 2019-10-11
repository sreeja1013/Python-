a=[]
n=int(input("enter the number of elements"))
for i in range(0,n):
    e=int(input("enter a number"))
    a.append(e)
for i in range(0,n):
    for j in range(0,n-i-1):
        if(a[j+1]<a[j]):
            (a[j+1],a[j])=(a[j],a[j+1])
print("the sorte array is",a)
