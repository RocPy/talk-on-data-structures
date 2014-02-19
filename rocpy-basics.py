import this
# OUT: The Zen of Python, by Tim Peters
# OUT: Beautiful is better than ugly.
# OUT: Explicit is better than implicit.
# OUT: Simple is better than complex.
# OUT: Complex is better than complicated.
# OUT: Flat is better than nested.
# OUT: Sparse is better than dense.
# OUT: Readability counts.
# OUT: Special cases aren't special enough to break the rules.
# OUT: Although practicality beats purity.
# OUT: Errors should never pass silently.
# OUT: Unless explicitly silenced.
# OUT: In the face of ambiguity, refuse the temptation to guess.
# OUT: There should be one-- and preferably only one --obvious way to do it.
# OUT: Although that way may not be obvious at first unless you're Dutch.
# OUT: Now is better than never.
# OUT: Although never is often better than *right* now.
# OUT: If the implementation is hard to explain, it's a bad idea.
# OUT: If the implementation is easy to explain, it may be a good idea.
# OUT: Namespaces are one honking great idea -- let's do more of those!
help
# OUT: Type help() for interactive help, or help(object) for help about object.
help()
# OUT: Welcome to Python 2.7!  This is the online help utility.
# OUT: If this is your first time using Python, you should definitely check out
# OUT: the tutorial on the Internet at http://docs.python.org/2.7/tutorial/.
# OUT: Enter the name of any module, keyword, or topic to get help on writing
# OUT: Python programs and using Python modules.  To quit this help utility and
# OUT: return to the interpreter, just type "quit".
# OUT: To get a list of available modules, keywords, or topics, type "modules",
# OUT: "keywords", or "topics".  Each module also comes with a one-line summary
# OUT: of what it does; to list the modules whose summaries contain a given word
# OUT: such as "spam", type "modules spam".
# OUT: help> this
# OUT: help> exit
# OUT: help> 
# OUT: You are now leaving help and returning to the Python interpreter.
# OUT: If you want to ask for help on a particular object directly from the
# OUT: interpreter, you can type "help(object)".  Executing "help('string')"
# OUT: has the same effect as typing a particular string at the help> prompt.
clear
# OUT: Traceback (most recent call last):
# OUT:   File "<input>", line 1, in <module>
# OUT: NameError: name 'clear' is not defined
clear()
# OUT: Traceback (most recent call last):
# OUT:   File "<input>", line 1, in <module>
# OUT: NameError: name 'clear' is not defined
reset
# OUT: Traceback (most recent call last):
# OUT:   File "<input>", line 1, in <module>
# OUT: NameError: name 'reset' is not defined
reset()
# OUT: Traceback (most recent call last):
# OUT:   File "<input>", line 1, in <module>
# OUT: NameError: name 'reset' is not defined
2+2
# OUT: 4
2 - 2
# OUT: 0
2 -3
# OUT: -1
2 - 3
# OUT: -1
2 * 4
# OUT: 8
2/3
# OUT: 0
2%3
# OUT: 2
2.3 + 3.6
# OUT: 5.9
5%2
# OUT: 1
1.0 + 3
# OUT: 4.0
#floatingpoint
#PEMDAS
1.0 + 3 * 5.0
# OUT: 16.0
(1.0+3)*5
# OUT: 20.0
(1.0+3)*5.
# OUT: 20.0
#don't need the "0" after the "." !
'string'
# OUT: 'string'
#strings
'string' + 3
# OUT: Traceback (most recent call last):
# OUT:   File "<input>", line 1, in <module>
# OUT: TypeError: cannot concatenate 'str' and 'int' objects
'string' + str(3)
# OUT: 'string3'
'string' + str('3')
# OUT: 'string3'
'string' * 3
# OUT: 'stringstringstring'
'string' / 3
# OUT: Traceback (most recent call last):
# OUT:   File "<input>", line 1, in <module>
# OUT: TypeError: unsupported operand type(s) for /: 'str' and 'int'
'string' * 0
# OUT: ''
'string' * -1
# OUT: ''
s = 'string'
s
# OUT: 'string'
s()
# OUT: Traceback (most recent call last):
# OUT:   File "<input>", line 1, in <module>
# OUT: TypeError: 'str' object is not callable
s * 3
# OUT: 'stringstringstring'
#samething
s(0)
# OUT: Traceback (most recent call last):
# OUT:   File "<input>", line 1, in <module>
# OUT: TypeError: 'str' object is not callable
s[0]
# OUT: 's'
s[1]
# OUT: 't'
s[-1]
# OUT: 'g'
s
# OUT: 'string'
s[2:]
# OUT: 'ring'
s[:2]
# OUT: 'st'
s[2:5]
# OUT: 'rin'
s[2:-1]
# OUT: 'rin'
len(s)
# OUT: 6
len(s[:2])
# OUT: 2
s * .5
# OUT: Traceback (most recent call last):
# OUT:   File "<input>", line 1, in <module>
# OUT: TypeError: can't multiply sequence by non-int of type 'float'
s.upper()
# OUT: 'STRING'
t = (1, 2, 3, 4)
t
# OUT: (1, 2, 3, 4)
t[0]
# OUT: 1
t[0
]
# OUT: 1
t[:-1]
# OUT: (1, 2, 3)
t+1
# OUT: Traceback (most recent call last):
# OUT:   File "<input>", line 1, in <module>
# OUT: TypeError: can only concatenate tuple (not "int") to tuple
t+t
# OUT: (1, 2, 3, 4, 1, 2, 3, 4)
t+t^2
# OUT: Traceback (most recent call last):
# OUT:   File "<input>", line 1, in <module>
# OUT: TypeError: unsupported operand type(s) for ^: 'tuple' and 'int'
t^2
# OUT: Traceback (most recent call last):
# OUT:   File "<input>", line 1, in <module>
# OUT: TypeError: unsupported operand type(s) for ^: 'tuple' and 'int'
t
# OUT: (1, 2, 3, 4)
#assignment
t[-1] = 5
# OUT: Traceback (most recent call last):
# OUT:   File "<input>", line 1, in <module>
# OUT: TypeError: 'tuple' object does not support item assignment
#tuples are immutable!
t = t[:-1]
t
# OUT: (1, 2, 3)
t = t[:-1][5]
# OUT: Traceback (most recent call last):
# OUT:   File "<input>", line 1, in <module>
# OUT: IndexError: tuple index out of range
t = t[:-1]+[5]
# OUT: Traceback (most recent call last):
# OUT:   File "<input>", line 1, in <module>
# OUT: TypeError: can only concatenate tuple (not "list") to tuple
#lists
#built-ins
len()
# OUT: Traceback (most recent call last):
# OUT:   File "<input>", line 1, in <module>
# OUT: TypeError: len() takes exactly one argument (0 given)
len('string')
# OUT: 6
type(5)
# OUT: <type 'int'>
l = [2, 3, 4, 5]
l.append('string')
l
# OUT: [2, 3, 4, 5, 'string']
l[2]
# OUT: 4
l[22]
# OUT: Traceback (most recent call last):
# OUT:   File "<input>", line 1, in <module>
# OUT: IndexError: list index out of range
#dict
d = {}
e = {2}
#sets
set([2, 3, 4])
# OUT: set([2, 3, 4])
j = set([2, 3, 4])
j
# OUT: set([2, 3, 4])
#dicts
d
# OUT: {}
d['key'] = 'val'
d
# OUT: {'key': 'val'}
d['key']
# OUT: 'val'
d['key'].strip()
# OUT: 'val'
d['key']
# OUT: 'val'
D = dict(keyword=3, k2='go')
D
# OUT: {'k2': 'go', 'keyword': 3}
d.values('3')
# OUT: Traceback (most recent call last):
# OUT:   File "<input>", line 1, in <module>
# OUT: TypeError: values() takes no arguments (1 given)
d.keys('3')
# OUT: Traceback (most recent call last):
# OUT:   File "<input>", line 1, in <module>
# OUT: TypeError: keys() takes no arguments (1 given)
d.viewkeys()
# OUT: dict_keys(['key'])
help(d)
help(d)
d.pop()
# OUT: Traceback (most recent call last):
# OUT:   File "<input>", line 1, in <module>
# OUT: TypeError: pop expected at least 1 arguments, got 0
d.pop('key')
# OUT: 'val'
d
# OUT: {}
d['key'] = 'val'
d.viewkeys()
# OUT: dict_keys(['key'])
d.viewitems
# OUT: <built-in method viewitems of dict object at 0x2274bc0>

d.viewitems()
# OUT: dict_items([('key', 'val')])
d.viewitems().strip()
# OUT: Traceback (most recent call last):
# OUT:   File "<input>", line 1, in <module>
# OUT: AttributeError: 'dict_items' object has no attribute 'strip'
#nested lists
nest = [[1, 2, 3], [2, 3, 4]]
nest
# OUT: [[1, 2, 3], [2, 3, 4]]
len(nest)
# OUT: 2
nest[0]
# OUT: [1, 2, 3]
nest[0[1]]
# OUT: Traceback (most recent call last):
# OUT:   File "<input>", line 1, in <module>
# OUT: TypeError: 'int' object has no attribute '__getitem__'
nest[0][1]
# OUT: 2
max(nest)
# OUT: [2, 3, 4]
max(max(nest))
# OUT: 4
for i in l:
    print(i)
    

# OUT: 2
# OUT: 3
# OUT: 4
# OUT: 5
# OUT: string
range(10)
# OUT: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[i for i in [1, 2, 3]]
# OUT: [1, 2, 3]
#list comprehensions
[i+2 for i in [1, 2, 3]]
# OUT: [3, 4, 5]
#ftw!
