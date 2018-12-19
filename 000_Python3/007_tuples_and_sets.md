# Sets and Tuples

## Tuples:

* A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.

		mu_tuple = (1, 2, 'Hii', True)

## Tuple Methods

### Tuple index()
* The method **index()** finds the index of a passed value from the Tuple.
* **Syntax**

		Tuple.index(item) # Takes three  arguments.

* **index()** method takes three arguments two optional.
* **index()** method returns index of the passed value from the Tuple.
* **Example Usage:**
		
		>>> a_tuple = (1, 2, 3, 4)
		>>> res = a_tuple.index(3) #finding 3 index from a_Tuple
		>>> res
		2
		>>>

### Tuple count()
* The method **count()** appends a passed obj into the existing Tuple.
* **Syntax**

		Tuple.count(obj) # Takes only one argument

* **count()** method takes only one argument
* **count()** method does not return any value but updates the existing Tuple.
* **Example Usage:**
		
		>>> a_tuple = (1, 2, 3, 4, 3, 3, 3)
		>>> a_tuple.count(3) #Finding no. of occurances of 3 in a_tuple
		4
		>>>

## Sets:

* A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.
* Sets does not allow to store duplicate items
* Sets does not support indexing

		my_set = {"apple", "banana", "cherry"}


## Set Methods

### Set add()

* The method **add()** adds the new item to the existing set.
* **Syntax**

		Tuple.add(item)

* **add()** method takes one argument
* **add()** method returns None but updates the set with given item

* **Example Usage:**
		
		>>> my_set = {"apple", "banana", "cherry"}
		>>> my_set.add("grapes")
		>>> my_set
		set(['cherry', 'banana', 'grapes', 'apple'])
		>>>


### Set remove()

* The method **remove()** removes the item from the set.
* **Syntax**

		Tuple.remove(item)

* **remove()** method takes one argument
* **remove()** method returns None but removes the given item from the set.
* **remove()** method will throws KeyError if the given item is not presented.

* **Example Usage:**
		
		>>> my_set = {"apple", "banana", "cherry"}
		>>> my_set.remove('apple')
		>>> my_set
		set(['cherry', 'banana'])
		>>>
		>>> my_set.remove('jelly') #Returns KeyError if item not presented.
		Traceback (most recent call last):
		  File "<stdin>", line 1, in <module>
		KeyError: 'jelly'
		>>>


### Set discard()

* The method **discard()** removes the item from the set if item is presented else returns None.
* **Syntax**

		Tuple.discard(item)

* **discard()** method takes one argument
* **discard()** method returns None but removes the given item from the set.
* **discard()** method will not throw any Error even if the given item is not presented.

* **Example Usage:**
		
		>>> my_set = {"apple", "banana", "cherry"}
		>>> my_set.discard('apple')
		>>> my_set
		set(['cherry', 'banana'])
		>>> my_set.discard('jelly') #Even the jelly is not presented no error will return
		>>>


## Set Math

### Set Union (|)
	
	* Combines two sets into on by elemenating duplicates

		>>> class_one = {'tom', 'tony', 'chris'}
		>>> class_two = {'rocket', 'groot', 'drax'}
		>>> school = class_one | class_two
		>>> school
		set(['tony', 'groot', 'rocket', 'tom', 'chris', 'drax'])
		>>>


## Set Intersection (&)

	* Creates new set with the values that are in both sets

		>>> class_one = {'tom', 'tony', 'chris', 'groot', 'rocket'}
		>>> class_two = {'rocket', 'groot', 'drax', 'thor'}
		>>> class_one & class_two
		set(['groot', 'rocket'])
		>>>

