# Please answer the practice questions at the end of chapters 1-6 here under the cooresponding comment:

# # Chapter 1
# #1.)*, -, +, /
# #2.) 'spam'
# 3.) string, integer, and float
# 4.)Most basic kind of programming intruction
# 5.)An experession involes mathmatical operations between numbers, while an assignment statements are the storing of data which can be strings, integers, or floats.
# 6.)21
# 7.)'spamspamspam'
# 'spamspamspam'
# 8.)It does not have anyspaces and doesn't begin with a number.
# 9.)str(), int(), float()
# 10.) Because you cannot add a string and integer togeter.

# # Chapter 2
# 1.)True and False. Write them with the first letter capitalized.
# 2.) and, or, and not.
# 3.)and- True and True: True, True and False: False, False and True: False, False and False: False 
# or- True or True:True, True or False: True, False or True: True, False or False: False
# not- not True: False, not False: True
# 4.)False, False, True, False, False, True
# 5.)==,!=,>,<,<=,>=
# 6.) The equal opertator is determining whether two values are equviliant, while the assignment operators are storing values.
# 7.)A condition is an experssions that always evaluates down to a Boolean value, True or False.
# 8.)print('eggs'), print('bacon'), print('ham')
# 9.)if spam == 1:
#     print('Hello')
# elif spam ==2:
#     print('Howdy')
# else:
#     print('Greetings')
# 10.)What keys can you press if your program is stuck in an infinite loop? CRTL-C
# 11.)What is the difference between break and continue? The break statement with exist the loop by writng break into the code. Continue will jump back into a loop and rerun the loop condition from there.
# 12.)What is the difference between range(10), range(0, 10), and range(0, 10, 1) in a for loop? range(10) will add up all the values in from 0 to 1. range(0, 10) will give all the numbers from 0 upto 10, but not including 10. range(0,10,1) will give the range from ) upto 10, and will display them in interval of 1. 

# 13.) Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.
# For num in range(1,11)
#     print(num)
# 14.)If you had a function named bacon() inside a module named spam, how would you call it after importing spam?
# bacon.spam()

# # Chapter 3
# 1. Why are functions advantageous to have in your programs?
#  It groups code that gets executed multiple times, without have to copy and paste multiple times.
# 2. When does the code in a function execute: when the function is defined or when the function is called? 
#  When the function is called.
# 3. What statement creates a function?
#  The def statement creats a functions.
# 4. What is the difference between a function and a function call?
#  A function is the piece of code that is defined to be ran, while a called function is the running of that specific piece of programing.
# 5. How many global scopes are there in a Python program? How many local scopes? 
#  There is one global sccope in a python program. 
# 6. What happens to variables in a local scope when the function call returns? 
#  The variables are destroyed.
# 7. What is a return value? Can a return value be part of an expression?
#  The return value is the value that a function calls. Yes, a return value can be used in an expression.
# 8. If a function does not have a return statement, what is the return value of a call to that function?
#  None
# 9. How can you force a variable in a function to refer to the global variable?
#  Use a global statement in the function.
# 10. What is the data type of None? 
#  NoneType
# 11. What does the import areallyourpetsnamederic statement do? 
#  It will import the module areallypourpetsnamederic to python so that phython will be able to understand it when ran.
# 12. If you had a function named bacon() in a module named spam, how would you call it after importing spam? 
#  spam.bacon()
# 13. How can you prevent a program from crashing when it gets an error? 
#  You would use the try and except statement. 
# 14. What goes in the try clause? What goes in the except clause? 
#  The valid arguements go in the try clause and the errored argument goes within the except statement.

