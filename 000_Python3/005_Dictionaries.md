# Python Dictionaries


### Python **dictionary** is an unordered collection of items. While other compound data types have only value as an element, a dictionary has a key: value pair. Dictionaries are optimized to retrieve values when the key is known.

### **Example dictionary**

		my_dict = {'name': 'Gopikrishna', 'age': 24, 'single': True, 1 : 'Lucky Number'}

### **Example dictionary**

		>>> student = dict(name="Stark", age=28, male=True)
		>>> student
		{'age': 28, 'male': True, 'name': 'Stark'}
		>>>

### **Accessing dictonary value using key**

		>>> student = {'age': 28, 'male': True, 'name': 'Stark'}
		>>> #Reading dict value using key 'name'
		...
		>>> student['name']
		'Stark'
		>>> print(student.get('phone')) # Will return None if key not presented
		None


### Dictonary methods

### dict.get()

#####  **Accessing dictonary value using get() method**

* Takes one argument i.e key
* Return value of the corresponding key

		>>> student = {'age': 28, 'male': True, 'name': 'Stark'}
		>>> #Reading dict value using key 'name'
		...
		>>> student.get('age')
		28
		>>>

### dict.keys()

##### **Get all keys from a dictonary using keys() method**

* Takes no arguments
* Returns list containing keys of the dictonary

		>>> student = {'age': 28, 'male': True, 'name': 'Stark'}
		>>> student.keys()
		['age', 'male', 'name']
		>>>


### dict.values()

##### **Get all keys from a dictonary using values() method**

* Takes no arguments
* Returns list containing values of the dictonary

		>>> student = {'age': 28, 'male': True, 'name': 'Stark'}
		>>> student.values()
		[28, True, 'Stark']
		>>>	

### dict.items()

##### **Get all items from a dictonary using items() method**

* Takes no arguments
* Returns list of tuple containing keys, values pairs of the dictonary

		>>> student = {'age': 28, 'male': True, 'name': 'Stark'}
		>>> student.values()
		[('age', 28), ('male', True), ('name', 'Stark')]
		>>>	

### dict.clear()

* Takes no arguments
* Returns None

##### **clear() method Deletes all items from a dict**

		>>> student = {'age': 28, 'male': True, 'name': 'Stark'}
		>>> student.clear()
		>>> student
		{}
		>>>


### dict.copy()

* Takes no arguments
* Returns copy of the dict.

#### **copy() method can create copy of a dict**

		>>> student = {'age': 28, 'male': True, 'name': 'Stark'}
		>>> student_copy = student.copy() #Creating student dict copy and storing in student_copy
		>>> student
		{'age': 28, 'male': True, 'name': 'Stark'}
		>>> student_copy
		{'age': 28, 'male': True, 'name': 'Stark'}
		>>>
		>>>
		>>> student == student_copy #Both dicts student and student_copy are same according to values
		True
		>>> student is student_copy #But memory addresses are different
		False
		>>>

### fromkeys()

* Takes two arguments
* Returns resultent dictonary.

#### **fromkeys() method to give same value for all keys**

		>>> my_dict = {}.fromkeys(['name', 'age', 'phone', 'email'], 'unknown')
		>>> my_dict
		{'phone': 'unknown', 'age': 'unknown', 'name': 'unknown', 'email': 'unknown'}
		>>>


### dict.pop()

* Takes one argument i.e key
* Returns corresponding key, value pair which was removed.

#### **pop() method to delete corresponding key, value pair**

		>>> student = {'age': 28, 'male': True, 'name': 'Stark'}
		>>> student
		{'age': 28, 'male': True, 'name': 'Stark'}
		>>> student.pop('male') #Removes key, value pair if key is present and retuns True/False
		True
		>>> student
		{'age': 28, 'name': 'Stark'}
		>>>

### dict.popitem()

* Takes no arguments
* Returns any random key, value pair which was removed.


#### **popitem() method to delete a random key, value pair**

		>>> student = {'age': 28, 'male': True, 'name': 'Stark'}
		>>> student.popitem()
		('age', 28)
		>>> student
		{'male': True, 'name': 'Stark'}
		>>>


### **Iterating Dictionarieswith for loop**


		>>> student = {'age': 28, 'male': True, 'name': 'Stark'}
		>>> for key, value in student.items():
		...     print(key)
		...     print(value)
		...
		age
		28
		male
		True
		name
		Stark
		>>>


### **Check exestance of a key in dictonary uisng in keyword**

		>>> student = {'age': 28, 'male': True, 'name': 'Stark'}
		>>> 'age' in student #Will return True if key is presented
		True
		>>> 'phone' in student #Will return False if key is not presented
		False
		>>>

### **Check exestance of a value in dictonary**

		>>> student = {'age': 28, 'male': True, 'name': 'Stark'}
		>>> 'Stark' in student.values() #Will return True if value is presented
		True
		>>> 'Avengers' in student.values() #Will return False if value is not presented
		False