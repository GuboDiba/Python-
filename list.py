Python 3.8.10 (default, Nov 14 2022, 12:59:47) 
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> x="Akirachix"
>>> x[0]
'A'
>>> x[1]
'k'
>>> x[2]
'i'
>>> x[3]
'r'
>>> x[4]
'a'
>>> x[5]
'c'
>>> x[6]
'h'
>>> x[7]
'i'
>>> x[8]
'x'
>>> x[9]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
>>> x[-0]
'A'
>>> x[-1]
'x'
>>> x[-2]
'i'
>>> x[-3]
'h'
>>> x[-4]
'c'
>>> x[-5]
'a'
>>> x[-6]
'r'
>>> x[-7]
'i'
>>> x[-8]
'k'
>>> x[-9]
'A'
>>> x[-10]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
>>> a="aki ra"
>>> a[3]
' '
>>> x[0:3]
'Aki'
>>> x[4:8]
'achi'
>>> x[3: ]
'rachix'
>>> x[1:4]
'kir'
>>> a[2:4]
'i '
>>> a[2:5]
'i r'
>>> x[-8:-6]
'ki'
>>> x[-5:-2]
'ach'
>>> x[-4: ]
'chix'
>>> x[-3:-7]
''
>>> x[1:-3]
'kirac'
>>> x[-6:7]
'rach'
>>> x[-5:8]
'achi'
>>> x[3:-3]
'rac'
>>> x[-3:3
... x[-3:3]
  File "<stdin>", line 2
    x[-3:3]
    ^
SyntaxError: invalid syntax
>>> x[-3:3]
''
>>> y=[1,2,3,4,5,6]
>>> z=["a","b","c","d"]
>>> s=[1,2,"a","b",3.33,true,false]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'true' is not defined
>>> s=[1,2,"a","b",3.33,"true","false"]
>>> type(y)
<class 'list'>
>>> type(z)
<class 'list'>
>>> type(s)
<class 'list'>
>>> a=[1,2,3,4]
>>> b=[5,6,7]
>>> c=a+b
>>> c
[1, 2, 3, 4, 5, 6, 7]
>>> b=a*3
>>> b
[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
>>> dir(a)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> fruits=["Mango","Banana","passion","melon"]
>>> fruits.append("pineapple")
>>> fruits
['Mango', 'Banana', 'passion', 'melon', 'pineapple']
>>> fruits.extend(["orange","graps"])
>>> fruits
['Mango', 'Banana', 'passion', 'melon', 'pineapple', 'orange', 'graps']
>>> fruits.insert(1,"avocado"]
  File "<stdin>", line 1
    fruits.insert(1,"avocado"]
                             ^
SyntaxError: closing parenthesis ']' does not match opening parenthesis '('
>>> fruits.insert(1,"avocado")
>>> fruits
['Mango', 'avocado', 'Banana', 'passion', 'melon', 'pineapple', 'orange', 'graps']
>>> fruits.sort()
>>> fruits
['Banana', 'Mango', 'avocado', 'graps', 'melon', 'orange', 'passion', 'pineapple']
>>> fruits.reverse()
>>> fruits
['pineapple', 'passion', 'orange', 'melon', 'graps', 'avocado', 'Mango', 'Banana']
>>> fruits.remove()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: remove() takes exactly one argument (0 given)
>>> fruits.remove("melon")
>>> fruits
['pineapple', 'passion', 'orange', 'graps', 'avocado', 'Mango', 'Banana']
>>> fruits.pop()
'Banana'
>>> fruits
['pineapple', 'passion', 'orange', 'graps', 'avocado', 'Mango']
>>> len(fruits)
6
>>> fruits[0]
'pineapple'
>>> fruits[2]
'orange'
>>> fruits[3]
'graps'
>>> fruits[6]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>> fruits[7]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>> fruits[3:5]
['graps', 'avocado']
>>> fruits[ :4]
['pineapple', 'passion', 'orange', 'graps']
>>> fruits[2: ]
['orange', 'graps', 'avocado', 'Mango']
>>> x=[1,2,3,4,5]
>>> for n in x:print(n)
... 
1
2
3
4
5
>>> for n in x:print(n*10)
... 
10
20
30
40
50
>>> for n in x:print(n*n)
... 
1
4
9
16
25
>>> for n in fruits:print(fruits.upper)
... 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'list' object has no attribute 'upper'
>>> for n in fruits:print(fruits.capitalize())
... 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'list' object has no attribute 'capitalize'
>>> for f in fruits:prints(f.upper)
... 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'prints' is not defined
>>> for f in fruits:print(f.upper())
... 
PINEAPPLE
PASSION
ORANGE
GRAPS
AVOCADO
MANGO
>>> for fruit in fruits:print(fruit.upper())
... 
PINEAPPLE
PASSION
ORANGE
GRAPS
AVOCADO
MANGO
>>> 
[3]+  Stopped                 python3
