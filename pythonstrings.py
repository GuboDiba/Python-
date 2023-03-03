Akirachix"
'i loveAkirachix'
>>> print('i love Akirachix'
... print('Akirachix','is a','good','school')
  File "<stdin>", line 2
    print('Akirachix','is a','good','school')
    ^
SyntaxError: invalid syntax
>>> x="cat"
>>> y="dog"
>>> print(F{y} is better than{x})
  File "<stdin>", line 1
    print(F{y} is better than{x})
           ^
SyntaxError: invalid syntax
>>> 
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> print(f"{y}is better than{x}")
dogis better thancat
>>> name="Rita Khaseyi"
>>> balance="1000000"
>>> print(f"Hello {name}, your current balace is {balance}")
Hello Rita Khaseyi, your current balace is 1000000
>>> print("Hello\b Akirachix")
Hell Akirachix
>>> print("Hello\n Akirachix")
Hello
 Akirachix
>>> print("Hello\r Akirachix")
 Akirachix
>>> print("Hello\t Akirachix")
Hello	 Akirachix
>>> print("Hello\v Akichix")
Hello
      Akichix
>>> print("Hello\a A")
Hello A
>>> print("a\ab")
ab
>>> len("Akirachix")
9
>>> len("Today is Friday")
15
>>> a in "Akirachix"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'a' is not defined
>>> "a" in "Akirachix"
True
>>> "z" in "Akirachix"
False
>>> "z" in "Akirachix"
False
>>> "a" not in "Akirachix"
False
>>> "z" not in "Akirachix"
True
>>> s="Akirachix"
>>> dir(s)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> x=10
>>> dir(x)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
>>> s.upper
<built-in method upper of str object at 0x7fbfcd7b63f0>
>>> s.Upper
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'str' object has no attribute 'Upper'
>>> s.upper()
'AKIRACHIX'
>>> s.lower()
'akirachix'
>>> s.tittle()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'str' object has no attribute 'tittle'
>>> s.title
<built-in method title of str object at 0x7fbfcd7b63f0>
>>> s.title()
'Akirachix'
>>> x="I am a student
  File "<stdin>", line 1
    x="I am a student
                    ^
SyntaxError: EOL while scanning string literal
>>> x.title()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'int' object has no attribute 'title'
>>> d=" i love python"
>>> d.title
<built-in method title of str object at 0x7fbfcd7bd770>
>>> d.title()
' I Love Python'
>>> d.capitalise()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'str' object has no attribute 'capitalise'
>>> d.capitalize
<built-in method capitalize of str object at 0x7fbfcd7bd770>
>>> d.capitalize()
' i love python'
>>> d.count("a")
0
>>> d.count(b)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'b' is not defined
>>> d.count("b")
0
>>> d.replace("o","a")
' i lave pythan'
>>> d
' i love python'
>>> d.replace("i love python","Akirachix")
' Akirachix'
>>> d.endswith("x")
False
>>> d.startswith("A")
False
>>> d.startswith("i")
False
>>> x="Akirachix"
>>> x.startswith("A")
True
>>> x.islower()
False
>>> d.islower()
True
>>> "hello".islower
<built-in method islower of str object at 0x7fbfcd7bd5f0>
>>> "hello".islower()
True
>>> d.isupper()
False
>>> x.isupper()
False
>>> "HELLO".isupper()
True
>>> x.isnumeric()
False
>>> "20".isnumeric
<built-in method isnumeric of str object at 0x7fbfcd7bd7b0>
>>> "20".isnumeric()
True
>>> "20 years".isnumeric()
False
>>> "0.3".isnumeric()
False
>>> "3.3".isnumeric90
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'str' object has no attribute 'isnumeric90'
>>> "3.3"
'3.3'
>>> x.isalpha
<built-in method isalpha of str object at 0x7fbfcd7b63f0>
>>> x.isalpha()
True
>>> x.isalnum()
True
>>> "20".alnum()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'str' object has no attribute 'alnum'
>>> "20".isalnum()
True
>>> "20 years".isalnum()
False
>>> x.isdigit()
False
>>> "20".isdigit()
True
>>> "20 years".isdigit()
False
>>> x.index("A")
0
>>> x.index("a")
4
>>> x.index("x")
8
>>> x.index("z")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: substring not found
>>> x.find("a")
4
>>> x.find("Z")
-1
>>> x.find("x")

