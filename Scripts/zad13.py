a=int(input("enter a"))


b=int(input("enter b"))
b=b+1

c=int(input("enter c"))


d=int(input("enter d"))
d=d+1
k=9
h=" "
print(end="   ")

for i in range(a,b):
   
    for j in range (c,d):
        if (j*i)>k:
            h="  "
    print(i,end=h)
       
         
    


for i in range(c,d):
    print("\n",i,end="")
    for j in range (a,b):
        print("",i*j,end="")
