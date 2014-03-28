__author__ = 'rcarino'

def is_5and2_palindromic(n):
    binary = bin(n)[2:]
    return is_palindrome(str(n)) and is_palindrome(binary)

def is_palindrome(s):
    end = len(s)
    for i in range(end/2 + 1):
        if s[i] != s[end - 1 - i]:
            return False
    return True

def palindromes_base_5and2(n):
    rtn = []
    for i in range(0, n):
        if is_5and2_palindromic(i):
            rtn.append(i)
    return rtn

print sum(palindromes_base_5and2(1000000))