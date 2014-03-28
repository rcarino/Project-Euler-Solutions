import datetime
start = datetime.datetime.now()

def permute(digit_string):
    # permutation generator with modifications to return millionth perm
    global writes, millionth
    writes = 0
    def perm_helper(write, read):
        global writes, millionth
        if not read:
            writes += 1
            if writes == 1000000:
                millionth = int(write)
        else:
            for c in read:
                perm_helper(write + c, read.replace(c, ''))
    perm_helper('', digit_string)
    return millionth

#print permute('0123456789') # Brute force takes 9 seconds
import math
def nth_perm(n, digit_string):
    # Use sorted property of digit string to calculate 1mm'th perm using factorials
    perm = ""
    i = 1
    while digit_string: # 9! < 1mm
        target_perms = math.factorial(len(digit_string) - 1) # The number of permutations remaining after fixing item i
        # fixing on item i, is out of range for n, try fixing next item
        if target_perms * i < n:
            i += 1
        else:
            # Fixing item i - 1 falls in n's range
            write = digit_string[i - 1]
            perm += write
            digit_string = digit_string.replace(write, '')
            n -= target_perms * (i - 1)
            i = 1
    return perm

print nth_perm(1000000, '0123456789') # Combinatorial solution takes less than a ms

# solution 2783915460

end = datetime.datetime.now()

print 'time: ', end - start