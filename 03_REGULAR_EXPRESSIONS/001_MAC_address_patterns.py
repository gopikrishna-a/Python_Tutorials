
#MAC Address Pattern

import re

txt = "this is my mac address f:4d:a5:f4:23:66 slefdkm A'S;L CVLLF"

pattern = re.compile(r'(\s[0-9a-fA-F]{1,2}:[0-9a-fA-F]{1,2}:[0-9a-fA-F]{1,2}:[0-9a-fA-F]{1,2}:[0-9a-fA-F]{1,2}:[0-9a-fA-F]{1,2})')
      
print(re.findall(pattern,txt))
  
