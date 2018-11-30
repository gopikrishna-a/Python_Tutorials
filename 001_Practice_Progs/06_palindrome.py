def palindrome(a):
    b = a[::-1]
    if a == b:
        print "Ur Input is palindrome"
    else:
        print "Ur Input is not a palindrome"

a = raw_input("Enter Ur In put:")
palindrome(a)
