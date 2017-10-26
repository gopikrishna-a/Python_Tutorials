import re

text = 'this is my sss333 333email id 10.35.4.216 hagsdvjksbd 5246 jbd 8888881 10.20.21.5 jdfn'

pattern = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')


print(re.findall(pattern,text))
