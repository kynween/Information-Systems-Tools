x=int(input("введите x"))
c=x
y=int(input("введите y"))
z=y
if y>x:
    while y%x!=0:
        y=y+z
    else:
        print("otvet",y)
elif x>y:
    while x%y!=0:
        x=x+c
    else:
        print("otvet",x)
