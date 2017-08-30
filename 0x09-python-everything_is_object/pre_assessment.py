"""Pre-assessment for Python object questions
   See comment to compare anwer with test result"""

""" 0. A function that prints the object type"""
>>> a = 68
>>> type(a)
<class 'int'>


""" 1. Get the function identifier, which is the memory
      address in the Cpython implementation"""
>>> a = "string"
>>> id(a)
140515731787480


""" 2. Same object?"""
>>> a = 89
>>> b = 100
>>> id(a) == id(b)
False
>>> a is b
False

""" 3. Same object?"""
>>> a = 89
>>> b = 89
>>> id(a) == id(b)
True
>>> a is b
True
>>> a == b
True

""" 4. Same object?"""
>>> a = 89
>>> b = a
>>> id(a) == id(b)
True
>>> a is b
True
>>> a == b
True

""" 5. Same object?"""
>>> a = 89
>>> b = a + 1
>>> id(a) == id(b)
False
>>> a is b
False

""" 6. Output check - Is equal?"""
>>> s1 = "Holberton"
>>> s2 = s1
>>> print(s1 == s2)
True
>>> id(s1) == id(s2)
True

""" 7. Output check - Is the same?"""
>>> s1 = "Holberton"
>>> s2 = s1
>>> print(s1 is s2)
True

""" 8. Output check - Is really equal?"""
>>> s1 = "Holberton"
>>> s2 = "Holberton"
>>> print(s1 == s2)
True

""" 9. Output check - Is really the same?"""
>>> s1 = "Holberton"
>>> s2 = "Holberton"
>>> print(s1 is s2)
True

""" 10. Output check (list) - Is it equal?"""
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3]
>>> print(l1 == l2)
True

""" 11. Output check (list) - Is it the same?"""
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3]
>>> print(l1 is l2)
True  # Incorrect

""" 12. Output check (list) - Is it really equal?"""
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 == l2)
True

""" 13. Output check (list) - Is it really the same?"""
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 is l2)
True

""" 14. Output check - append"""
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> l1.append(4)
>>> print(l2)
[1, 2, 3, 4]

""" 15. Output chec - add"""
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> l1 = l1 + [4]
>>> print(l2)
[1, 2, 3]

""" 16. Integer Incrementation"""
>>> def increment(n):
...     n += 1

>>> a = 1
>>> increment(a)
>>> print(a)
2  # Incorrect

""" 17. List Incrementation"""
>>> def increment(n):
...     n.append(4)
>>> l = [1, 2, 3]
>>> increment(l)
>>> print(l)
[1, 2, 3, 4]


""" 18. List assignation"""
>>> def assign_value(n, v):
...     n = v
>>> l1 = [1, 2, 3]
>>> l2 = [4, 5, 6]
>>> assign_value(l1, l2)
>>> print(l1)
[4, 5, 6]  # Incorrect


""" 19. Copy a list object"""
>>> l = [12, 14, 16]
>>> def copy_list(l):
...     new_list = l
...     return new_list
>>> print(new_list)
[12, 14, 16]
>>> id(l) == id(new_list)
True


""" 20. Tuple or not?"""
>>> a = ()
>>> type(a)
<class 'tuple'>  # Correct
>>> a is tuple
True  # Incorrect (why?)


""" 21. Tuple or not?"""
>>> a = (1, 2)
>>> type(a)
<class 'tuple'>  # Correct
>>> a is tuple
True  # Incorrect (why?)


""" 22. Tuple of not?"""
>>> a = (1)
>>> type(a)
<class 'int'>
>>> a is tuple
False


""" 23. Tuple or not?"""
>>> a = (1, )
>>> type(a)
<class 'tuple'>
>>> a is tuple
True  # Incorrect (why?)


""" 24. Output check - Richard Sim #0"""
>>> a = (1)
>>> b = (2)
>>> a is b
False


""" 25. Output check - Richard Sim #1"""
>>> a = (1, 2)
>>> b = (1, 2)
>>> a is b
True  # Incorrect


""" 26. Output check - Richard Sim #2"""
>>> a = ()
>>> b = ()
>>> a is b
True


""" 27. Output check - Richard Sim #3"""
>>> id(a)
139926795932424
>>> a
[1, 2, 3, 4]
>>> a = a + [5]
>>> id(a)
id(a_after) == id(a_before)  => False

>>> print(a)
TypeError: can't concatenate lists  # Incorrect: a = [1, 2, 3, 4, 5]


""" 28. Output check - Richard Sim #4"""
>>> a
[1, 2, 3]
>>> id (a)
139926795932424
>>> a += [4]
>>> id(a) == 139926795932424
False  # Incorrect
>>> print(a)
TypeError: cannot concatenate  # Incorrect; a = [1, 2, 3, 4]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
