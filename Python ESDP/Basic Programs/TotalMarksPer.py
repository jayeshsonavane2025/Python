list1=[] 
n=int(input("Enter number of subjects"))
for i in range(0,n):
    item=int(input())
    # if(item>100):
    #      print("Enter valid number")
    #      exit()
    list1.append(item)
sum=0
for i in range(0,n):
     sum+=i
percent=sum/n; 
 
if percent>=90:
     grade="O"
elif percent>=80:
     grade="A"
elif percent>=70:
     grade="B"
elif percent>60:
     grade="C+"
elif percent>50:
     grade="C"
else:
     grade="Fail"
print("Grade: ",grade)
print("Percent:",percent)    
     
      
