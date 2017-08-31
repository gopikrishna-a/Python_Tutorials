import string
def write_alphabets(name):
    file = open(name,'w')
    count = 1
    for i in string.ascii_lowercase:
        if count % 2 == 0:
            file.write(i + "\n")
        else:
            file.write(i)
        count +=1

name = "123.txt"

print write_alphabets(name)
