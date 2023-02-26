#crate a fucntion that removes all duplicate numbers
""""
>>dup(1223344)
1234
>>dup(55432)
5432
>>dup(6789)
6789
"""

23456.7
23456
def dup(n):
    list = ""
    for char in str(n):
        if list.find(char) != -1:
            list += char
    return int(list)


#create a palindrome checker for a string
"""
>>palindrome("hello")
False
>>palindrome("mom")
true
"""
def palindrome(n):
    return recurse(n, 0, len(n))
def recurse(s, first, last):
    if first >= last - 1:
        return True
    if s[first] == s[last - 1]:
        return palindrome(s, first + 1, last - 1)
    return False

print(palindrome("racecar", 0, 7))
print(palindrome("mom", 0, 3))
print(palindrome("hello", 0, 5))
