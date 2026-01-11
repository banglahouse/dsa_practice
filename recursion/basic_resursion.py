import array

# In recursion there is a base condition when hit, helps exit the function 
# If I want


def basicRecursion(n):
    if (n == 0):
        return
    basicRecursion(n - 1)
    print(n)

"""

Given an integer N, return the sum of first N natural numbers. Try to solve this using recursion.


Example 1

Input : N = 4

Output : 10

Explanation : first four natural numbers are 1, 2, 3, 4.

Sum is 1 + 2 + 3 + 4 => 10.

Example 2

Input : N = 2

Output : 3

Explanation : first two natural numbers are 1, 2.

Sum is 1 + 2 => 3.
"""


# This is the parameterized way where we are carrying the sum in the param 

def sumOfNnaturalNumbers(n,sum):
    if (n == 0):
        print(sum)
        return
    sum =  sum + n
    sumOfNnaturalNumbers(n-1,sum)


# there is another way called functional

def fSumOfNnaturalNums(n):
    if(n < 1 or n == 0): # khud ki tasali ke liye or likha hai ki meko or pta hai 
        return 0
    
    return n + fSumOfNnaturalNums(n - 1)

def factorialOfN(n):
    if(n < 1 or n == 0): # khud ki tasali ke liye or likha hai ki meko or pta hai 
        return 1
    
    return n * factorialOfN(n - 1)

# We need to reverse an array 
# using recursion

def reverse(arr: list, n: int):
    if(n <= len(arr)//2):
        return arr
    swap(n-1,len(arr)-n,arr)
    reverse(arr,n-1)

def isPalindrome(n: int, s: str):
    print(n)
    if(n >= len(s)//2):
        return True
    if(s[n] != s[len(s)-n-1]):
        return False
    return isPalindrome(n+1,s)

    


def swap(first: int,second: int, arr: list):
    arr[first], arr[second] = arr[second], arr[first]



def isPalindromeAgain(n: int, s: str):
    if(n >= len(s)//2):
        return True
    if(s[n] != s[len(s)-1-n]):
        return False
    return isPalindromeAgain(n+1,s)

# fibonanci series for N numbers 

def fibonacciR(n:int):
    if(n <= 1):
        return n
    sum = fibonacciR(n - 1) + fibonacciR(n -2)
    return sum


# multiple recursion calls
    
def fibonacci(n: int):
    first = 0
    second = 1
    for i in range(0,n,1):
        print(first)
        temp = second
        second = first + second
        first = temp
    


if __name__ == "__main__":
    # s = "madaf"
    # check = isPalindromeAgain(0,s)
    # print(check)
    # l = [1,2,43,4,5]
    # reverse(l,5)
    # print(l)
    n = fibonacciR(6)
    print(n)
