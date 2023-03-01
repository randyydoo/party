"""
1. Write a Python function to find the maximum of three numbers. Go to the editor
Click me to see the sample solution
"""
def max(x, y, z):
    if x > y and x > z:
        return x
    elif y > x and y > z:
        return y
    return z


"""
2. Write a Python function to sum all the numbers in a list. Go to the editor
Sample List : (8, 2, 3, 0, 7)
Expected Output : 20
Click me to see the sample solution
"""
def list_sum(list):
    i, sum = 0, 0
    length = len(list) - 1
    while i <= length:
        sum = sum + list[i]
        i += 1
    return sum


"""
3. Write a Python function to multiply all the numbers in a list. Go to the editor
Sample List : (8, 2, 3, -1, 7)
Expected Output : -336
Click me to see the sample solution
"""
def list_prod(list): 
    i, prod = 0, 0
    length = len(list) - 1
    while i <= length:
        prod = prod * list[i]
        i += 1
    return prod

"""
4. Write a Python program to reverse a string. Go to the editor
Sample String : "1234abcd"
Expected Output : "dcba4321"
Click me to see the sample solution
"""
def reverse_string(string):
    # return string[::-1]
    empty = ""
    length = len(string) - 1
    while length >= 0:
        empty = empty + string[length]
        length -= 1
    return empty

"""
5. Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument. Go to the editor
Click me to see the sample solution
"""
def factorial(num):
    product = 1
    while num >= 1:
        product = product * num
        num -= 1
    return product

"""
6. Write a Python function to check whether a number falls within a given range. Go to the editor
Click me to see the sample solution
"""
def range(num, lower, upper):
    return lower <= num >= upper
"""
7. Write a Python function that accepts a string and counts the number of upper and lower case letters. Go to the editor
Sample String : 'The quick Brow Fox'
Expected Output :
No. of Upper case characters : 3
No. of Lower case Characters : 12
Click me to see the sample solution
"""
def case_counter(string):
    i, lower, upper = 0, 0, 0
    length = len(string) - 1
    while i <= length:
        if string[i].islower():
            lower += 1
        if string[i].isupper():
            upper += 1
        i += 1
    return upper, lower

"""
8. Write a Python function that takes a list and returns a new list with distinct elements from the first list. Go to the editor
Sample List : [1,2,3,3,3,3,4,5]
Unique List : [1, 2, 3, 4, 5]
Click me to see the sample solution
"""
def unique(list, newList):
    if not list:
        return newList
    #fix first condition
    elif list[-1] not in newList:
        value = list[-1]
        newList.append(value)
    return unique(list.pop(), newList)
## x = [1,2,3,3,3,4,4,5,5]
## empty = []
## print(unique(x, empty))

"""
9. Write a Python function that takes a number as a parameter 
and checks whether the number is prime or not. Go to the editor
Note : A prime number (or a prime) is a natural number greater 
than 1 and that has no positive divisors other than 1 and itself.
Click me to see the sample solution
"""


"""
10. Write a Python program to print the even numbers from a given list. Go to the editor
Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
Expected Result : [2, 4, 6, 8]
Click me to see the sample solution
"""


"""
11. Write a Python function to check whether a number is "Perfect" or not. Go to the editor
According to Wikipedia : In number theory, a perfect number is a positive integer that is equal 
to the sum of its proper positive divisors, that is, the sum of its positive divisors excluding 
the number itself (also known as its aliquot sum). Equivalently, a perfect number is a number 
that is half the sum of all of its positive divisors (including itself).
Example : The first perfect number is 6, because 1, 2, and 3 are its proper positive divisors, 
and 1 + 2 + 3 = 6. Equivalently, the number 6 is equal to half the sum of all its positive divisors: 
( 1 + 2 + 3 + 6 ) / 2 = 6. The next perfect number is 28 = 1 + 2 + 4 + 7 + 14. This is followed by 
the perfect numbers 496 and 8128.
Click me to see the sample solution
"""



"""
12. Write a Python function that checks whether a passed string is a palindrome or not. Go to the editor
Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.
Click me to see the sample solution
"""



"""
13. Write a Python function that prints out the first n rows of Pascal's triangle. Go to the editor
Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal.
Sample Pascal's triangle :
Pascal's triangle
Each number is the two numbers above it added together Go to the editor
Click me to see the sample solution
"""



"""
14. Write a Python function to check whether a string is a pangram or not. Go to the editor
Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
For example : "The quick brown fox jumps over the lazy dog"
Click me to see the sample solution
"""



"""
15. Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically. Go to the editor
Sample Items : green-red-yellow-black-white
Expected Result : black-green-red-white-yellow
Click me to see the sample solution
"""



"""
16. Write a Python function to create and print a list where the values are the squares of numbers between 1 and 30 (both included). Go to the editor
Click me to see the sample solution
"""



"""
17. Write a Python program to create a chain of function decorators (bold, italic, underline etc.). Go to the editor
Click me to see the sample solution
"""



"""
18. Write a Python program to execute a string containing Python code. Go to the editor
Click me to see the sample solution
"""



"""
19. Write a Python program to access a function inside a function. Go to the editor
Click me to see the sample solution
"""



"""
20. Write a Python program to detect the number of local variables declared in a function. Go to the editor
Sample Output:
3
Click me to see the sample solution
"""



"""
21. Write a Python program that invokes a function after a specified period of time.
"""

def can_win(number):
    """Returns True if the current player is guaranteed a win
    starting from the given state. It is impossible to win a game
    from an invalid game state.
    >>> can_win (-1) # invalid game state
    False
    >>> can_win (3) # take all three !
    True
    >>> can_win (4)
    False
    """
    "*** YOUR CODE HERE ***"
    return True