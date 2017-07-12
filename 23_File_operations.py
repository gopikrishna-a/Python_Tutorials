#Writing into file
fw = open('sample.txt','w')
fw.write('Hi Bucky\n')
fw.write('How are You\n')
fw.close()

#reading from a file
fr = open('sample.txt','r')
text = fr.read()
print (text)
fr.close()

