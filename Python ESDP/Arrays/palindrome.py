def isPalindrome(string):
    start = 0
    end = len(string - 1)
    while start < end:
        if string[start] != string[end]:
            print("Not palindrome")
            break
    else:
        print("Palindrome")
