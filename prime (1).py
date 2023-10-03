n=int(input("enter n:"))
i,j=2,1
print(i," is a prime")
while(i<n):
    
     while(j<i):
          if(i%j==0):
               break
          j+=1
     else:
          print(i,"is a prime")
     i+=1
     j=2
else:
     print("exit from loop")