# # Chapter 4
# 1. What is []?
#  Denotes a list, and item stored inside theses bracket are list items.
# 2. How would you assign the value 'hello' as the third value in a list stored in a variable named spam? (Assume spam contains [2, 4, 6, 8, 10].)
#  spam = [2,4,'hello', 6, 8]
# For the following three questions, let’s say spam contains the list ['a', 'b', 'c', 'd'].
# 3. What does spam[int(int('3' * 2) // 11)] evaluate to? 
# 'd'
# 4. What does spam[-1] evaluate to? 
# 'd'
# 5. What does spam[:2] evaluate to?
#  ['a', 'b', 'c']
# For the following three questions, let’s say bacon contains the list [3.14, 'cat', 11, 'cat', True].
# 6. What does bacon.index('cat') evaluate to?
#  1
# 7. What does bacon.append(99) make the list value in bacon look like? 
#  bacon=[3.14, 'cat', 11, 'cat', True, 99]
# 8. What does bacon.remove('cat') make the list value in bacon look like? 
#  bacon=[3.14, 11, 'cat', True]
# 9. What are the operators for list concatenation and list replication? 
#  The operators are + to combine values and * to replicate list.

# 10. What is the difference between the append() and insert() list methods? 
#  append() will add an item to the end of a list and insert() allows one to choose where exactly in a list an item will go.

# 11. What are two ways to remove values from a list? 
#  remove() and del()

# 12. Name a few ways that list values are similar to string values. 
#  Both are called items, can be store as variables, and have to be contained within parameteres []for list and ''or ""for a string value.

# 13. What is the difference between lists and tuples? 
#  List use [], while tiples use (). Tuplues can not be modified, appended or removed.
# 14. How do you type the tuple value that has just the integer value 42 in it?
#  int(tuple('42'))
# 15. How can you get the tuple form of a list value? How can you get the list form of a tuple value? 
#  tuple([]) and list (()).
# 16. Variables that “contain” list values don’t actually contain lists directly. What do they contain instead? 
#  They contain a refernce to the list.
# 17. What is the difference between copy.copy() and copy.deepcopy()? 
#  copy.copy() will make dulicate of a list or dictionary and copy.deepcopy( ) will make a copy of list within list.

#  # Chapter 5
# 1. What does the code for an empty dictionary look like?
#  dictionary = {}
# 2. What does a dictionary value with a key 'foo' and a value 42 look like?
#  {'foo':42}
# 3. What is the main difference between a dictionary and a list? 
#  Dictionaries are not order while list are.
# 4. What happens if you try to access spam['foo'] if spam is {'bar': 100}? 
#  You would get a KeyError error message.
# 5. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.keys()? 
#  'cat' in spam.keys() will return the key associated with 'cat'.
# 6. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.values()?
#  'cat' in spam.value() will return the value associated with 'cat'.
# 7. What is a shortcut for the following code?
# if 'color' not in spam:
#     spam['color'] = 'black'
# answer:spam.setdefault('color', 'black')
# 8. What module and function can be used to “pretty print” dictionary values? 
#  pprint.pprint()

# # Chapter 6
# 1. What are escape characters?
#  Escape charaters are characters that let you add impossible characters to a string.
# 2. What do the \n and \t escape characters represent? 
#  \n- new line(line break) \t- Tab
# 3. How can you put a \ backslash character in a string? 
# \\
# 4. The string value "Howl's Moving Castle" is a valid string. Why isn’t it a problem that the single quote character in the word Howl's isn’t escaped?
#  Because it uses doule quotation marks on the outside of the string.
# 5. If you don’t want to put \n in your string, how can you write a string with newlines in it?
#  One would use three single or double quotation marks if they did not want to use \n. 
# 6. What do the following expressions evaluate to?
# 'Hello, world!'[1]
# 'Hello, world!'[0:5]
# 'Hello, world!'[:5]
# 'Hello, world!'[3:]
# answer:'e', "Hello", 'Hello', 'lo, world!'
# 7. What do the following expressions evaluate to?
# 'Hello'.upper() 
# 'Hello'.upper().isupper()
# 'Hello'.upper().lower()
# answer: 'HELLO', True, 'hello'
# 8. What do the following expressions evaluate to?
# 'Remember, remember, the fifth of November.'.split()
# '-'.join('There can be only one.'.split()) 
# answer:'Remember', ',', 'remember', ',', 'the', 'fifth', 'of', 'November'
# 'There_', can_,'be_', 'only_', 'one'

# 9. What string methods can you use to right-justify, left-justify, and center a string? 
#  rjust(), ljust(), or center()
# 10. How can you trim whitespace characters from the beginning or end of a string?
#  To remove white space from the beginning or the end of a string would involve using strip(), rstrip(), or the lstrip().


