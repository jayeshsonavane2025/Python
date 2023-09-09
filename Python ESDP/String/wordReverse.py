s = input("Enter String :")
temp = ""
ans = ""
for i in s:
    if i != " ":
        temp += i
    else:
        ans = temp + " " + ans
        temp = ""
ans = temp + " " + ans
print(ans)
