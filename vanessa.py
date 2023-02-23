#create a fucntiom that take an positive integer "n" and print the sum of 1 - n using while loop
"""
>>whilee(6) = 1 + 2 + 3 + 4 + 5 + 6
21
>>whilee(3) = 1, 2, 3
6
>>whilee(-1)
False
"""
def while_(n):
    sum = 0
    while n > 0:
        sum += n
        n -= 1
    print(sum)
    return

# while_(6)
#create a function that checks how many times a number appears in an integer
"""
checker(12234, 2)
2
checker(3333111, 3)
4
checker(1234, 5)
0
"""
def checker(num , target):
    target = str(target)
    i = 0
    num = str(num)
    for _ in num:
        if _ == target:
            i += 1
        else:
            continue
    print(i)
    return
# checker(12234, 2)
#crate a fucntion that removes all duplicate numbers
""""
>>dup(1223344)
1234
>>dup(55432)
5432
>>dup(6789)
6789
"""
def dup(n):
    m = str(n)
    seen = set()
    ans = ""
    for _ in m:
        if _ in seen:
            continue
        else:
            ans += _
            seen.add(_)
    print(ans)
    return n
dup(12223334)
#create a palindrome checker for a string
"""
>>palindrome("hello")
False
>>palindrome("mom")
true
"""
def palindrome(s):
    mp = len(s)//2
    if s == s[::-1]:
        print("Valid")
    else:
        print("Invalid")
palindrome("hello")

palindrome("aaabbbaaa")
