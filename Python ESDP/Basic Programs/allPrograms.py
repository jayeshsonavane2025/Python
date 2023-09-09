import math

 
def sqRoot(n):
    for i in range(0,n):
        print(math.sqrt(i))


def perfectDivide(a,b):
    if a%b==0:
        print("Perfect Divide")
    else:
        print("Not perfect divide")



def factorial(n):
    if n<=1:
        return 1;
    return n*factorial(n-1)


def star1(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print("*",end=" ")
        print()
   
def star2(n):
    for i in range(n,0,-1):
        for j in range(i,0,-1):
            print("*",end=" ")
        print()
  
def star3(n):
    for i in range(0,n+1):
        for j in range(0,n-i):
            print(" ",end="")
        for k in range(0,i+1):
            print("*",end="")
        print()
    
def star4(n):
     for i in range(0,n+1):
        for j in range(0,n-i):
            print(" ",end="")
        for k in range(0,i+1):
            print("*",end="")
        for l in range(0,i):
            print("*",end="")
        print()


def starABC(n):
    asci=97
    for i in range(0,n):
        for j in range(0,i+1):
           char=chr(asci)
           print(char,end=" ")
           asci+=1
        print()
    
def sumOfFirstLastDigit(n):
     
     lastDigit=n%10
     print(lastDigit)
     while n>9:
           
          n//=10
     print(n)
     print( lastDigit+n)
def sumOfDigit(n):
    res=0
    sum=0
    while(n!=0):
        sum+=n%10
        n//=10
    print(sum)
    
def reverseNumber(n):
    res=0;
    ans=0
    while(n!=0):
        ans=ans*10+n%10
         
        n//=10
    print(ans)
#print(factorial(0))
#perfectDivide(20,3)
#sqRoot(10)

#star1(4)

#star2(5)

# star3(5)

# star4(5)

# starABC(5)

#sumOfFirstLastDigit(10019)

#sumOfDigit(15131)

reverseNumber(102)
