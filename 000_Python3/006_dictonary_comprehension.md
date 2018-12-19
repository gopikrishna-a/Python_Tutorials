# Dictonary comprehensions
Dictonary comprehensions are used for creating new Dictonary from another iterables.


### Dictonary comprehensions for loop:

* **multiplying dict values with 2 using For loop**

		>>> my_dict = {'A': 1, 'B': 2, 'C': 3, 'D': 4}
		>>> for key, vale in my_dict.items():
		...     my_dict[key] = vale * 2
		...
		>>> my_dict
		{'A': 2, 'C': 6, 'B': 4, 'D': 8}
		>>>


* **Using Dictonary comprehensions the above program can be written as follows**

		>>> my_dict = {'A': 1, 'B': 2, 'C': 3, 'D': 4}
		>>> my_dict = {key : value * 2 for key, value in my_dict.items()}
		>>> my_dict
		{'A': 2, 'C': 6, 'B': 4, 'D': 8}
		>>>


### Dictonary comprehensions for loop and if condiation:

* **Finding even numbers from given list and storing into dictonary**

		>>> numbers = [1, 2, 3, 4, 5, 6, 7, 8]
		>>> result = {}
		>>> for num in numbers:
		...     if num % 2 == 0:
		...         result[num] = "Even"
		...     else:
		...         result[num] = "Odd"
		...
		>>> result
		{1: 'Odd', 2: 'Even', 3: 'Odd', 4: 'Even', 5: 'Odd', 6: 'Even', 7: 'Odd', 8: 'Even'}
		>>>


* **Using Dictonary comprehensions the above program can be written as follows**

		>>> numbers = [1, 2, 3, 4, 5, 6, 7, 8]
		>>> result = {num: ("Even" if num % 2 == 0 else "Odd") for num in numbers}
		>>> result
		{1: 'Odd', 2: 'Even', 3: 'Odd', 4: 'Even', 5: 'Odd', 6: 'Even', 7: 'Odd', 8: 'Even'}
		>>>