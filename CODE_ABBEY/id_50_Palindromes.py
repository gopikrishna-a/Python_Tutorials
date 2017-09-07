"""
NOTE:
Your goal in this programming exercise is to determine, whether the phrase represents a palindrome or not.
As you see, case of the letters is ignored. Spaces and punctuations are ignored too.
"""

n = int(raw_input("Enter No. of Cases : ").strip())
l = []
for i in range(0,n):
    st = raw_input("Enter Test String: ")
    st = st.lower()
    for i in st:
        if i in '.?!:;-—()[]...’“”/, ':
            st = st.replace(i,"")
    rev_st = st[::-1]
    if st == rev_st:
        l.append("Y")
    else:
        l.append("N")

for i in l:
    print i,
