import re

def find_phone_number(input): 
    """Function to find first valid phone number in the provided input"""
    phone_regx = re.compile(r'((\(\d{3}\)|\d{3})\s\d{3}-\d{4})')
    match = phone_regx.search(input)
    if match:
    	return match.group()
    return None
#print(find_phone_number('333 444-5555'))
#print(find_phone_number('(333) 444-6666'))

"""
#OutPut
$ python 002_regex_phone_numbers.py
333 444-5555
(333) 444-5555
"""

def find_all_phone_numbers(input):
    """Function to find all valid phone number in the provided input"""
    phone_regx = re.compile(r'(\(\d{3}\)|\d{3})\s\d{3}-\d{4}')
    return phone_regx.findall(input)

print(find_all_phone_numbers('call me on (333) 444-5555 or 333 444-6666'))