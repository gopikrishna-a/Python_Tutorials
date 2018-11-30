
#Method -1
#With out regx
#number format = '415-555-1234'


def isphonenumber(txt):
    if len(txt) != 12:
        return False
    for i in range(0,3):
        if not txt[i].isdecimal():
            return False
    if txt[3] != '-':
        return False
    for i in range(4,7):
        if not txt[i].isdecimal():
            return False
    if txt[7] != '-':
        return False
    for i in range(8,12):
        if not txt[i].isdecimal():
            return False
    return True



message = 'call me on this number 415-555-1234 or call to this 415-565-1234 phone number'
numberfound= False

for i in range(len(message)):
    chunk =  message[i:i+12]
    if isphonenumber(chunk):
        print( 'phone number found ' + chunk)
        numberfound = True
if not numberfound:
    print( 'could not found any phone numbers')

    
    
    
    
    
    
    
    
    
#Method -2
#With out regx  
    
import re
message = 'call me on this number 415-555-1234 or call to this 415-565-1234 phone number'

obj = re.compile(r'\d\d\d-\d\d\d-\d\d\d')
    
