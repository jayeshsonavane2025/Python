a = int(input("Enter the number:"))
b = 0
c = 1
if(a==0):
    print(b)
else:
 for i in range(0,a+1):
     temp = b+c
     print(temp)
     b = c
     c = temp
     

 