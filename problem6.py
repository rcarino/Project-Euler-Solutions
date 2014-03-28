"""Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum."""

def square(n):
    return n*n

def sumOfSquares(n):
    """sum of squares of numbers up to n"""
    sum = 0
    for i in xrange(1, n+1):
        sum += square(i)
    return sum

def squareOfSum(n):
    """square of sum of numbers up to n"""
    sum = 0
    for i in xrange(1, n+1):
        sum += i
    return square(sum)

print squareOfSum(100) - sumOfSquares(100)
