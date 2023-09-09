s = input("Enter String :")

start = 0
end = len(s) - 1
while start <= end:
    if s[start] != s[end]:
        print(s, " is not Palimndrome")
        break
    start += 1
    end -= 1
else:
    print(s, " is  palindrome")
