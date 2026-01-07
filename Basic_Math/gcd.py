# Brute force approach is to divide till min(a,b)


def gcd(a, b):
    gcd = 1
    for i in range(min(a,b),0, -1):
        if(a % i == 0 and b % i == 0):
            gcd = i
            break
    return gcd

# Euclidean algorithm 
"""
 It states that 
 g(a,b) = g(a -b, b) where a > b
 using this concept we can find gcd till a become 0 
 for example
 g(10,5) = g(10-5,5)
 g(5,5) --> g(0,5) --> gcd === 5


 but if number is like 52,10 then it is not better solution, better approach would be 
 a%b,b --> repeat till one number becomes 0
"""

def eGcd(a,b):
    gcd = 1
    m = max(a,b)
    n = min(a,b)
    while(m != 0):
        m = m % n
        if(n > m and m != 0):
            c = m
            m = n
            n = c
    return n


# Striver solution --> this looks better tbh

def sGcd(a,b):
    while(a > 0 and b > 0):
        if(a > b):
            a = a % b
        else:
            b = b % a
    
    if(a > b ):
        return a
    else:
        return b


""" time complextity is big O log phi min(a,b) phi is a constant which is equal to 1.6 and
 fibonacchi numbers increment/decrement based on this number, 
 we are not sure about how fast or slow this algo will work thats why we say log phi,
  slowest when fibonnaci numbers are presented"""





if __name__ == "__main__":
    c = sGcd(52, 10)
    print(c)




