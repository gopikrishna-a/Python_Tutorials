
#MAC Address Pattern

file = open('macs.txt','rb').read()

a = re.compile(r'(\s[0-9a-fA-F]{1,2}:[0-9a-fA-F]{1,2}:[0-9a-fA-F]{1,2}:[0-9a-fA-F]{1,2}:[0-9a-fA-F]{1,2}:[0-9a-fA-F]{1,2})')
      
mac = re.findall(a,file)
for i in mac:
  print i
  
  
  
