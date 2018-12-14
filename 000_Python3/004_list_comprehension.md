List comprehensions are used for creating new list from another iterables.



### List comprehensions for loop:

* **Finding squares using For loop**

		numbers = [1, 2, 3, 4, 5, 6]
		result = []
		for num in numbers:
		   num = num * num
		   result.append(num)
		print(result)


* **OutPut for above Example code**
		[1, 4, 9, 16, 25, 36]

* **Using List comprehensions the above program can be written as follows**

		numbers = [1, 2, 3, 4, 5, 6]
		result = [num*num for num in numbers]
		print(result)

* **OutPut for above Example code**
		[1, 4, 9, 16, 25, 36]

### List comprehensions for loop and if condiation:

* **Finding even numbers from given list**

		numbers = [1, 2, 3, 4, 5, 6, 7, 8]
		result = []
		for num in numbers:
		   if num % 2 == 0:
		       result.append(num)
		print(result)


* **OutPut for above Example code**
		[2, 4, 6, 8]

* **Using List comprehensions the above program can be written as follows**

		numbers = [1, 2, 3, 4, 5, 6, 7, 8]
		result = [num for num in numbers if num % 2 == 0]
		print(result)
		
* **OutPut for above Example code**
		[2, 4, 6, 8]


### List comprehensions for loop and if and else condiation:

* **squre the number if it's even else divide by 2**

		numbers = [1, 2, 3, 4, 5, 6, 7, 8]
		result = []
		for num in numbers:
		   if num % 2 == 0:
		       result.append(num * 2)
		   else:
		       result.append(num / 2)
		print(result)


* **OutPut for above Example code**
		[0.5, 4, 1.5, 8, 2.5, 12, 3.5, 16]

* **Using List comprehensions the above program can be written as follows**

		numbers = [1, 2, 3, 4, 5, 6, 7, 8]
		result = [i for i in numbers if i % 2 == 0]
		print(result)
		
* **OutPut for above Example code**
		[0.5, 4, 1.5, 8, 2.5, 12, 3.5, 16]

