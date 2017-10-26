# 1. List down the python variable types with example

"""

Python Datatypes:
=================

1. int()
All numarical values without fractional part
EX: a = 10


2. float()
All numarical values with fractional part
EX: a = 10.20


2. float()
All numarical values with fractional part
EX: a = 10.20




Built-in Collection Data Types:
===============================



1. Lists:
=========
A list contains items separated by commas and enclosed within square brackets ([]).

NOTE: lists are mutable
EX: l = [1,'a',True]



2. Strings:
===========
A string is a sequence of characters in order

EX: s = 'Hello'



3. Tuples:
==========

A tuple consists of a number of values separated by commas.
NOTE: lists are mutable
EX: tup = (1,'a',True) 	(Note: tuples are immutable ie. not changable and supports indexing)


4. Sets:
========

EX: set1 = {1,2,3,4,}


5. Dictionaries:
================

a data type consist of key-value pairs.

EX: dic = {'a':1,'b':True}



"""

###############################################################################################################

# 2. dictonary operations

dict = {'a':1,'b':True,'c':5.8} # creating dict


#task-1 print values of first key

print(dict['a'])


#task-2 update values of second key

dict['b'] = 'HII'


#task-3 delete values of third key


del dict['c']


###############################################################################################################


# 3. file operations


def write_in_file(file_name):

	file = open('123.txt','r')      #opening file
	new_file = open('new.txt','w')  #reading content of file

	for line in file:
	    print(line)
	    line = line.strip('\n')
	    new_file.write(line+' ADDING_PATTERN\n') #appending pattern

	file.close()
	new_file.close()


print(write_in_file('123.txt'))



###############################################################################################################

# 4. validating testing123asm@asmltd.com


import re

text = 'this is my email id testing123asm@asmltd.com'
obj = re.compile(r'[a-zA-Z0-9_.]+@+[a-zA-Z0-9_.]+')

print(re.findall(obj,text))



###############################################################################################################

#5. adding 5 numbers using a class

class AddNumbers(object):
    

    def __init__(self):
        print("Adding Numbers!!")
        
    def adding_it(self,nums):
        self.nums = nums
        return sum(self.nums)
    

result = AddNumbers()
print(result.adding_it([1,2,3,4,5]))



###############################################################################################################



# 6. function to run linux command

#Method	-----------> 1


import subprocess

def run_command(cmd):
    out = subprocess.check_output(cmd)
    return out
    
print(run_command('ls'))



#Method	-----------> 2

import commands

def run_command(cmd):
    out = commands.getoutput(cmd)
    return out
    
print(run_command('ls'))







###############################################################################################################

# 7. "obj,name,value,command,code,class_method,is,was" split the pattern with delimiter ',' and return pattern and count


def split_pattern(patern):
    patern = patern.split(',') #splitting with delimiter ','
    return (' '.join(map(str,patern)) +" length of string is "+ str(len(patern)))
    
    
    
print(split_pattern("obj,name,value,command,code,class_method,is,was"))


###############################################################################################################

# 8. function for exception handling


def exception_handling():
    
    a = 10
    b = 0
    
    try:
        c = a / b
        print(c)
        
    except ZeroDivisionError:
        print("can't divide number with zero")
    

exception_handling()




###############################################################################################################


# 9. script to connect to MySQLdb


import MySQLdb


db = MySQLdb.connect('localhost','root','asm123','TESTDB')

cursor = db.cursor()

sql = 'SELECT * FROM TESTDB'

cursor.execute(sql)
data = cursor.fetchall()
print(data)

db.close()


#this answer is incomplete


###############################################################################################################

# 10.List down top 5 modules that you used in your project

#1. os

import os

os.system('pwd')


#2. sys


import sys

name = sys.argv[1] # command line arguments
print(name)



#3.re

#Extracting vowels from a string

import re

txt = 'abcdefghijklmopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

obj = re.compile(r'[aeiouAEIOU]')

print(re.findall(obj,txt))


#4. datetime

import datetime

t = datetime.datetime.now()    #present time and date
print(t)



#5 . subprocess

import subprocess

a = subprocess.check_output('ls')
print(a)



###############################################################################################################


















    































