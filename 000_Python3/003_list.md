# List Methods

### what is List in Python

* List is a collection data type, which can store all datatype values, List is ordered and changeable. and it allows duplicate members.

### Example List

		my_list = [1, 'Hi', True, [1, 2], {1 : A}]

### List Methods

### List append()
* The method **append()** appends a passed obj into the existing list.
* **Syntax**

		list.append(obj) # Takes only one argument
* **append()** method takes only one argument
* **append()** method does not return any value but updates the existing list.
* **Example Usage:**
		
		a_list = [1, 2, 3, 4]
		a_list.append(5) #Appending 5 into a_list
		print(a_list)

* **OutPut for above Example code**
		[1, 2, 3, 4, 5]


### List extend()
* The method **extend()** appends the contents of seq to list.
* **Syntax**

		list.extend(seq) # Takes only one argument

* **extend()** method takes list of elements or a string
* **extend()** method does not return any value but add the content to existing list.
* **Example Usage:**
		
		a_list = [1, 2, 3, 4]
		a_list.extend([5 ,6 , 7, 8]) #Extending a_list with 5, 6, 7, 8 sequence
		print(a_list)

* **OutPut for above Example code**
		[1, 2, 3, 4, 5, 6, 7, 8]


### List insert()
* The method **insert()** method inserts object into list at given index.
* **Syntax**

		list.insert(index, obj) # Takes two arguments

* **insert()** method takes two arguments i.e index and value
* **insert()** does not return any value but it inserts the given element at the given index.
* **Example Usage:**
		
		a_list = ['A', 'C', 'D']
		a_list.insert(1, 'B') #Inserting 'B' at the 1st Index in a_list
		print(a_list)

* **OutPut for above Example code**
		['A', 'B', 'C', 'D']


### List clear()
* The method **clear()** method deletes all items in  list.
* **Syntax**

		list.clear() # Takes no arguments

* **clear()** method does not take any arguments
* **clear()** method does not return any value but deletes all items in a list.
* **Example Usage:**
		
		a_list = [1, 2, 3, 4]
		a_list.extend() #Deleting items in a_list using clear() method
		print(a_list)

* **OutPut for above Example code**
		[]


### List pop()
* The method **pop()** method removes and returns last object or obj from the list.
* **Syntax**

		list.pop() #Takes one optional argument

		or

		list.pop(1) #Takes one optional argument

* **pop()** method takes one optional argument
* **pop()** method returns last object or obj from the list.
* **Example 1 Usage without argument:**
		
		a_list = [1, 2, 3, 4]
		a_list.pop() #Deleting last item in a_list using pop() method
		print(a_list)

* **OutPut for above Example code**
		[1, 2, 3]

* **Example 2 Usage without argument:**
		
		a_list = [1, 2, 3, 4]
		a_list.pop() #Deleting item 3 by providing index of 3.
		print(a_list)

* **OutPut for above Example code**
		[]

### List remove()
* The method **remove()** removes a passed value from the existing list.
* **Syntax**

		list.remove(item) # Takes only one argument

* **remove()** method takes only one argument
* **remove()** method does not return any value but removes given item from the existing list.
* **Example Usage:**
		
		a_list = [1, 2, 3, 4]
		a_list.remove(3) #removing 3 from a_list
		print(a_list)

* **OutPut for above Example code**
		[1, 2, 4]



### List index()
* The method **index()** finds the index of a passed value from the list.
* **Syntax**

		list.index(item) # Takes three  arguments.

* **index()** method takes three arguments two optional.
* **index()** method returns index of the passed value from the list.
* **Example Usage:**
		
		a_list = [1, 2, 3, 4]
		res = a_list.index(3) #finding 3 index from a_list
		print(res)

* **OutPut for above Example code**
		2


* **Example Usage With two arguments:**

		a_list = [1, 2, 3, 4, 4 , 1]
		a_list.index(1, 1)
		print(a_list)

* **OutPut for above Example code**
		5          #index of value 1 after the index 1


### List count()
* The method **count()** appends a passed obj into the existing list.
* **Syntax**

		list.count(obj) # Takes only one argument

* **count()** method takes only one argument
* **count()** method does not return any value but updates the existing list.
* **Example Usage:**
		
		a_list = [1, 2, 3, 4, 3, 3, 3]
		a_list.count(3) #Finding no. of occurances of 3 in a_list
		print(a_list)

* **OutPut for above Example code**
		4

### List reverse()
* The method **reverse()** reverses the items the list.
* **Syntax**

		list.reverse() # Takes no argument

* **reverse()** method takes no argument
* **reverse()** method does not return any value but updates the existing list by reversing the items.
* **Example Usage:**
		
		a_list = [1, 2, 3, 4, 5]
		a_list.reverse() #reversing the items in a_list
		print(a_list)

* **OutPut for above Example code**
		[5, 4, 3, 2, 1]


### List sort()
* The method **sort()** reverses the items the list.
* **Syntax**

		list.reverse() # Takes no argument

* **sort()** method takes no argument
* **sort()** method does not return any value but updates the existing list by sorting the items.
* **Example Usage:**
		
		a_list = [1, 5, 4, 2, 3]
		a_list.sort() #sorting the items in a_list
		print(a_list)

* **OutPut for above Example code**
		[1, 2, 3, 4, 5]



### String Method


### join()

* join() used to join the items in a list or a iterable

* **Example Usage:**
		
		a_list = ['A', 'B', 'C', 'D']
		','.join(a_list)#Joining the items in the list with a ,
		print(a_list)

* **OutPut for above Example code**
		'A,B,C,D'


