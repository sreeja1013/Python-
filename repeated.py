def repeated(l):
  c=[]
  n=len(l)
  for i in range(0,n):
    s=0
    for j in range(i+1,n):
      if(l[i]==l[j]):
        s=s+1
    if(s>0):
   	  c.append(s)
  print(c)
