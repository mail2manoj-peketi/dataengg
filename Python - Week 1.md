## Day 1 
###### Data types : 
	- Int -ve to +ve (no limit grows as per systems memory)
	- Float / decimal
	- Complex { Real , Imaginary value} (1+2j)
	- Strings
###### Variables : 
	
	-Integer -> a = 1
	-Float -> a=0.1
	-String -> a="1" 
		**revise f'string concept more later**
	-Boolean -> a , b = True , False
###### Functions : 
print()
input()
	`-Input always takes string as datatype when entering` 
	`-Use type conversion to change string to desired value`
	`-i.e., age = int(input(enter age : ))`
	`-Above statement converts age into an integer while entering it` 
type()
	-returns the type of the variable
```
		type(stringName)
		<class 'str'>
```
stringName.upper()
	- `makes all the characters in string to upper case
stringName.lower()
	- `makes all the characters in string to lower case
len(stringName)
	- `returns length of the string as a string

## DAY 2
##### List : a = [1, 2, 3, 4, 5, ...]
	- Slower, uses more memory, Mutable objects
	- Lists contains collection of similar or different data type values, but mostly similar and are immutable
	- slcing is available in lists
```
>>> a = [1, 2, 3, 4]
>>> a[1:]
[2, 3, 4]
```
	- copying can be done through slicing and this makes the referenced object linked and any change made to either of the them will reflect in both 
```
>>> b = a
>>> b
[1, 2, 3, 4] 
```
	- This behaviour can be avoided by using shallow copying technique utilizing slicing
```
>>> c = a[:]
>>> c
[1, 2, 3, 4]
>>> c[2:] = 0,0
>>> c
[1, 2, 0, 0]
>>> b
[1, 2, 3, 4]
```
	-It is possible to create nested lists
```
>>> x=['a','b','c']
>>> y=[0,1,2]
>>> z=x,y
>>> z[0]
['a', 'b', 'c']
>>> z[0][1]
'b'
>>> z[1]
[0, 1, 2]
>>> z[1][2]
2
```
	-We can add new elements to list using append() function
```
>>> a.append(5)
>>> a
[1, 2, 3, 4, 5]
```
	-We can add multiple elements at once using extend() function
```
>>> a.extend([6,7,8])
>>> a
[1, 2, 3, 4, 5, 6, 7, 8]
```
##### Tuples : d = (1, 'Hello', 2.45, [1, 2, 3, 4, 5]) 
	- Faster, highly optimized, heteregenous immutable objects.
	- they are seperated / differenciated by comma
	- they can be accessed by indexing d[3][2] = 3
	- tuples may contain mutable objects like lists
	- Can be used as keys in dictionaries
	- They can be unpacked like below 
```
temp, temp1, temp2, temp4 = d
>>> temp
1
>>> temp1
'Hello'
>>> temp2
2.45
>>> temp4
[1, 2, 0, 4, 5]
>>>
```

	-Real World scenario :
		-Returning Multiple Values from a Function : When a Python function returns more than one item, it secretly bundles them up and returns them as a single tuple.
##### Range : r = range(0, 10 , 2)
	-`range` object will always take the same amount of memory, no matter the size of the range as it only store start, stop, step values
##### Sets : a ={'apple', 'banana'}
	-Unordered collection of unique elements
	-Does not support indexing, slicing
	-Useful for membership, intersection, uninons
	-Has two types 
		1. set()  - mutable {add(),remove()}, not hashable, cannot be used as keys
		2. frozenset() - immutable , hashable, can be used as keys in dictionaries
			`boxFrozenSetA = frozenset([1,2,3,4]) #Can only be assigned like this`
	-Real World Scenarios : 
		- converting a list to a set for a quick lookup for unique values. 
			`boxSet = set(ListA)
			'apple' in boxSet`
		- Finding common items 
			`print(boxSetA & boxSetB)`
##### Dictionaries : dictA = {'alpha' : 1, 'beta' : 2, 'gamma' : 3} or dictB = dict([(1 , 'apple')]) 
	-Always stored in key:value pairs
	-Keys are unique in one set - tuples, frozensets , strings , numbers can be used / Lists cannot be used as keys. 
	-If tuples has mutable elements , then they cannot be used as keys . 
	-Below functions can be used
	`dictA.get(keys) >>> dictA.get('alpha')`
	`key in dictA >>> 'alpha' in dictA`
	-Values can be added by below
		-dictA.append({'key':'value','key1':'value'})
		%%-dictA.update('key':'value','key1':'value') #need to review more not working%%
	-Items can be deleted by below
		-dictA.pop('key')
	-Values can be viewed by below
		-dictA['key']
		-dictA.get('key')
		-dictA.items()
##### For Loop:
```
	for i in string :
		print(i)
```
	-in above example, i will iterate on number of strings present in "string" variable.
	-As such above will only work if the iterable variable is a string
	-To iterate over an integer `range` function should be used
```
fruits = 10
for i in range(fruits) :
	print(i)
``` 

## DAY 3 
User defined Functions : 
	-Reusable part of code that can be defined by user . 
	-Can be create to have or not have arguments to pass onto the function
	-`return` can be used to return the value from function 
	-`*` can be used as arguments to pass tuples onto the function.
	-`**` can be used as arguments to pass dictionaries onto the function.
```
#Basic Function
def dog():
	print("I am a dog, Wan! Wan!")
	
#Parametrized function
def dog(name):
	print(f"I am a dog and my name is {name} Wan!")
	
#Returning Function
def bark():
	return("bow!bow!")
	
#Default Function
def dog(name, treats=2):
	print(f"I am {name} and i get {treats} treats wan!")
	
#Arbitary arguments
def dog(name, *puppynames):
	print(f"{name} has {len(puppynames)} many puppies and their names are : ")
	for wan in puppynames :
		print(f"{wan}")
		
Calling above function looks like
pups=('mary','susan','lucy')
dog('Anna',*pups)        #here adding `asterisk` passes tuple as a single object
						 #To pass multiple tuple pass argument without `*`
```