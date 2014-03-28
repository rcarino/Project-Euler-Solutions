#If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
nums = {'1': 'one', '2': 'two', '3': 'three', '4':'four', '5': 'five', '6':'six', '7' :'seven', '8': 'eight',
        '9': 'nine'}

special_prefixes = {'2': 'twen', '3': 'thir', '4': 'for', '5': 'fif'}
# Plain looking fourteen is counted as a uniqueten because 4 is a special prefix (forty) for tens, but not teens
unique_tens = {'10': 'ten', '11': 'eleven', '12': 'twelve', '14': 'fourteen'}


def to_words(n):
    n = str(n)
    rtn_str = ''
    # Process last 2 digits together
    last_two = n[-2:] if len(n[-2:]) == 2 else '0' + n
    tens = last_two[0]
    ones = last_two[1]
    # handle teens
    if last_two in unique_tens:
        rtn_str += unique_tens[last_two]
    elif tens == '1':
        if ones in special_prefixes:  # [2-5] have altered prefixes
            rtn_str += special_prefixes[ones] + 'teen'
        else:  # [6-9] have prefixes that match the original word
            postfix = 'teen' if ones != '8' else 'een'  # Eight already ends with a 't'
            rtn_str += nums[ones] + postfix
    # handle all other tens
    else:
        if tens != '0':
            if tens in special_prefixes:
                rtn_str += special_prefixes[tens] + 'ty'
            else:
                postfix = 'ty' if tens != '8' else 'y'  # Eight already ends with a 't'
                rtn_str += nums[tens] + postfix
        if ones != '0':
            rtn_str += nums[ones]
    # handle hundreds
    if len(n) >= 3 and n[-3] != '0':
        rtn_str = 'and' + rtn_str if len(rtn_str) > 0 else rtn_str
        rtn_str = nums[n[-3]] + 'hundred' + rtn_str
    # handle thousands
    if len(n) >= 4:
        rtn_str = nums[n[-4]] + 'thousand' + rtn_str
    return rtn_str

let_count = 0
for i in range (1, 1001):
    let_count += len(to_words(i))
print let_count