#################################################################
############################################## (Intruduction)
#########################################################
# Things should be always remember

print(help('modules')) # A list of all available modules within python
import os # (importing module)
print(dir(os)) # all methods and attributes exists within given module

import os
print(os.getcwd()) # apply any method/attributes on any builts-on/custom objects just putting . after objects/instance of class

my_list = [1,2,3,4]
print(my_list.__doc__) #Get documentions of any objects/instance of class

import keyword
print(keyword.kwlist) # Python all reserved word which has special meaning in python 

# Note: If Using Jupyter notebook shift+tab within method parenthesis give access to details
#########################################################
######### Question #* Say "Hello, World!" With Python
if __name__ == '__main__':
    print("Hello, World!")

#########################################################
################### Question #* Python If-Else
# 🔑 strip(), if, elif, else
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 != 0:
        print("Weird")
    elif n % 2 == 0 and n in range(2, 6):
        print("Not Weird")
    elif n % 2 == 0 and n in range(6, 21):
        print("Weird")
    elif n % 2 == 0 and n > 20:
        print("Not Weird")

#Trick for summarise if elif
# Example1:-
item = 4
if item % 2 == 0:
    print("even")
else:
    print("odd") 
# output:- even

item = 4
print("even" if item % 2 == 0 else "odd")
# output:- even

# Example2:-
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 8, 9]
my_comp = ("even" if i % 2 == 0 else "odd" for i in my_list)
print(*my_comp, sep="\n")
# >>> odd
# >>> even
# >>> odd 
# >>> even
# >>> odd 
# >>> even
# >>> odd 
# >>> even
# >>> even
# >>> odd


# Example3:-
my_list = [1,2,3,4,5,6,67,8,8,9]
for i in my_list:
    if i%2==0 :
        print("div_by_2")
    elif i%3 == 0:
        print("div_by_3")
    elif i%4 == 0:
        print("div_by_4")
    else:
        print("not_divisible")
# Note in genrator comp or list compre if statement always expect else
# >>> not_divisible
# >>> div_by_2     
# >>> div_by_3     
# >>> div_by_2     
# >>> not_divisible
# >>> div_by_2     
# >>> not_divisible
# >>> div_by_2     
# >>> div_by_2     
# >>> div_by_3

my_list = [1, 2, 3, 4, 5, 6, 67, 8, 8, 9]
map_dict = {
    2: "div_by_2",
    3: "div_by_3",
    4: "div_by_4"
}
my_comp = [map_dict.get(i, "not_divisible") for i in my_list]
print(*my_comp, sep="\n")
# >>> not_divisible
# >>> div_by_2     
# >>> div_by_3     
# >>> div_by_4     
# >>> not_divisible
# >>> not_divisible
# >>> not_divisible
# >>> not_divisible
# >>> not_divisible
# >>> not_divisible

# statements are typically used for performing actions and control flow, while expressions are used for computing values.
# Expressions can often be embedded within statements to calculate values or make decisions based on those values.

#########################################################
################### Question #* Arithmetic Operators
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    sum_ = a+b
    diff = abs(a-b)
    product = a*b
    print(f"{sum_}\n{diff}\n{product}")
    # or output = '\n'.join([str(sum_), str(diff), str(product)])
    # print('\n'.join(map(str, (sum_, diff, product))))
    # print(sum_, diff, product, sep='\n')
    

"""
In Python's print function, sep is a parameter that determines the separator
between the different arguments that are passed to the function.
It is not a function itself but a parameter of the print function.
By default, the sep parameter is set to ' ' (a single space character)
but you can change as you want for example:-
a = 2
b = 3
c = 4
print(a,b,c, sep=" # ")
# >>> 2 # 3 # 4
"""

#########################################################
################### Question #* Python: Division
# 🔑 Division Operator (/), Floor Division Operator (//)
# In Python, the division operator (/) performs floating-point division by default
"""
Division Operator (/):

The division operator / performs floating-point division, regardless of the operand types.
It returns a floating-point result, even if the operands are integers.
The result may have decimal places, representing the fractional part of the division.

Floor Division Operator (//):

The floor division operator // performs integer division, which rounds the result down to the nearest integer (floor).
If both operands are integers, the result will be an integer.
If one or both operands are floats, the result will be a float.

Example

"""
a = 10
b = 3
result = a / b
print(result)  # Output: 3.3333333333333335

a = 10
b = 3
result = a // b
print(result)  # Output: 3

# *question answer
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    int_div = a//b
    float_div = a/b
    print(int_div)
    print(float_div)


#########################################################
################### Question #*Loops
# 🔑 loop
# 1st method
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i**2)

# 2nd method by defining function
if __name__ == '__main__':
    def square(n):
        return n*n
    n = int(input())
    for i in range(n):
        print(square(i))

# 3rd method by defining function
n = 5
squared = pow(n, 2)
print(squared)  # Output: 25

"""
pow:- with you can square,cube any exp you want
The first argument is the base number, and the second argument is the exponent.
syntac pow(number, exponent)
"""

#########################################################
################### Question #*Write a function
def is_leap(year):
    leap = False
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True  # Leap year if divisible by 400
            else:
                return False  # Not a leap year if divisible by 100 but not by 400
        else:
            return True  # Leap year if divisible by 4 but not by 100
    else:
        return False  # Not a leap year if not divisible by 4
    return leap

year = int(input())
print(is_leap(year))


#########################################################
##################### Question #* Print Function
# *"STDIN" refers to the standard input stream. It is a way to receive input from the user.
# 1st method by using join() method
if __name__ == '__main__':
    n = int(input())
    li = []
    for i in range(1, n+1):
        li.append(i)
    print("".join(str(x) for x in li))  # join except only str object

# 2nd method by using seprater
if __name__ == '__main__':
    n = int(input())
    li = []
    for i in range(1, n+1):
        li.append(i)
    print(*li, sep='')

# 3rd method by using end
if __name__ == '__main__':
    n = int(input())
    for i in range(1, n+1):
        print(i, end="")


########################################################
#################################### (Basic Data Types)
#########################################################
############# Question #*List Comprehensions
# 🔑 List Comprehensions
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    result = [[i, j, k] for i in range(
        x+1) for j in range(y+1) for k in range(z+1) if (i+j+k) != n]
    print(result)

# 2nd method by using loop
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    li = []
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                li.append(i, j, k)
                if (i+j+k) != n:
                    pass


############################################################
################ Question #* Find the Runner-Up Score!
# 🔑 sort(), sorted()
# Note: map creed object not a list or tup
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    print(*arr[-3:-2])

# 2nd method sort
if __name__ == '__main__':
    n = int(input())
    arr = set(map(int, input().split()))
    arr_ = list(arr)
    arr_.sort(reverse=True)
    print(arr_[1])

# 3rd method sorted
if __name__ == '__main__':
    n = int(input())
    arr = set(map(int, input().split()))
    arr_ = sorted(arr, reverse=True)  # orarr_ = sorted(arr, reverse = True)[1]
    print(arr_[1])


############################################################
######################## Question #* Nested lists
# 🔑 nested list
# Note: Square brackets are used for indexing or accessing elements, whereas parentheses are used for calling functions.
# * For receive input from the user in the specific range you can use "for _ in range(int(input()))"

"""
some situations where _ is usefull in the loop:
* 1.Discarding Values: commonly used in situations where the value is returned by a function or unpacked from a sequence, but you don't need it.
* 2.Ignoring Index:
* 3.Localization Markers: 
* 4.Placeholder Variables:
example is mentioned below
The use of the underscore as a convention helps improve code readability and communicates the intent clearly.
"""

# 1.Discarding Values
# Or some_function() # Assign only the second value, discarding the first
_, y = input().split()
for _ in range(5):  # Ignore the loop variable
    # Perform some repetitive task
    pass  # don't forgot to use pass method otherwise for loop expect indented block bcz python directly ignored comment

# 2.Ignoring Index
my_list = [1, 2, 3, 4, 5]
for _ in my_list():
    # Process each item without using the index
    pass

# 3.Localization Markers
def greet():
    print(_("Hello, World!"))  # Mark the string for translation

# 4.Placeholder Variables
# Calculate the sum of a list of numbers
numbers = [1, 2, 3, 4, 5]
_ = sum(numbers)  # Store the sum temporarily


#  1st method by using sort & set function
# Note sort() method expects a key function that specifies the sorting criteria.
# specially with lambda fxn key provides flexibility in specifying the sorting criteria
# * --and enables you to customize the sorting behavior based on specific requirements.
#  more on here https://docs.python.org/3/howto/sorting.html
if __name__ == '__main__':
    my_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        my_list.append([name, score])
    scores = sorted(set(score for name, score in my_list))
    second_lowerscore = scores[1]
    li_sorted = []
    for i in my_list:
        if i[1] == second_lowerscore:  # access the second element of the sublist
            li_sorted.append(i)
    li_sorted.sort(key=lambda x: x[0])
    print("\n".join(str(x[0]) for x in li_sorted))


# 2nd method Using list comprahension
records = [[input(), float(input())]for _ in range(int(input()))]
score = list(set([i[1] for i in records]))
score.sort()
second_smallest_score = score[1]
student = [i[0] for i in records if i[1] == second_smallest_score]
student.sort()
print(*student, sep="\n")
# for i in student:
# print(i)

# Or
if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
    scores = [i[1] for i in records]
    runner_score = sorted(set(scores))[1]
    # Or runner_score = sorted(set([i[1] for i in records]))[1]
    names = sorted(i[0] for i in records if i[1] == runner_score)
    print(*names, sep='\n')
    # Or directly print(*sorted(names), sep = '\n')

# Remeber:-The sort() method is used to sort a list in-place, meaning it modifies the original list directly.
# * --This method does not return a new list but rather returns None so if you assign it to a varible
# * -- u'll get error "TypeError: 'NoneType' object is not subscriptable (key 1)""
# * Usually it’s less convenient than sorted() - but if you don’t need the original list, it’s slightly more efficient.


# 3rd method using loop functions
if __name__ == '__main__':
    my_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        my_list.append([name, score])

    # Find the minimum and second minimum scores
    scores = set(score for name, score in my_list)
    sorted_scores = sorted(scores)
    second_lowest_score = sorted_scores[1]

    # Find the names with the second lowest score
    li_sorted = [name for name,
                score in my_list if score == second_lowest_score]
    li_sorted.sort()
    # Print the names
    for name in li_sorted:
        print(name)
    # Or print(*li_sorted, sep="\n")


# 4th by using dictionary method
# Python3
if __name__ == '__main__':
    a = []
    key_value = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        a.append(score)
        if score in key_value:
            key_value[score] += "-"+name
        else:
            key_value[score] = name
        # Or you can do it directly by using get method in one line
        # *-- key_value[score] = key_value.get(score, []) + [name]
    a = sorted(set(a))
    answer = key_value[a[1]]
    answer = sorted(str(answer).split("-"))
    print("\n".join(answer))


# 5th method using collections method
from collections import defaultdict
if __name__ == '__main__':
    scores = set()
    names = defaultdict(list)
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        scores.add(score)
        names[score].append(name)

    second_lowest = sorted(scores)[1]
    sorted_names = sorted(names[second_lowest])
    for name in sorted_names:
        print(name)


# 6th methed
records = [[input(), float(input())] for _ in range(int(input()))]
records = sorted(records, key=lambda x: x[1])
uniq_scr = []
[uniq_scr.append(y[1]) for y in records if y[1] not in uniq_scr]
temp = sorted([i[0] for i in records if i[1] == uniq_scr[1]])
for j in temp:
    print(j)


# 7th methed
records = [[input(), float(input())]for _ in range(int(input()))]
score = list(set([i[1] for i in records]))
score.sort()
second_smallest_score = score[1]
student = [i[0] for i in records if i[1] == second_smallest_score]
student.sort()
for i in student:
    print(i)


##########################################################################
################ Question #* Finding the percentage
# 🔑 f-string
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    score = list(student_marks[query_name])
    sum = 0
    for i in score:
        sum = i + sum
    num = sum/3
print(f"{num:.2f}")  # f-string method
"""
Here are some of the formatting options that you can use with f-strings:

.2f - Rounds the number to two decimal places.
.0f - Removes any decimal places from the number.
%d - Converts the number to a decimal integer.
%s - Converts the number to a string.
"""

# 2nd method using comprehension method
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
print("%.2f" % (sum(
    score for score in student_marks[query_name]) / len(student_marks[query_name])))


###########################################################################
################ Question #* Lists
# Note n, *args = input().split() #* args returns list (<class 'list')>
# Remember : [] are used for indexing or accessing elements, whereas () are used for calling functions.
# 🔑 *arg, split(), insert(), remove(), append(), sort(),pop(),reverse()
if __name__ == '__main__':
    N = int(input())
    my_list = []
    for _ in range(N):
        command, *arg = input().split()
        arg = list(map(int, arg))
        if command == "insert":
            my_list.insert(arg[0], arg[1])
        elif command == "print":
            print(my_list)
        elif command == "remove":
            my_list.remove(arg[0])
        elif command == "append":
            my_list.append(arg[0])
        elif command == "sort":
            my_list.sort()
        elif command == "pop":
            my_list.pop()
        elif command == "reverse":
            my_list.reverse()

# 2nd method using eval() method
N = int(input())
List = []
for _ in range(N):
    Line = input().split()
    if Line[0] != "print":
        cmd = Line[0] + "(" + ",".join(Line[1:]) + ")"
        eval("List."+cmd)
    else:
        print(List)

#  Or more better way to try
if __name__ == '__main__':
    N = int(input())
    arr = []
    for i in range(N):
        opCommand, *args = input().split()
        if opCommand == "print":
            print(arr)
        else:
            exp = ','.join(args)
            eval(f'arr.{opCommand}({exp})')

    N = int(input())
    arr = []
    for _ in range(N):
        cmd, *values = input().split()
        values = tuple(map(int, values))
        if cmd == 'print':
            print(temp)
        else:
            eval(f"arr.{cmd}{values}")


# 3rd method using gettr() method
if __name__ == "__main__":
    the_list = []
    number_of_input_lines = int(input())

    for _ in range(number_of_input_lines):
        tokens = input().split()

        if tokens[0] == "print":
            print(the_list)
        else:
            method = getattr(the_list, tokens[0])
            args = [int(t) for t in tokens[1:]]
            method(*args)


#####################################################################
################ Question #*Tuples Question #*Tuples
# keyconcept hash(), tuple
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    int_tup = tuple(integer_list)
    print(hash(int_tup))


############################################################
###########################################################
################################### Question #* (String)
###########################################################

###################################################################
################################### Question #* Swapcase
# 🔑 join, swapcase, islower(), isupper(), lower(), upper() fuxn
def swap_case(s):
    string = ""
    for i in s:
        if i.islower():
            string = string + i.upper()
        elif i.isupper():
            string = string + i.lower()
        else:
            string = string + i
    return string
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

# 2nd method using bult-in method swapcase()
def swap_case(s):
    string = s.swapcase()
    return string

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

# 3rd method using join and list comprehention
def swap_case(s):
    string = ''.join(i.upper() if i.islower() else i.lower() for i in s)
    return string
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)


###########################################################################
#################################### Question #* String Split and Join
# 🔑 join, split
def split_and_join(line):
    split_sent = '-'.join(k for k in line.split())
    return split_sent

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)


###########################################################################
#################################### Question #* What's Your Name?
# 🔑print & f-string
def print_full_name(first, last):
    print(f"Hello {first} {last}! You just delved into python.")

    # print("Hello",first,last + "!","You just delved into python.")
if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)


###########################################################################
#################################### Question #* Mutations
# 🔑 list, join method
def mutate_string(string, position, character):
    my_list = list(string)
    my_list[position] = character
    string = ''.join(my_list)
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

# 2nd method using string slicing
def mutate_string(string, position, character):
    string = string[:position] + character + string[position+1:]
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)


###########################################################################
################################### Question #* Find a string
# 🔑  using find method
# 1st method
def count_substring(string, sub_string):
    string_count = string.find(sub_string)
    return string_count
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    count = count_substring(string, sub_string)
    print(count)


# 2nd method using iterating over for loop
def count_substring(string, sub_string):
    count = 0
    for i in range(len(string) - len(sub_string) + 1):
        if string[i:i+len(sub_string)] == sub_string:
            count += 1
    return count
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    count = count_substring(string, sub_string)
    print(count)


###########################################################################
################################# Question #* String Validators
# 🔑 str.isalnum(), str.isalpha(), str.isdigit(), str.isupper(),get , any all, any
# 1st method
s = input()
lower = False
upper = False
alnum = False
num = False
alph = False
for i in s:
    if i.islower():
        lower = True
    if i.isupper():
        upper = True
    if i.isdigit():
        num = True
        alnum = True
    if i.isalpha():
        alph = True
        alnum = True
print(alnum, alph, num, lower, upper, sep="\n")


# 2nd methed using getattr
# * getattr provides a way to retrieve attributes dynamically, based on a given name or string.
# * getattr(object, attribute_name, default) Example:-
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("John", 25)
name = getattr(person, "name")
print(name)  # Output: John

age = getattr(person, "age")
print(age)  # Output: 25

city = getattr(person, "city", "Unknown")
print(city)  # Output: Unknown

# --
if __name__ == '__main__':
    s = input()
    command = ['isalnum', 'isalpha', 'isdigit', 'islower', 'isupper']
    for method in command:
        print(any(getattr(i, method)() for i in s))

# 3nd method using any() method
# *Returns True if at least one element in the iterable is considered True (non-zero, non-empty, or True boolean value)
    # *Stops iteration and returns True as soon as it encounters the first True element.
    # *Useful for checking if any element satisfies a condition.
    # any() returns True if at least one element is True after stoped excuting on empty retrun False
# *all() The all() takes an iterable as an argument. It returns True if all elements in the iterable are considered True (non-zero, non-empty, or True boolean value). Otherwise, it returns False.
    # *all() returns True only if all elements are True
    # *Useful for checking if all elements satisfy a condition.
    # all() returns True only if all elements are True empty return True
s = input()
print(any(i.isalnum() for i in s))
print(any(i.isalpha() for i in s))
print(any(i.isdigit() for i in s))
print(any(i.islower() for i in s))
print(any(i.isupper() for i in s))
# Or even
if __name__ == '__main__':
    s = input()
print(any([i.isalnum() for i in s]), any([i.isalpha() for i in s]), any([i.isdigit()
                                                                        for i in s]), any([i.islower() for i in s]), any([i.isupper() for i in s]), sep='\n')


# 4th method Using eval() method
# * the eval() function is a built-in function that evaluates a given string as a Python expression.
#   *Allows you to dynamically execute code represented as a string.
# example () eval(expression, globals=None, locals=None)
x = 10
y = 20
expression = "x + y"
result = eval(expression)
print(result)  # Output: 30

# --
if __name__ == '__main__':
    s = input()
    for method in ('.isalnum()', '.isalpha()', '.isdigit()', '.islower()', '.isupper()'):
        if any(eval('i'+method) for i in s):
            print(True)
        else:
            print(False)


##############################################################################
#################################### Question #* Text Alignment
# 🔑 center(), ljust, rjust
width = 20
print('HackerRank'.center(width, '-'))  # By default it takes argument as space
# -----HackerRank-----

width = 20
print('HackerRank'.ljust(width, '-'))
# HackerRank----------

width = 20
print('HackerRank'.rjust(width, '-'))
# ----------HackerRank

width = 20
print(''.rjust(width, '-'))
# --------------------

width = 20
print('*'.rjust(width, '-'))
# -------------------*

width = 20
print('*'.ljust(width, '-'))
# *-------------------

# Question
thickness = 5  # This must be an odd number
c = 'H'

# print V
num_rows = 7  # Number of rows in the "V" shape

for i in range(num_rows):
    # Print spaces before the left half of the "V"
    print(' ' * i, end='')

    # Print stars for the left half of the "V"
    print('*', end='')

    # Print spaces between the two halves of the "V"
    print(' ' * (2 * (num_rows - i - 1)), end='')

    # Print stars for the right half of the "V"
    print('*')

# example for more clearance
star = "*"
line = 7
for i in range(1, line+1):
    print(star.rjust(i) + (star.ljust(line+i)))


star = "*"
line = 7
for i in range(0, line):
    print(" " * i, end='')
    print('*', end='')
    print(' ' * (2 * (line - i - 1)), end='')
    print('*')

# -- QAnswer
# Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

# Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

# Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))

# Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

# Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c +
        (c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))


thickness = 5  # This must be an odd number
c = 'H'
# Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1, "-")+c+(c*i).ljust(thickness-1, "-"))

# Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2, "-") +
        (c*thickness).center(thickness*6, "*"))

# Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6, "-"))

# Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2, "-") +
        (c*thickness).center(thickness*6, "-"))

# Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness, "-")+c +
        (c*(thickness-i-1)).ljust(thickness, "-")).rjust(thickness*6, "-"))


# * Find() Method: -
""" The .find() method is a built-in string method in Python 
that is used to find the first occurrence of a substring within a string.
It returns the index of the first occurrence of the substring, or -1
if the substring is not found.The syntax for using the .find() method is as follows:

string.find(substring, start, end)

Here's what each parameter represents:
string:  In which you want to search for the substring.
substring:  you want to find within the string.
start (optional): the starting index of the search. The .find() method will start searching from this index. If not provided, the search will begin from the beginning of the string (index 0).
end (optional): Ending index of the search. The .find() method will search for the substring up to, but not including, this index. If not provided, the search will continue until the end of the string. 

*Example : """

string = "Hello, world!"
substring = "world"
index = string.find(substring)
print(index)  # Output: 7

# *  Any() Function:=

"""
The any() function is a built-in Python function that takes an iterable
(such as a list, tuple, or generator expression) as an argument.
It returns True if at least one element in the iterable evaluates to True,
and False if all elements evaluate to False or if the iterable is empty.
"""

num_rows = 7
for i in range(7):
    print(" "*i, end="")
    print("*", end="")
    print(' ' * (2 * (num_rows - i - 1)), end='')
    print("*")


####################################################################################
############################################# Question #* Text Wrap
# # 🔑 textwrap module and their wrap() & fill fuxn
# Textwrap:- The textwrap module provides two convenient functions: wrap() and fill().
import textwrap
string = "This is a very very very very very long string."
print(textwrap.wrap(string, 8))
# >>> ['This is', 'a very', 'very', 'very', 'very', 'very', 'long', 'string.']

string = "This is a very very very very very long string."
print(textwrap.fill(string, 8))
# >>> This is
# >>> a very
# >>> very
# >>> very
# >>> very
# >>> very
# >>> long
# >>> string.

# -- QAnswer
def wrap(string, max_width):
    my_result = textwrap.fill(string, max_width)
    return my_result

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)


#######################################################################
############################## Question #*(Designer Door Mat)
# 🔑 text allignment and loop
n, m = map(int, input().split(' '))
n = int(input())
m = int(input())
pattern = ".|."
filler = "-"
for i in range(int(n/2)):
    print((pattern * i).rjust(int(m/2)-1, filler) +
        pattern + (pattern*i).ljust(int(m/2)-1, filler))

for i in range(int(n/2), int(n/2)+1):
    print(("welcome").center(m, filler))

for i in range(int(n/2)-1, -1, -1):
    print((pattern * i).rjust(int(m/2)-1, filler) +
        pattern + (pattern*i).ljust(int(m/2)-1, filler))


n, m = map(int, input().split(' '))
pattern = ".|."
filler = "-"
lngth = int(input())
# top part
for i in range(1, lngth):
    print(('.|.'*(2*i - 1)).center(m, '-'))

# middle part
print('WELCOME'.center(m, '-'))

# bottom part
for i in range(1, lngth):
    print(('.|.'*(2*(lngth - i) - 1)).center(m, '-'))


"""
Find() Method: -  The .find() method is a built-in string method in Python that is used to find the first occurrence of a substring within a string. It returns the index of the first occurrence of the substring, or -1 if the substring is not found.
The syntax for using the .find() method is as follows:
    *string.find(substring, start, end)
Here's what each parameter represents:
* string: This is the string in which you want to search for the substring.
* substring: This is the substring you want to find within the string.
* start (optional): This parameter specifies the starting index of the search. The .find() method will start searching from this index. If not provided, the search will begin from the beginning of the string (index 0).
* end (optional): This parameter specifies the ending index of the search. The .find() method will search for the substring up to, but not including, this index. If not provided, the search will continue until the end of the string.


Example : 
string = "Hello, world!"
substring = "world"

index = string.find(substring)
print(index)  # Output: 7
"""


#########################################################################
################################ Question #*String Formatting
# 🔑: The general form of a standard format specifier is:
"""
format_spec     ::=  [[fill]align][sign]["z"]["#"]["0"][width][grouping_option]["." precision][type]
fill            ::=  <any character>
align           ::=  "<" | ">" | "=" | "^"
sign            ::=  "+" | "-" | " "
width           ::=  digit+
grouping_option ::=  "_" | ","
precision       ::=  digit+
type            ::=  "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g" | "G" | "n" | "o" | "s" | "x" | "X" | "%"
"""

"""
*Accessing arguments by position:

'{0}, {1}, {2}'.format('a', 'b', 'c')

'{}, {}, {}'.format('a', 'b', 'c')  # 3.1+ only

'{2}, {1}, {0}'.format('a', 'b', 'c')

'{2}, {1}, {0}'.format(*'abc')      # unpacking argument sequence

'{0}{1}{0}'.format('abra', 'cad')   # arguments' indices can be repeated
"""
"""
*Accessing arguments by name:
'Coordinates: {latitude}, {longitude}'.format(latitude='37.24N', longitude='-115.81W')

coord = {'latitude': '37.24N', 'longitude': '-115.81W'}
'Coordinates: {latitude}, {longitude}'.format(**coord)
"""

"""
*Accessing arguments’ attributes:
c = 3-5j
('The complex number {0} is formed from the real part {0.real} '
'and the imaginary part {0.imag}.').format(c)

class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __str__(self):
        return 'Point({self.x}, {self.y})'.format(self=self)

str(Point(4, 2))
"""

"""
*Aligning the text and specifying a width:
'{:<30}'.format('left aligned')

'{:>30}'.format('right aligned')

'{:^30}'.format('centered')

'{:*^30}'.format('centered')  # use '*' as a fill char
"""
# OR
text = 'o'
width = 5
formatted_text = f"{text:>{width}}"
print(formatted_text)  # output:    o

text = 'o'
width = 5
formatted_text = f"{text:>{width}}"
formatted = f"{'*':>{15}}"
print(formatted_text)
print(formatted)
# >>>    o
# >>>              *

# * QAnswer
# method 1
def print_formatted(number):
    # your code goes here
    space = len(bin(number)[2:])
    for i in range(1, number+1):
        decimal = str(i).rjust(space)
        octal = oct(i)[2:].rjust(space)
        hexadecimal = hex(i)[2:].rjust(space).upper()
        binary = bin(i)[2:].rjust(space)
        print(f"{decimal} {octal} {hexadecimal} {binary}")

# method 2 as of concept metnioned above
    for n in range(1, number+1):
        print(f"{n:>{space}d} {n:>{space}o} {n:>{space}x} {n:>{space}b}".upper())

# method 3
    for i in range(1, number + 1):
        print(str(i).rjust(space, ' '), oct(i)[2:].rjust(space, ' '), hex(
            i)[2:].rjust(space, ' ').upper(), bin(i)[2:].rjust(space, ' '))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

# *
word, length = input().split()
"""
input() function is used to read a line of input from the user.
.split() method is called on the input string, which splits the string into a list of substrings
using whitespace as the delimiter.
The resulting list is unpacked into two variables: word and length.
The first element of the list is assigned to word.
The second element of the list is assigned to length.
If there are more than two elements in the list, an error will occur.

* If the input has a different format or number of values, it may lead to errors. Therefore,
*it's a good practice to include proper input validation and error handling to handle such scenarios.
"""

s, k = input().split()
l = sorted(list(permutations(s, int(k))))
for i in l:
    print("".join(i))

s = "ramj"
l = permutations(s, 2)
print(tuple(l))


##################################################################
############################# Question #*Capitalize!
# 🔑 capitalize() method and join()
# 1st method
# Complete the solve function below.


def solve(s):
    cap_word = s.split(" ")
    cap = []
    for i in cap_word:
        cap.append(i.capitalize())
    return ' '.join(cap)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = solve(s)
    fptr.write(result + '\n')
    fptr.close()

# 2nd method By Using list comprehension, capitalize() and join() method
def solve(s):
    cap = [word.capitalize() for word in s.split(' ')]
    return ' '.join(cap)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = solve(s)
    fptr.write(result + '\n')
    fptr.close()


# Note here, you cannot use my_string.isintances directly because isintances is not a valid attribute
# or method of a string object in Python. The correct method to check the type of an object is isinstance().
# Here's the corrected code


# 3rd method By replacing list
# * Note:- split() method in Python returns a list, It splits a string into substrings based on a specified delimiter and returns a list of these substrings.
# *                 You can specified delimeter like whitespace, *, and comma etc...
#  Example
s = "Hello, World!"
result = s.split("!")
print(result)  # >>> output ['Hello, World', '']

s = "Hello, World!"
result = s.split(",")
print(result)  # >>> output ['Hello', ' World!']

# 3rd method By using replacing method
def solve(s):
    for name in s.split():
        s = s.replace(name, name.capitalize())
    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = solve(s)
    fptr.write(result + '\n')
    fptr.close()
""" 
* replace() method is a built-in string method that is used to create a new string by replacing all occurrences of a specified substring with another substring.
    #*Syntax new_string = original_string.replace(old_substring, new_substring, count)
* original_string: This is the original string on which you want to perform the replacement operation.
* old_substring: This is the substring that you want to replace within the original string.
* new_substring: This is the substring that will replace each occurrence of the old substring in the original string.
* count (optional): This parameter specifies the maximum number of replacements to be made. If provided,
* -- only the first count occurrences of the old substring will be replaced. By default, all occurrences are replaced.


replace() method is a string method and does not work directly with lists
It is specifically designed to replace substrings within a string.
For perform replacement operations on a list,we can use list comprehension
or other list manipulation methods to achieve the desired result.
"""
# Note: -The replace() method returns a new string with the specified replacements.The original string remains unchanged.

original_list = ['apple', 'banana', 'cherry']
replaced_list = [fruit.replace('a', 'X') for fruit in original_list]
print(replaced_list)  # ['Xpple', 'bXnXnX', 'cherry']

# 4th method By using isintances() and append method
# isintances() method:- often used in Python for type checking, object introspection, and conditional logic based on the type of an object.
'''
The syntax for the isinstance() function
#* isinstance(object, classinfo)
object: The object that you want to check.
classinfo: A class or a tuple of classes against which the object's type will be checked.
'''
def solve(s):
    slist = s.split(" ")
    cap_list = []
    for name in slist:
        if isinstance(name, str):
            cap_list.append(name.capitalize())
        else:
            cap_list.append(name)
    return " ".join(str(x) for x in cap_list)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = solve(s)
    fptr.write(result + '\n')
    fptr.close()

##################################################################
######################### # Question #* Alphabet Rangoli
"""
#* Slicing concept :-
The :: syntax in list slicing is used for specifying the step or stride of the slice. It has the form (start:stop:step)
#where: -
start is the starting index of the slice (inclusive),
stop is the ending index of the slice (exclusive), and
step is the step or stride between elements. 

"""
# Let's take a look at example to be clear 
#* 1.Basic Slicing:
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Get every element with a step of 2
result = numbers[::2]
print(result)  # Output: [0, 2, 4, 6, 8]

#* 2.Negative Step - Reversing a List:
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Reverse the list
result = numbers[::-1]
print(result)  # Output: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]


#* 3.Negative Start and Stop:
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Start from the second-to-last element and go backward with a step of 2
result = numbers[-2::-2]
print(result)  # Output: [8, 6, 4, 2, 0]

#* 4.Negative Start and Stop: 
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
result = numbers[-2::2]
print(result) # Output: [8]

#* 5.Positive Start and Stop:
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
result = numbers[2::-2]
print(result) # Output: [2, 0]


#* 6.Negative Start, Stop, and Step:
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Start from the second-to-last element, go backward with a step of 3, and stop at the third element
result = numbers[-2:2:-3]
print(result)  # Output: [8, 5]



"""
pattern[-2::-1]  index -2 -> second-to-last element in the list('c').
[::-1] -> a step of -1, meaning the list is reversed.

So [-2::-1] means start from the second-to-last element ('c') and move backward with a step of -1reversing the list from that point.
The result is a new list ['c', 'd', 'e'].
"""
#break down
pattern = ['e']
print(pattern[-2::-1]) # Output: []

pattern = ['e','d']
print(pattern[-2::-1]) # Output: ['e']

pattern = ['e','d','c']
print(pattern[-2::-1]) # Output: ['d', 'e']

pattern = ['e','d','c','b']
print(pattern[-2::-1]) # ['c', 'd', 'e']

pattern = ['e','d','c','b','a']
print(pattern[-2::-1]) # ['b', 'c', 'd', 'e']

pattern = ['e','d','c','b','a']
print('-'.join(pattern)) # e-d-c-b-a

alpha = 'abcdefghijklmnopqrstuvwxyz'
def print_rangoli(size):
    string = alpha[:size]
    pattern = []
    width = size * 4 - 3
    height = string[::-1]
    
    for letter in height:
        pattern.append(letter)
        print('-'.join(pattern + pattern[-2::-1]).center(width, '-')) 
    
    for element in range(len(pattern) - 1):
        pattern.pop()
        print('-'.join(pattern + pattern[-2::-1]).center(width, '-'))


# 2nd method
import string
def print_rangoli(size):
    alpha = string.ascii_lowercase
    width = 4 * size - 3
    length = 2 * size - 1
    
    for i in range(length):
        right_half = alpha[abs(size-1-i)+1:size]
        concatenated = right_half[::-1] + alpha[abs(size-1-i)] + right_half
        print("-".join(concatenated).center(width, "-"))

# 3rd method
def print_rangoli(size):
    import string
    alphabet = string.ascii_lowercase
    
    width = size*2-1 + (size-1) * 2
    
    for i in range(1-size, size):
        sublist = list(alphabet[abs(i):size])
        prelist = list(reversed(sublist[1:]))
        wholelist = prelist + sublist
        print('-'.join(wholelist).center(width, '-'))
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
    
# 4th method
def print_rangoli(size):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    dash = '-'
    
    width = size * 2 - 1 + (size - 1) * 2
    for i in range(-size + 1, size):
        d = abs(i)
        sublist = list(alphabet\[d:size\])
        prelist = list(reversed(sublist\[1:\])
        wholelist = prelist + sublist
        print(dash.join(wholelist).center(width, dash))
        
# 5th method
def print_rangoli(size):
    result = []
    for i in range(size):
        sub = [chr(96+size-j) for j in range(i+1)]
        result.append("-".join(sub + sub[::-1][1:]).center(size*4-3,"-"))
    print("\n".join(result + result[::-1][1:]))
    
# 6th method
import itertools
import string
def print_rangoli(size):
    a = string.ascii_lowercase
    i = size -1
    while i > -size:
        p = ['-' for _ in range(abs(i))]
        print("-".join(itertools.chain(p, a[size-1 : abs(i): -1], a[abs(i): size], p)))
        i -= 1

# 7th method
def rangoli(size):
    E=list()
    S="abcdefghijklmnopqrstuvwxyz"
    for i in range(0,size):
        S1=S[0:size]
        S2=S1[::-1]
        A=[S2[j] for j in range(size-i)]
        B=("-").join(A+A[::-1][1:])
        E.append(B.center(4*size-3,"-"))
print("\n".join(E[::-1]+E[1:]))


# 8th method
alphabet = 'abcdefghijklmnopqrstuvwxyz'
l=alphabet[:n]
l1=[]
for i in range(n):
    x="-".join(l[::-1][:i+1])
    y=((n-i)*2-2)*"-"
    l1.append(y+x+x[::-1][1:]+y)
k=l1[:n-1]
print(*l1,*k[::-1],sep="\n")

# 9th method
def print_rangoli(size):
    # your code goes here
    import string
    l = string.ascii_lowercase[:n]
    o = []
    for i in range(n):
        o.append('-'.join(l[::-1][:i+1] + l[n-i:]).center((4*n-3), '-'))
    print(*o, *o[::-1][1:], sep = '\n')
    
# 10th day
def print_rangoli(size):
    width = 4 * size - 3
    alpha = string.ascii_lowercase
    for i in list(range(size))[::-1] + list(range(1, size)):
        print('-'.join(alpha[size-1:i:-1] + alpha[i:size]).center(width, '-'))
        
# from __future__ import print_function

def print_rangoli(size):
    # The whole alphabet.
    alpha = "abcdefghijklmnopqrstuvwxyz"
    # The subset on which we are operating.
    subset = alpha[:size]
    
    # The base string, will be something like "e-d-c-b-a"
    # It will go in the middle, every row will be made from that base
    # string, and also be mirrored.
    base = "-".join(reversed(subset))
    rows = []
    # Generate the top-left square like this:
    '''--------e
       ------e-d
       ----e-d-c
       --e-d-c-b
       e-d-c-b-a'''
    for i in range(size):
        # Generate each row by removing trailing chars from the base string.
        row = base[:len(base) - i*2]
        # Pad that row to match length of the base string
        row = ("-" * (len(base) - len(row))) + row
        rows.insert(0, row)
    # Now that upper left corner is generated, mirror it downwards like this,
    # without adding again the base string:
    '''--------e
       ------e-d
       ----e-d-c
       --e-d-c-b
       e-d-c-b-a
       --e-d-c-b
       ----e-d-c
       ------e-d
       --------e'''
    rows.extend(reversed(rows[:-1]))
    # Now that the left half is generated, mirror each row to the right.
    for i in range(len(rows)):
        row = rows[i]
        # Reverse the row.
        rev_row = row[::-1]
        # Append the reversed row without the initial character.
        rows[i] = row + rev_row[1:] 
    '''--------e--------
       ------e-d-e------
       ----e-d-c-d-e----
       --e-d-c-b-c-d-e--
       e-d-c-b-a-b-c-d-e
       --e-d-c-b-c-d-e--
       ----e-d-c-d-e----
       ------e-d-e------
       --------e--------'''
    # The result is ready to be printed.  
    print(*rows, sep="\n")
    
# without comment
from __future__ import print_function

def print_rangoli(size):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    subset = alpha[:size]
    base = "-".join(reversed(subset))
    rows = []
    for i in range(size):
        row = base[:len(base) - i*2]
        row = ("-" * (len(base) - len(row))) + row
        rows.insert(0, row)
    rows.extend(reversed(rows[:-1]))
    for i in range(len(rows)):
        row = rows[i]
        rev_row = row[::-1]
        rows[i] = row + rev_row[1:] 
    print(*rows, sep="\n")

# 
def print_rangoli(size):

    alphabet = ' abcdefghijklmnopqrstuvwxyz'

    for i in range(size,0,-1):
        c = alphabet[size:i:-1] + alphabet[i:size+1]
        c = '-'.join(c)
        print(c.center((size*4)-3,'-'))

    for i in range(0,size-1):
        c = alphabet[size:i+2:-1] + alphabet[i+2:size+1]
        c ='-'.join(c)
        print(c.center((size*4)-3,'-'))
        
        
# 
import string
    a = string.ascii_lowercase
    L = []
    for i in range(size):
        s = "-".join(a[i:size])
        L.append((s[::-1]+s[1:]).center(4*size-3, "-"))
    print('\n'.join(L[:0:-1]+L))
##################################################################
######################### # Question #* The Minion Game
import string
# Get all uppercase letters from the alphabet
uppercase_letters = string.ascii_uppercase
print(uppercase_letters) #Output : ABCDEFGHIJKLMNOPQRSTUVWXYZ

import string
# Get all uppercase letters from the alphabet
uppercase_letters = string.ascii_uppercase
print(type(uppercase_letters)) #Output : <class 'str'>


def minion_game(string):
    # your code goes here
    vowels = {'A', 'E', 'I', 'O', 'U'}
    count_vowels = 0
    count_consonants = 0
    n = len(string)
    for i in range(n):
        if set(string[i]).issubset(vowels):
            count_vowels+=n-i
        else:
            count_consonants +=n-i
    
    if count_consonants > count_vowels:
        print('Stuart', count_consonants)
    elif count_consonants < count_vowels:
        print('Kevin', count_vowels)
    else:
        print('Draw')
        
# 2nd method
def minion_game(string):
    stuart, kevin = 0,0
    vokal=('A','I','U','E', 'O')

for idx,val in enumerate(string):
    k=len(string)-idx
    if val in vokal:
        kevin+=k
    else:
        stuart+=k
if kevin == stuart:
    print('Draw')
else:
    print('Kevin', kevin) if kevin > stuart else print('Stuart', stuart)
if name == 'main': s = input() minion_game(s)

# 3rd method
def minion_game(string):
    # your code goes here
    vowels = ('A', 'E', 'I', 'O', 'U')
    stuart, kevin = 0, 0
    size = len(string)
    
    for i in range(0, size):
        k = size - i
        if string[i].upper().startswith(vowels):
            kevin += k
        else:
            stuart += k
    
    if kevin == stuart:
        print('Draw')
    else:
        print('Kevin', kevin) if kevin > stuart else print('Stuart', stuart)




##################################################################
######################## # Question #* Merge Tools

# 1st method
def merge_the_tools(string, k):
    # your code goes here
    num_part = len(string)//k
    my_list = []
    for _ in range(num_part):
        my_string = string[:k]
        my_list.append(my_string)
        # string  = string.replace(my_string, '') mistake i'va done
        string  = string[k:]
    for k in (my_list):
        print(''.join(str(j) for j in set(k)), sep = '\n')
        
        
# 2nd method by initializing a new string and using membership operater  to assign 
def merge_the_tools(string, k):
    num_part = len(string) // k
    my_list = []

    for _ in range(num_part):
        my_string = string[:k]
        my_list.append(my_string)
        string = string[k:]

    for substring in my_list:
        unique_chars = ''
        for char in substring:
            if char not in unique_chars:
                unique_chars += char
        print(unique_chars)
        
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)


# 3rd method
from collections import OrderedDict
def merge_the_tools(string, k):
    num_part = len(string) // k
    my_list = []

    for _ in range(num_part):
        my_string = string[:k]
        my_list.append(my_string)
        string = string[k:]

    for substring in my_list:
        unique_chars = ''.join(OrderedDict.fromkeys(substring))
        print(unique_chars)
        
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

# 4th method more compact way
def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        print(''.join(dict.fromkeys(string[i:i + k])))
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

# 5th method using textrap module
import textwrap
def merge_the_tools(string, k):
    substr_lst = textwrap.wrap(string, k)

    for sub in substr_lst:
        print("".join(dict.fromkeys(sub)))





####################################################################
############################################################ (Sets)
####################################################################

#######################################################################
################################### Question #*Introduction to Sets
# 🔑 set
"""
*set:- A set is an unordered collection of elements without duplicate entries.When printed,
*        iterated or converted into a sequence, its elements will appear in an arbitrary order.
"""
print(set())
# >>> set([])

print(set('HackerRank'))
# >>> set(['a', 'c', 'e', 'H', 'k', 'n', 'r', 'R'])

print(set([1, 2, 1, 2, 3, 4, 5, 6, 0, 9, 12, 22, 3]))
# >>> set([0, 1, 2, 3, 4, 5, 6, 9, 12, 22])

print(set((1, 2, 3, 4, 5, 5)))
# >>> set([1, 2, 3, 4, 5])

print(set(set(['H', 'a', 'c', 'k', 'e', 'r', 'r', 'a', 'n', 'k'])))
# >>> set(['a', 'c', 'r', 'e', 'H', 'k', 'n'])

print(set({'Hacker': 'DOSHI', 'Rank': 616}))
# >>> set(['Hacker', 'Rank'])

print(set(enumerate(['H', 'a', 'c', 'k', 'e', 'r', 'r', 'a', 'n', 'k'])))
# >>> set([(6, 'r'), (7, 'a'), (3, 'k'), (4, 'e'), (5, 'r'), (9, 'k'), (2, 'c'), (0, 'H'), (1, 'a'), (8, 'n')])

# * Question answer
# 1st method
def average(array):
    my_array = set(array)
    total_num = len(my_array)
    sum = 0
    for i in my_array:
        sum = i + sum
    return sum/total_num

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

# 2nd method direct using sum function
def average(array):
    my_array = set(array)
    total_num = len(my_array)
    # * Or also sum_values = sum(i for i in my_array)
    sum_values = sum(my_array)
    return sum_values / total_num

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

# 3rd method by using lambda functions
def average(array): return sum(set(array)) / len(set(array))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)


##################################################################
############### # Question #*Set Symmetric Difference
# 🔑
N = int(input())
set(map(int, input().split()))
print(N)  # enter input 1,2 gives 1

N = set(map(int, input().split()))
int(input())
print(N)  # enter input 1,2 return {1}
# >>> 1
# >>> 1 23 34
#    1
# >>> 23 45 23
# >>> 2
#   {45, 23}

"""
Using a semicolon allows you to write multiple statements on the same line. In this case,
it assigns the value returned by int(input()) to the variable N and then creates a set
using set(map(int, input().split())).
"""
m, M = int(input()), set(map(int, input().split()))
n, N = int(input()), set(map(int, input().split()))

# zip function :-
"""when using zip() function  make sureinput sequences you provide have the same length.
otherwise zip reaches the end of the shortest input sequence by truncate """

list1 = [1, 2, 3]
list2 = [4, 5, 6, 7, 8]
for pair in zip(list1, list2):
    for x in pair:
        print(x)
result = [x for pair in zip(list1, list2) for x in pair]
print(result)
# >>> 1
# >>> 4
# >>> 2
# >>> 5
# >>> 3
# >>> 6
# >>> [1, 4, 2, 5, 3, 6]


####################################################################
######################################## # *Question Set .add()
N = int(input())
stamps = list(map(lambda _: input(), range(N)))
set_ = set()
for i in range(N):
    set_.add(stamps[i])
print(len(set_))


#####################################################################
###################### # *Question Set .discard(), .remove() & .pop()
# 1st method
n = int(input())
s = set(map(int, input().split()))
n_commands = int(input())

for i in range(n_commands):
    command_task, *args = input().split()
    if command_task == "remove":
        s.remove(int(args[0]))
    elif command_task == "pop":
        s.pop()
    elif command_task == "discard":
        s.discard(int(args[0]))
print(sum(s))


# 2nd method
n = int(input())
s = set(map(int, input().split()))
n_commands = int(input())
for i in range(n_commands):
    command_name = input().split()
    if command_name[0] == "remove":
        s.remove(int(command_name[1]))
    elif command_name[0] == "discard":
        s.discard(int(command_name[1]))
    elif command_name[0] == "pop":
        s.pop()
print(sum(s))


# 3rd method
n = int(input())
s = set(map(int, input().split()))
n_commands = int(input())

command_dict = {
    "remove": s.remove,
    "pop": s.pop,
    "discard": s.discard
}
for i in range(n_commands):
    command_task = input().split()
    removing_number = int(command_task[1])
    command_func = command_dict.get(command_task[0])
    if command_func:
        command_func(removing_number)
print(sum(s))


# 4th method
n = int(input())
s = set(map(int, input().split()))
n_commands = int(input())
command_dict = {
    "remove": lambda x: s.remove(x),
    "discard": lambda x: s.discard(x),
    "pop": lambda: s.pop()
}

for i in range(n_commands):
    command_name, *args = input().split()
    command_func = command_dict.get(command_name)
    if command_func:
        if args:
            command_func(int(args[0]))
        else:
            command_func()
print(sum(s))


#####################################################################
########################## # *Question Set .union() Operation
# .union()

"""
#* The .union() operator returns the union of a set and the set of elements in an iterable.
#* Sometimes, the "|" operator is used in place of .union() operator, but it operates only on the set of elements in set.
#* Set is immutable to the .union() operation (or | operation).
"""
# example
s = set("Hacker")
print(s.union("Rank"))
# output: set(['a', 'R', 'c', 'r', 'e', 'H', 'k', 'n'])

print(s.union(set(['R', 'a', 'n', 'k'])))
# output: set(['a', 'R', 'c', 'r', 'e', 'H', 'k', 'n'])

print(s.union(['R', 'a', 'n', 'k']))
# Output: set(['a', 'R', 'c', 'r', 'e', 'H', 'k', 'n'])

print(s.union(enumerate(['R', 'a', 'n', 'k'])))
# Output: set(['a', 'c', 'r', 'e', (1, 'a'), (2, 'n'), 'H', 'k', (3, 'k'), (0, 'R')])

print(s.union({"Rank": 1}))
# Output: set(['a', 'c', 'r', 'e', 'H', 'k', 'Rank'])

print(s | set("Rank"))
# Output: set(['a', 'R', 'c', 'r', 'e', 'H', 'k', 'n'])

# 1st method
# Enter your code here. Read input from STDIN. Print output to STDOUT
eng_subs = int(input())
roll_num_eng = set(map(int, input().split()))
french_subs = int(input())
roll_num_french = set(map(int, input().split()))
subs = roll_num_eng.union(roll_num_french)
print(len(subs))


########################################################################
########################### #Question #* Set .intersection() Operation
# *The .intersection()
"""
#* The .intersection() Operator returns the intersection of a set and the set of elements in an iterable.
#* Sometimes, the & operator is used in place of the .intersection() operator, but it only operates on the set of elements in set.
#* The set is immutable to the .intersection() operation (or & operation). """
# Example
s = set("Hacker")
print(s.intersection("Rank"))
# Output: set(['a', 'k'])

print(s.intersection(set(['R', 'a', 'n', 'k'])))
# Output: set(['a', 'k'])

print(s.intersection(['R', 'a', 'n', 'k']))
set(['a', 'k'])

print(s.intersection(enumerate(['R', 'a', 'n', 'k'])))
# Output: set([])

print(s.intersection({"Rank": 1}))
# Output: set([])

print(s & set("Rank"))
# Output: set(['a', 'k'])

# Solution
num_of_french_subs = int(input())
frnech_subs = set(map(int, input().split()))
num_of_eng_subs = int(input())
eng_subs = set(map(int, input().split()))
subs = frnech_subs.intersection(eng_subs)
print(len(subs))


#####################################################################
########################### #Question #*Set .diffrence() Operation
# *.difference()
"""
The tool .difference() returns a set with all the elements from the set that are not in an iterable.
Sometimes the - operator is used in place of the .difference() tool, but it only operates on the set of elements in set.
Set is immutable to the .difference() operation (or the - operation).
"""
s = set("Hacker")
print(s.difference("Rank"))
# Output: set(['c', 'r', 'e', 'H'])

print(s.difference(set(['R', 'a', 'n', 'k'])))
# Output: set(['c', 'r', 'e', 'H'])

print(s.difference(['R', 'a', 'n', 'k']))
# Output: set(['c', 'r', 'e', 'H'])

print(s.difference(enumerate(['R', 'a', 'n', 'k'])))
# Output: set(['a', 'c', 'r', 'e', 'H', 'k'])

print(s.difference({"Rank": 1}))
# Output: set(['a', 'c', 'e', 'H', 'k', 'r'])

print(s - set("Rank"))
# Output: set(['H', 'c', 'r', 'e'])


# Solution
if __name__ == "__main__":
    n, english_students = int(input()), set(map(int, input().split()))
    m, french_students = int(input()), set(map(int, input().split()))
    print(len(english_students - french_students))


###############################################################################
########################### #*Question Set .symmetric_diffrence() Operation
# * .symmetric_difference()
"""
#* The .symmetric_difference() operator returns a set with all the elements that are in the set and the iterable but not both.
#* Sometimes, a ^ operator is used in place of the .symmetric_difference() tool, but it only operates on the set of elements in set.
#* The set is immutable to the .symmetric_difference() operation (or ^ operation).
"""
s = set("Hacker")
print(s.symmetric_difference("Rank"))
# Output: set(['c', 'e', 'H', 'n', 'R', 'r'])

print(s.symmetric_difference(set(['R', 'a', 'n', 'k'])))
# Output: set(['c', 'e', 'H', 'n', 'R', 'r'])

print(s.symmetric_difference(['R', 'a', 'n', 'k']))
# Output: set(['c', 'e', 'H', 'n', 'R', 'r'])

print(s.symmetric_difference(enumerate(['R', 'a', 'n', 'k'])))
# Output: set(['a', 'c', 'e', 'H', (0, 'R'), 'r', (2, 'n'), 'k', (1, 'a'), (3, 'k')])

print(s.symmetric_difference({"Rank": 1}))
# Output: set(['a', 'c', 'e', 'H', 'k', 'Rank', 'r'])

print(s ^ set("Rank"))
# Output: set(['c', 'e', 'H', 'n', 'R', 'r'])


######################################################################
############################## #*Questions (Set Mutations)
# Key concept (.update() or |= , .intersection_update() or &= , .difference_update() or -= , .symmetric_difference_update() or ^=)
# * .update() or |=
# Update the set by adding elements from an iterable/another set.
H = set("Hacker")
R = set("Rank")
H.update(R)
print(H)
# >>>set(['a', 'c', 'e', 'H', 'k', 'n', 'r', 'R'])


# * .intersection_update() or &=
# Update the set by keeping only the elements found in it and an iterable/another set.
H = set("Hacker")
R = set("Rank")
H.intersection_update(R)
print(H)
# >>>set(['a', 'k'])

# * .difference_update() or -=
# Update the set by removing elements found in an iterable/another set.
H = set("Hacker")
R = set("Rank")
H.difference_update(R)
print(H)
set(['c', 'e', 'H', 'r'])


# * .symmetric_difference_update() or ^=
# Update the set by only keeping the elements found in either set, but not in both.
H = set("Hacker")
R = set("Rank")
H.symmetric_difference_update(R)
print(H)
set(['c', 'e', 'H', 'n', 'r', 'R'])


# getatrr() method
"""
    built-in function that allows you to retrieve an attribute or method from an object dynamically.
    Its syntax is getattr(object, attribute[, default]),
    where: object is the object from which you want to retrieve the attribute or method.
        attribute is a string representing the name of the attribute or method you want to access.
"""

# Example
class MyClass:
    def greet(self):
        print("Hello!")
obj = MyClass()
# Calling the greet() method using getattr()
method_name = "greet"
method = getattr(obj, method_name)
method()  # Output:Hello!


# Example
lst = set()
# Adding elements to the set
lst.add(10)
lst.add(20)
lst.add(30)
print("Initial Set:", lst)  # Output:Initial Set: {10, 20, 30}

# Performing operations on the set based on user input
operation = input("Enter the operation (add/remove): ")
values = map(int, input("Enter values to modify the set: ").split())

getattr(lst, operation)(values)
print("Modified Set:", lst)

"""
run example
Enter the operation (add/remove): add
Enter values to modify the set: 40 50 60
Initial Set: {10, 20, 30}
Modified Set: {40, 10, 50, 20, 60, 30}
"""

# Question Answers
# The getattr() function is commonly used when you don't know the name of the attribute
#    -or method at the time of writing the code, but it is determined dynamically at runtime.
# 1st method
n = int(input())
lst = set(map(int, input().split()))
t = int(input())
for _ in range(t):
    a, b = input().split()
    b_lst = map(int, input().split())
    getattr(lst, a)(b_lst)
print(sum(lst))


# 2nd method
m = int(input().strip())
A = set(map(int, input().split()))
N = int(input())
for _ in range(N):
    cmd, n = input().split()
    lis = set(map(int, input().split()))
    s = f"A.{cmd}({lis})"
    eval(s)
print(sum(A))

"""
eval() is a built-in Python function that allows you to evaluate and execute a string containing
a Python expression or command. It takes a string as an argument and interprets it as code.
The evaluated code is then executed, and the result of the expression or command is returned.

"""
# 3rd method
n = int(input())
lst = set(map(int, input().split()))
t = int(input())
for _ in range(t):
    command, *arg = input().split()
    b_lst = set(map(int, input().split()))
    if command == "update":
        lst.update(b_lst)
    elif command == "difference_update":
        lst.difference_update(b_lst)
    elif command == "intersection_update":
        lst.intersection_update(b_lst)
    elif command == "symmetric_difference_update":
        # Note do not assign to a set bcz
        lst.symmetric_difference_update(b_lst)
        # The method symmetric_difference_update() doesn't return a set; instead,
        # it updates the existing set in-place. Therefore, there's no need to assign
        # the result back to lst in that case.
print(sum(lst))


##################################################################
##################### Question #*  Sets The Captain's Room
# Counting repeatative items in lis or dic
# function within collections module
from collections import deque, ChainMap, Counter, defaultdict, namedtuple,  OrderedDict, UserDict, UserList, UserString, 
collections_module = [namedtuple, deque, ChainMap, Counter, defaultdict, OrderedDict, UserDict, UserList, UserString]

# But most frequent used most_frequent_function = [Counter, defaultdict, namedtuple, deque, OrderedDict]
"""
The collections module in Python provides several useful functions and classes for data manipulation. Here are some of the most frequently used functions from the collections module:
#* Counter: Used for counting occurrences of elements in a collection.
#* defaultdict: Creates dictionaries with default values for nonexistent keys.
#* namedtuple: Creates simple classes (tuples) with named fields.
#* deque: Provides a double-ended queue with efficient append and pop operations from both ends.
#* OrderedDict: A dictionary that remembers the order of keys based on their insertion.
#* ChainMap: Allows combining multiple dictionaries or mappings into a single view.
#* UserDict: A dictionary-like class that allows easier subclassing for custom dictionaries.
#* UserList: A list-like class that allows easier subclassing for custom lists.
#* UserString: A string-like class that allows easier subclassing for custom strings.
"""
"""
collections:-
#* It is designed to extend the capabilities of the built-in data structures like dictionaries, lists, and tuples.
#* collections is used for tasks such as counting occurrences, creating dictionaries with default values, and managing ordered collections.
#* Common use cases of collections include counting elements with Counter, creating dictionaries with default values using defaultdict, and maintaining ordered dictionaries using OrderedDict.

itertools:- 
#* It focuses on creating and manipulating iterators and provides functions to generate and combine them in various ways.
#* itertools is used for tasks related to iteration, combination, and permutation of elements in an efficient manner.
#* Common use cases of itertools include generating infinite sequences, creating combinations and permutations of elements, and efficient data processing.

"""
itertool_function = [Counter,defaultdict,namedtuple,deque,OrderedDict,ChainMap,UserDict,UserList,UserString]
from collections import Counter
# 1st method
N = int(input())
li = input().split()
num_count = Counter(li)
print(num_count)
for n, c in num_count.items():
    if c == 1:
        print(n)


# 2nd methods
N = int(input())
li = input().split()
count = {}
for i in li:
    count[i] = count.get(i, 0) + 1
for k, v in count.items():
    if v != N:
        print(k)


#####################################################################
########################## # *Questions (Check Subset)
# 1st method by using .issubset() method
num_of_testcase = int(input())

for _ in range(num_of_testcase):
    num_of_element_seta = int(input())
    # Convert input elements to a set
    value_of_element_seta = set(input().split())
    num_of_element_setb = int(input())
    # Convert input elements to a set
    value_of_element_setb = set(input().split())

    # Check if setA is a subset of setB
    is_subset = value_of_element_seta.issubset(value_of_element_setb)
    print(is_subset)

# 2nd method using for loop
num_of_testcase = int(input())
for _ in range(num_of_testcase):
    num_of_element_seta = int(input())
    value_of_element_seta = input().split()
    num_of_element_setb = int(input())
    value_of_element_setb = input().split()
    Testcase = True
    for element in value_of_element_seta:
        if element not in value_of_element_setb:
            Testcase = False
            break
    print(Testcase)

# Or
num_of_testcase = int(input())

for _ in range(num_of_testcase):
    num_of_element_seta = int(input())
    value_of_element_seta = input().split()
    num_of_element_setb = int(input())
    value_of_element_setb = input().split()
    Testcase = False  # Initialize Testcase as False
    for element in value_of_element_seta:
        if element not in value_of_element_setb:
            break
    else:
        Testcase = True  # If all elements are found, assign Testcase as True
    print(Testcase)


# 3rd method using all method
num_of_testcase = int(input())
for _ in range(num_of_testcase):
    num_of_element_seta = int(input())
    value_of_element_seta = input().split()
    num_of_element_setb = int(input())
    value_of_element_setb = input().split()

    # Checking if setA is a subset of setB using all() function
    is_subset = all(element in value_of_element_setb for element in value_of_element_seta)
    print(is_subset)

# 4th method using set operator
num_of_testcase = int(input())

for _ in range(num_of_testcase):
    num_of_element_seta = int(input())
    value_of_element_seta = set(input().split())
    num_of_element_setb = int(input())
    value_of_element_setb = set(input().split())
    # Checking me if setA is a subset of setB using set operations
    is_subset = value_of_element_seta <= value_of_element_setb
    print(is_subset)

# 5th way using list comprehension
num_of_testcase = int(input())
for _ in range(num_of_testcase):
    num_of_element_seta = int(input())
    value_of_element_seta = input().split()
    num_of_element_setb = int(input())
    value_of_element_setb = input().split()

    is_subset = len([element for element in value_of_element_seta if element not in value_of_element_setb]) == 0
# Or also this  is_subset = len(value_of_element_seta - value_of_element_setb) == 0
# Or also is_subset = len(value_of_element_seta.intersection(value_of_element_setb)) == len(value_of_element_seta)
# Or also is_subset = (value_of_element_seta - value_of_element_setb) == set()
# Or also is_subset = value_of_element_seta.issubset(value_of_element_setb)
    print(is_subset)

# 6th method by defining a function
def is_subset(set_a, set_b):
    for element in set_a:
        if element not in set_b:
            return False
    return True

num_of_testcase = int(input())
for _ in range(num_of_testcase):
    num_of_element_seta = int(input())
    value_of_element_seta = set(input().split())
    num_of_element_setb = int(input())
    value_of_element_setb = set(input().split())

    # Check if setA is a subset of setB using the custom is_subset() function
    is_subset_result = is_subset(value_of_element_seta, value_of_element_setb)
    print(is_subset_result)


###############################################################
######################## # *Questions (Check Strict Superset)
set_a = set(input().split())
num_of_set = int(input())
is_superset = True
for _ in range(num_of_set):
    custom_set = set(input().split())
    if not set_a.issuperset(custom_set):
        is_superset = False
        break
print(is_superset)


# 2nd method Using all method
set_a = set(input().split())
num_of_set = int(input())
is_superset = True
for _ in range(num_of_set):
    custom_set = set(input().split())
    if not all(element in set_a for element in custom_set):
        is_superset = False
        break
print(is_superset)    


#######################################################################
################################### # Question #*(No Idea)
# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = list(map(int, input().split()))
arr = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))
happiness = 0
for k in arr:
    if k in A:
        happiness = happiness + 1
    elif k in B:
        happiness = happiness - 1
    else:
        happiness      
print(happiness)



####################################################################
############################################################ (Maths)
####################################################################

######################################################################
################################# #* Question (Polar Coordinates)
# * Polar coordinates are an alternative way of representing Cartesian coordinates or Complex Numbers.
""" A complex number z is
                        z = x + yj
determined by its real part x and imaginary part y .Here, j is the imaginary unit.
A polar coordinate (r,φ):
is completely determined by modulus r and phase angle φ.
r: Distance from z to origin, i.e., sqrt of (x**2+y**2)
φ: Counter clockwise angle measured from the positive x-axis to the line segment that joins z to the origin.

#* Python's cmath module provides access to the mathematical functions for complex numbers.

you can represent complex numbers in polar form using the cmath module,
... which is an extension of the built-in math module for complex numbers
#* cmath.phase: This tool returns the phase of complex number  (also known as the argument of z ).
phase(complex(-1.0, 0.0))
output: 3.1415926535897931

#* abs: This tool returns the modulus (absolute value) of complex number.
abs(complex(-1.0, 0.0))
output: 1.0
"""

# for example: Here's how we can represent a complex number in polar form:
# Define the complex number in rectangular form
complex_number = 3 + 4j

# Convert the complex number to polar form
import cmath
magnitude = abs(complex_number)
phase_radians = cmath.phase(complex_number)
phase_degrees = cmath.phase(complex_number) * 180 / cmath.pi

print("Polar Form:")
print(f"Magnitude: {magnitude}")
print(f"Phase (radians): {phase_radians}")
print(f"Phase (degrees): {phase_degrees}")


# * Question (Polar Coordinates) answer
complex_number = complex(input())
print(abs(complex_number))
print(cmath.phase(complex_number))

# Or
from cmath import*
complex_number = complex(input())
print(abs(complex_number))
print(phase(complex_number))


# 2nd method using polar attribute
z = complex(input())
r, theta = cmath.polar(z)
print(r, theta, sep='\n')


# * Note: Importing module take example
"""
When you use import math, you import the entire math module into your code.
This means you can access all the functions and variables in the math module using the math prefix.
For example, you would use functions like math.sqrt() and math.sin().
"""
x = 16
sqrt_x = math.sqrt(x)
sin_x = math.sin(x)

"""
#* Note: When you use from math import *,
you import all functions and variables from the math module directly into your code's namespace.
This means you can use the functions and variables without the need for the math prefix.
it's generally not recommended to use the import * syntax
as it can lead to name conflicts and make your code harder to understand,
especially when working with multiple modules.
"""

x = 16
sqrt_x = sqrt(x)
sin_x = sin(x)

###########################################################################
############################# Question Answeer #* Polar Coordinates
# key concept , cmath, polar cordinates
"""
Polar coordinates are an alternative way of representing Cartesian coordinates or Complex Numbers.
ex. z = x + iy
A complex number z is completely determined by its real part x and imaginary part y.
Here, i is the imaginary unit.
If we convert complex number z to its polar coordinate, we find:
r: Distance from z to origin, i.e., sqr(x^2+y^2)
phase(p):: Counter clockwise angle measured from the positive x-axis to the line segment that joins z to the origin.
Python's cmath module provides access to the mathematical functions for complex numbers.
"""
# cmath.phase:- This tool returns the phase of complex number z (also known as the argument of z).
phase_angle = cmath.phase(complex(-1.0, 0.0))
print(phase_angle)
# >>> 3.1415926535897931

# abs:- This tool returns the modulus (absolute value) of complex number z.
abs(complex(-1.0, 0.0))

# >>> 1.0

# Problem sol
# Input the real and imaginary parts separately
real_part = float(input("Enter the real part: "))
imaginary_part = float(input("Enter the imaginary part: "))

# Create the complex number using the input values
complex_number = complex(real_part, imaginary_part)

r = sqrt(real_part**2 + imaginary_part**2)
angle = cmath.phase(complex(real_part, imaginary_part))
print(r)
print(angle)


# OR IF input is given
z = complex(input())
real_part = z.real
imaginary_part = z.imag
r = sqrt(real_part**2 + imaginary_part**2)
angle = cmath.phase(complex(real_part, imaginary_part))
print(r)
print(angle)

# 2nd method
complex_no = complex(input())
r, t = cmath.polar(complex_no)
print(r)
print(t)

# 3rd method
a = complex(input())
print(abs(a))
print(cmath.phase(a))


####################################################################
#################### #* Question (Find Angle MBC)
import math
AB = int(input())
BC = int(input())
theta = (math.atan(AB/BC))
theta_to_degree = round(math.degrees(theta))

print(f"{theta_to_degree}{chr(176)}")


# 2nd method Or directly importing mudule functions
from math import*
a = int(input())
b = int(input())
print(str(round(degrees(atan(a/b))))+"\u00b0")  # \u00b0 is degree symbol (°)


####################################################################
######################## #* Question (Triangle Quest 2)
# 1st method 
for i in range(1,int(input())+1):
    print((((10**i) - 1)**2) // 81)


####################################################################
################### # * Question (Mod Divmod)
#🔑 divmod() function
a = int(input())
b = int(input())
c = divmod(a,b)
for x in c:
    print(x)
print(c)


####################################################################
######################## # * Question (Power -Mod Power)
#🔑 (Power - Mod Power)
# pow(): With this funx In Python we can be calculated Powers or exponents using the built-in power function.
pow(a,b) #or pow(a,b)

# It's also possible to calculate a^b and mod m
pow(a,b,m)

# Note: Here,  and  can be floats or negatives, but, if a third argument is present,  cannot be negative.
# Note: Python has a math module that has its own pow(). It takes two arguments and returns a float. It is uncommon to use math.pow().

#Questions answer
a = int(input())
b = int(input())
m = int(input())
print(pow(a,b))
print(pow(a,b,m))


####################################################################
######################## # * Question (Integers Come In All Sizes)
a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(a**b+c**d)

    
####################################################################
######################## #* Question (Triangle Quest)
for i in range(1,int(input())): 
    print(((10**i)//9)*i)





####################################################################
####################################################### (itertools)
####################################################################

###################################################################
############################## # * itertools In Python :-
import itertools

itertools_functions = [itertools.count, itertools.cycle, itertools.repeat, itertools.chain, itertools.zip_longest,
                    itertools.islice, itertools.filterfalse, itertools.combinations, itertools.permutations,
                    itertools.product, itertools.groupby, itertools.accumulate, itertools.starmap,
                    itertools.tee, itertools.dropwhile, itertools.takewhile, itertools.compress]

# You can access the functions from the list like this:
for func in itertools_functions:
    print(func.__name__)



""" 
itertools is a module in Python's standard library that provides a set of fast,
memory-efficient tools for working with iterators, which are objects that can be iterated over (print(dir(itertools))
"""

""" 
itertools is a module in Python's standard library that provides a set of fast,
memory-efficient tools for working with iterators, which are objects that can be iterated over (like lists or strings)
but do not store their contents in memory all at once.
"""
# Here are some notable
# * product: Returns the Cartesian product of input iterables.
numbers = [1, 2]
colors = ['red', 'blue']
cartesian_product = list(product(numbers, colors))
# Output: [(1, 'red'), (1, 'blue'), (2, 'red'), (2, 'blue')]


# * permutations: Returns all possible permutations of elements from an iterable.
letters = ['A', 'B', 'C']
perms = list(permutations(letters))
# Output: [('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ...]


# * groupby : Groups consecutive keys and groups from the iterable.
animals = ['cat', 'dog', 'cow', 'duck', 'elephant']
def key_func(x):
    return x[0]


grouped = groupby(animals, key_func)
for key, group in grouped:
    print(key, list(group))
# Output:
# 'c': ['cat', 'cow']
# 'd': ['dog', 'duck']
# 'e': ['elephant']


# * zip_longest: Aggregates elements from each of the iterables. If the iterables are of uneven length, fill missing values with a specified fill value.
from itertools import zip_longest
numbers = [1, 2, 3]
colors = ['red', 'blue']
zipped = list(zip_longest(numbers, colors, fillvalue=None))
# Output: [(1, 'red'), (2, 'blue'), (3, None)]


# * takewhile: Returns elements from the iterable as long as the elements are true.
from itertools import takewhile
numbers = [1, 2, 3, 4, 5]
taken = list(takewhile(lambda x: x < 3, numbers))  # Output: [1, 2]


# * product:Returns the Cartesian product of input iterables.
numbers = [1, 2]
colors = ['red', 'blue']
cartesian_product = list(product(numbers, colors))
# Output: [(1, 'red'), (1, 'blue'), (2, 'red'), (2, 'blue')]


# * combinations:Returns all possible combinations of length r from an iterable.
numbers = [1, 2, 3]
combs = list(combinations(numbers, 2))  # Output: [(1, 2), (1, 3), (2, 3)]


# * chain: Chains multiple iterables together into a single iterable.
from itertools import chain 
list1 = [1, 2, 3]
list2 = [4, 5, 6]
chained = list(chain(list1, list2))  # Output: [1, 2, 3, 4, 5, 6]


###############################################################
######################## #* Question (itertools.product())

"""
#* itertools.product():-
This tool computes the cartesian product of input iterables.
It is equivalent to nested for-loops.
For example, product(A, B) returns the same as ((x,y) for x in A for y in B).
#* Example
"""
from itertools import product
print(list(product([1,2,3],repeat = 2)))
# >>> Output:- [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
print(list(product([1,2,3],[3,4])))
# >>> Output:- [(1, 3), (1, 4), (2, 3), (2, 4), (3, 3), (3, 4)]
A = [[1,2,3],[3,4,5]]
print(list(product(*A)))
# >>> Output:- [(1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 3), (3, 4), (3, 5)]
B = [[1,2,3],[3,4,5],[7,8]]
print(list(product(*B)))
# >>> Output:- [(1, 3, 7), (1, 3, 8), (1, 4, 7), (1, 4, 8), (1, 5, 7), (1, 5, 8), (2, 3, 7), (2, 3, 8), (2, 4, 7), (2, 4, 8), (2, 5, 7), (2, 5, 8), (3, 3, 7), (3, 3, 8), (3, 4, 7), (3, 4, 8), (3, 5, 7), (3, 5, 8)]

#* Question's answer
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))
print(*list(product(list1,list2)))

# 1st method by using product method
list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))
print(*list(product(list1, list2)))
# Or directly print(*product(map(int,input().split()),map(int,input().split())))


# 2nd method By using list comprehension
A = input().split()
B = input().split()
cartesian = [(int(i), int(j)) for i in A for j in B]
print(*cartesian)

# OR
A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(*[(i, j) for i in A for j in B])


# EOF (End of File) error occurs when the input() function tries to read input from the user but finds that the input stream has ended, and there is no more data to read.
# 3rd METHOD by nested and end optional argument
# Remember for li manupulation join, iterating a loop and print with 'end = ""' optional argument or  Join is best
listA = list(map(int, input().split()))
listB = list(map(int, input().split()))
for i in listA:
    for j in listB:
        print((i, j), end=" ")
        # Or print((eval(i),eval(j)), end=' ')


####################################################################
######################## #* Question (itertools.permutations())
"""
#* itertools.permutations(iterable[, r]):-
This tool returns successive  length permutations of elements in an iterable.
If  is not specified or is None, then  defaults to the length of the iterable,
-- and all possible full length permutations are generated.
Permutations are printed in a lexicographic sorted order. So, if the input iterable is sorted,
-- the permutation tuples will be produced in a sorted order
#* Example
"""
from itertools import permutations
print(permutations(['1','2','3']))
# >>> Output: <itertools.permutations object at 0x02A45210>

print(list(permutations(['1','2','3'])))
# >>> Output: [('1', '2', '3'), ('1', '3', '2'), ('2', '1', '3'), ('2', '3', '1'), ('3', '1', '2'), ('3', '2', '1')]

print(list(permutations(['1','2','3'],2)))
# >>> Output: [('1', '2'), ('1', '3'), ('2', '1'), ('2', '3'), ('3', '1'), ('3', '2')]

print(list(permutations('abc',3)))
# >>> Output: [('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')]


#*Q answer
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
my_str, length = input().split()
lengt = int(length)
my_per = sorted(list(permutations(my_str,lengt)))
for i in my_per:
    print("".join(str(k) for k in i))


################################################################
# Question #* itertools.permutations()
# 1st method
m, n = input().split()
n = int(n)
pr = list(permutations(m, n))
li = []
for i in pr:
    li.append(''.join(i))
li = sorted(li)
print(*li, sep="\n")

# 2nd method By list comprehension
m, n = input().split()
n = int(n)
pr = list(permutations(m, n))
sort_li = sorted([''.join(k) for k in pr])
print(*sort_li, sep="\n")

# 3rd method by using lambda
m, n = input().split()
n = int(n)
pr = list(permutations(m, n))
sort_li = sorted(pr, key=lambda k: ''.join(k))
for permutation in sort_li:
    print(''.join(permutation))
# print(*[''.join(k) for k in sort_li], sep = '\n')

# Sorting a dictinary
list = ['2022 Population', '2020 Population', '2015 Population', '2010 Population',
        '2000 Population', '1990 Population', '1980 Population', '1970 Population']
pop_dic = {}
for i in list:
    k = i.split()
    pop_dic[k[0]] = k[1]
print(pop_dic)
new_po = dict(sorted(pop_dic.items(), key=lambda item: item[0]))
print(new_po)
li = []
for k, v in new_po.items():
    li.append(' '.join([k, v]))
print(li)




####################################################################
######################## #* Question (itertools.combinations())
"""
#*itertools.combinations(iterable, r) :-
This tool returns the r length subsequences of elements from the input iterable.
Combinations are emitted in lexicographic sorted order. So, if the input iterable is sorted,
the combination tuples will be produced in sorted order.
#* Example
"""
from itertools import combinations
print(list(combinations('12345',2)))
# >>> [('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('2', '3'), ('2', '4'), ('2', '5'), ('3', '4'), ('3', '5'), ('4', '5')]
A = [1,1,3,3,3]
print(list(combinations(A,4)))
# >>> [(1, 1, 3, 3), (1, 1, 3, 3), (1, 1, 3, 3), (1, 3, 3, 3), (1, 3, 3, 3)]




# Q answer
from itertools import combinations
my_str, str_length = input().split()
str_length = int(str_length)
my_str = sorted(my_str)
for i in range(1,str_length+1):
    my_comb = sorted(list(combinations(my_str, i)))
    for j in my_comb:
        print("".join(str(k) for k in j))

"""
In Python, the strip() method is a built-in string method that is used to remove leading and trailing whitespace characters from a string.
Whitespace characters include spaces, tabs, and newline characters.

The general syntax of the strip() method is:
                                            string.strip([characters])
string: The string on which the strip() method is called. This is the string from which leading and trailing whitespace will be removed.

characters (optional): An optional argument that specifies the characters to be removed from the beginning
and end of the string.If not provided, the strip() method removes all whitespace characters.
If you pass a string containing specific characters, it will remove those characters
from the beginning and end of the string, but not from within the string.
#* Example
"""
# Example 1: Basic usage to remove leading and trailing spaces
text = "  Hello, World!   "
cleaned_text = text.strip()
print(cleaned_text)  # Output: "Hello, World!"

# Example 2: Removing specific characters from the beginning and end
text = "###Python is awesome###"
cleaned_text = text.strip("#")
print(cleaned_text)  # Output: "Python is awesome"

# Example 3: Removing specific characters from both sides
text = "xxxHello, World!xxx"
cleaned_text = text.strip("x")
print(cleaned_text)  # Output: "Hello, World!"

# Example 4: Using strip() with newline characters
text = "\n\n\nHello, World!\n\n\n"
cleaned_text = text.strip()
print(cleaned_text)  # Output: "Hello, World!"


####################################################################
##################### # * itertools.combinations_with_replacement()

"""
#* This tool returns length subsequences of elements from the input iterable allowing individual elements to be repeated more than once.
#* Combinations are emitted in lexicographic sorted order. So,
#* -- if the input iterable is sorted, the combination tuples will be produced in sorted order.

"""

from itertools import combinations_with_replacement
print(list(combinations_with_replacement('12345',2)))
[('1', '1'), ('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('2', '2'), ('2', '3'), ('2', '4'), ('2', '5'), ('3', '3'), ('3', '4'), ('3', '5'), ('4', '4'), ('4', '5'), ('5', '5')]


A = [1,1,3,3,3]
print(list(combinations(A,2)))
[(1, 1), (1, 3), (1, 3), (1, 3), (1, 3), (1, 3), (1, 3), (3, 3), (3, 3), (3, 3)]

#* Questionn answer
from itertools import combinations_with_replacement
my_str, my_length = input().split()
my_length = int(my_length)
my_str = sorted(my_str)
comb = sorted(list(combinations_with_replacement(my_str, my_length)))
for i in comb:
    print("".join(str(k) for k in i))


# Note;-  "indices" is used to refer to multiple occurrences or positions, while "index" is used to refer to a single occurrence or position.
"""

# * Example1
String: "banana"
The indices of the letter 'a' in the string 'banana' are 1, 3, and 5."And
#* when referring to a single occurrence, we use the singular "index":
#* The index of the first occurrence of the letter 'a' in the string 'banana' is 1."

List: [2, 5, 8, 5, 3, 5]
The indices of the number 5 in the list are 1, 3, and 5.
The index of the first occurrence of the number 5 in the list is 1.

#* Example 2: Have a string and want to find the index of the first occurrence of the letter 
String: "elephant"
The index of the first occurrence of the letter 'e' in the string 'elephant' is 0.

#* Example 3: SupposeHave a table representing students' grades, and want to find the indices (row numbers) of students who scored above 90. The table is as follows:
Table: Grades

| Student | Score |
|---------|-------|
| Alice   | 85    |
| Bob     | 92    |
| Claire  | 78    |
| David   | 98    |

In this case, students with scores above 90 are Alice and David, and their row indices are 1 and 3,
respectively. So, when talking about multiple occurrences, we use "indices"
The indices of students who scored above 90 are 1 and 3.
The index of the first student who scored above 90 is 1.
"""




####################################################################
#################### # * Iterables and Iterators
"""
The itertools module standardizes a core set of fast,
memory efficient tools that are useful by themselves or in combination. Together,
they form an iterator algebra making it possible to construct specialized tools succinctly and efficiently in pure Python.
#* Infinite Iterators:

Iterator        Arguments       Results                                         Example
count()         start, [step]   start, start+step, start+2*step, …              count(10) --> 10 11 12 13 14 ...
cycle()         p               p0, p1, … plast, p0, p1, …                      cycle('ABCD') --> A B C D A B C D ...
repeat()        elem [,n]=      elem, elem, elem, … endlessly or up to n times  repeat(10, 3) --> 10 10 10

#* Iterators terminating on the shortest input sequence:
chain()         p, q, …         p0, p1, … plast, q0, q1, …                      chain('ABC', 'DEF') --> A B C D E F
compress()      data, selectors (d[0] if s[0]), (d[1] if s[1]), …               compress('ABCDEF', [1,0,1,0,1,1]) --> A C E F
dropwhile()     pred, seq       seq[n], seq[n+1], starting when pred fails      dropwhile(lambda x: x<5, [1,4,6,4,1]) --> 6 4 1
groupby()       iterable[, keyfunc]sub-iterators grouped by value of keyfunc(v)
takewhile()     pred, seq   seq[0], seq[1], until pred fails    takewhile(lambda x: x<5, [1,4,6,4,1]) --> 1 4
izip()  p, q, …      (p[0], q[0]), (p[1], q[1]), …   izip('ABCD', 'xy') --> Ax By
izip_longest()  p, q, … (p[0], q[0]), (p[1], q[1]), …   izip_longest('ABCD', 'xy', fillvalue='-') --> Ax By C- D-

#* Combinatoric generators:
product('ABCD', repeat=2)   AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
permutations('ABCD', 2)     AB AC AD BA BC BD CA CB CD DA DB DC
combinations('ABCD', 2)     AB AC AD BC BD CD
combinations_with_replacement('ABCD', 2)    AA AB AC AD BB BC BD CC CD DD

"""

import itertools
my_list = [[1,2],[5,6],[8,9]]
print(list(itertools.product(*my_list)))
# >>> [(1, 5, 8), (1, 5, 9), (1, 6, 8), (1, 6, 9), (2, 5, 8), (2, 5, 9), (2, 6, 8), (2, 6, 9)]


## Question Answer
from itertools import combinations
len_list=int(input())
my_string=input().split()
my_indices=int(input())
count=0
my_combinations=list(combinations(my_string,my_indices))
for x in my_combinations:
    if "a" in x:
        count+=1
print(count/len(my_combinations))


# 2 method using list comprehension
from itertools import combinations
len_list=int(input())
my_string=input().split()
my_indices=int(input())
my_combinations=list(combinations(my_string,my_indices))
count = sum(1 for x in my_combinations if "a" in x)
result = count / len(my_combinations)
print(result)


# 3rd method
from itertools import combinations

n, s, k = input(), input().split(), int(input())
combos = list(combinations(s, k))
print(f"{sum('a' in c for c in combos) / len(combos):.6f}")

# remember it's better to use genrator(comp) instead of list(comp) for efficient and faster bcz it doesn't store value in ram all at once
"""
Python's f-strings to format floating-point numbers.
#* Genral syntax: - f"{variable:.nf}
    where n is the number of decimal places you want to display.
example
"""
# No Formatting
num = 3.14159265
print(f"{num}") # output:- 3.14159265

# Fixed Decimal Places with :.2f:
num = 3.14159265
print(f"{num:.2f}") # output:- 3.14

# Fixed Decimal Places with :.6f:
num = 3.14159265
print(f"{num:.6f}") # output:- 3.141592

# Using Variables:
decimal_places = 3
formatted_num = f"{num:.{decimal_places}f}"
print(formatted_num)


####################################################################
#################### # *  Maximize It!
# m, *n = map(int, input().split()) #it's better to use when you don't know no. of input value map retruns genrator objets
# m, *n = list(map(int, input().split()))
"""
#*  m, *n = list(map(int, input().split()))

let's soppose users enters the input "10 20 30".
*n in the unpacking operator is called the splat operator.
It tells Python to unpack all the remaining values in the list to the variable n.
In this case, the list will contain three integers, so the variable n will be a list of three integers.

The output of the code will be the two integers 10 and the list [20, 30].

"""
# m, n = list(map(int, input().split())) will take two value as user input 
# suppose the user enters the input "10 20" then there are enough values to unpack. The output of the code will be the two integers 10 and 20.
def g(str1):
    m, n = list(map(int, str1.split()))
    return m, n
result = g("10 20 ")
print(result)

# If suppose the user enters the input "10 20 30" will get a ValueError: too many values to unpack (expected 2) error 
"""
for avoiding this can use
try:
    m, n = list(map(int, input().split()))
except ValueError:
    print("Error: Please enter two integers")
"""

# m, n, l = list(map(int, input().split())) expect three value as input otherwise give ValueError if more 3 or less 3 you passed value

# testcase
def g(str1):
    m, n = list(map(int, str1.split()))
    return type(m), type(n)
result = g("10 20 ")
print(result)
# output >>> (<class 'int'>, <class 'int'>)

def g(str1):
    m, n = map(int, str1.split())
    return type(m), type(n)
result = g("10 20 ")
print(result)
# output >>> (<class 'int'>, <class 'int'>)


def g(str1):
    m, *n = map(int, str1.split())
    return type(m), type(n)
result = g("10 20 30 ")
print(result)
# output >>> (<class 'int'>, <class 'list'>)

#* Note bcz "*" returns lists

# Questions answer
#* 1st method by using for loop with itertools function product

from itertools import product
m, n = map(int, input().split())
my_list = []
for _ in range(m):
    my_input = list(map(int, input().split()))[1:] #as per constrain
    my_list.append(my_input)
comb_slcxn = list(product(*my_list))
max_list2 = []
for k in comb_slcxn:
    sum_square = sum([i**2 for i in k])%n
    max_list2.append(sum_square)
print(max(max_list2))

#Or can write even more shorter and
from itertools import product
m, n = map(int, input().split())
comb_slcxn, max_list = [], []
for _ in range(m):
    comb_slcxn.append(list(map(int, input().split()))[1:])
for k in product(*comb_slcxn):
    max_list.append(sum([i**2 for i in k])%n)
    # 
print(max(max_list))


#* Second way to do 

# But it's better to go with initialize value rather than intialize list two times bcz it's more efficieant

from itertools import product
m, n = map(int, input().split())
my_list = []
for _ in range(m):
    my_input = list(map(int, input().split()))[1:] # it also contains (the number of elements) so it must be excluded
    my_list.append(my_input)
comb_slcxn = list(product(*my_list))
max_sum = 0
for k in comb_slcxn:
    sum_square = sum([i**2 for i in k])%n
    # max_list.append(sum((i**2 for i in k))%n) for such calculation genrator expresion way better than list comprehns
    max_sum = max(max_sum, sum_square)
print(max_sum)

#OR
from itertools import product
m, n = map(int, input().split())
comb_slcxn = []
# we can also accomplish aboce two line into one line
# m, n = map(int, input().split()); comb_slcxn = []
for _ in range(m):
    comb_slcxn.append(list(map(int, input().split()))[1:])
max_sum = 0
for k in product(*comb_slcxn):
    max_sum = max(max_sum, sum([i**2 for i in k])%n)
print(max_sum)


from itertools import product
N , M = map(int,input().split()) ;
res = [[int(j)**2 for j in input().split()[1:]] for i in range(N)]
print(max((sum(i)%M for i in product(*res))))
# print(max((sum(i)%M for i in product(*[[int(j)**2 for j in input().split()[1:]] for i in range(N)]))))

#* 3RD METHOD by using lambda

# (As usuaul I use it for map, filter, or sorted.)
square_lambda = lambda x: x**2
print(type(square_lambda)) #output <class 'function'>

my_list = [1,2,3,4]
sm = sum((lambda x: x**2)(x) for x in my_list)
print(sm) #output 30
# Note; (lambda x: x**2): here lambda function that takes an argument x and returns x**2, which is the square of x.

#        (x): (x) is the argument that is immediately passed to the lambda function. means lambda function is being invoked with the value of x.

from itertools import product
m, n = map(int, input().split())
comb_slcxn = []
for _ in range(m):
    comb_slcxn.append(list(map(int, input().split()))[1:])
max_sum = 0
for k in product(*comb_slcxn):
    max_sum = max(max_sum, sum((lambda x: x**2)(x) for x in k)%n)
print(max_sum)

# Or also can be write 
from itertools import product
m, n = map(int, input().split())
comb_slcxn = (list(map(int, input().split()))[1:] for _ in range(m))
s = [sum(map(lambda x: x*x, i))%n for i in product(*comb_slcxn)]
print(max(s))



####################################################################
#################### # *  Compress the String!
"""the groupby function used to group elements from an iterable based on a key function.
It's particularly useful when you have a sorted iterable and you want to group adjacent elements that share the same key.

basic syntax of the groupby function:
#*                                    groupby(iterable, key_function)
"""

from itertools import groupby
def key_function():
    pass
iterable = [1,2,3]
groupby(iterable, key_function)


# Example
from itertools import groupby
my_list = [1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 4,5,1]
print(groupby(my_list)) #output <itertools.groupby object at 0x0000027973892610>

#
from itertools import groupby
my_list = [1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 4,5,1]
grouped_data = groupby(my_list)
for key, group in grouped_data:
    print(key, group)
# >>> 1 <itertools._grouper object at 0x0000021CAAFF12A0>
# >>> 2 <itertools._grouper object at 0x0000021CAAFF34F0> and so on

#
from itertools import groupby
my_list = [1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 4,5,1]
grouped_data = groupby(my_list)
for key, group in grouped_data:
    print(key, list(group))
"""
output:-
>>> 1 [1, 1]      
>>> 2 [2, 2, 2]   
>>> 3 [3, 3]      
>>> 4 [4, 4, 4, 4]
>>> 5 [5]
>>> 1 [1]
"""
# Define a key function to check if a number is even or odd
def key_func(item):
    return "even" if item % 2 == 0 else "odd"

# Group the data based on the key function
my_list = [1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 4,5,1]
grouped_data = groupby(my_list, key_func)


# Print the grouped data
for key, group in grouped_data:
    print(f"Key: {key}, Group: {list(group)}")
# >>> Key: odd, Group: [1, 1]
# >>> Key: even, Group: [2, 2, 2]   
# >>> Key: odd, Group: [3, 3]       
# >>> Key: even, Group: [4, 4, 4, 4]

set_a = {1, 2, 3, 4, 5}
set_b = {3, 4, 5, 6, 7}
common_elements = {x for x in set_a if x in set_b}
print(common_elements)
# Output:{3, 4, 5}

# 1st method
from itertools import groupby
my_string = input()
groups = groupby(my_string)
my_list = []
for key, group in groups:
    key, my_list.append(list(group))
my_list2 = []
for i in my_list:
    occ = len(i)
    item = set(map(int, i))
    my_list2.append((occ, *item))
print(*my_list2)  

# 2nd method
from itertools import groupby
my_string =input()
for key ,group in groupby(my_string):
    print((len(list(j)),int(i)),end=' ')
    # print(f'({len(list(j))}, {int(i)})', end = ' ')


# 3rd method by simple using list comprehension
from itertools import groupby
print(*[(len(list(group)),int(key)) for key,group in groupby(input())])
# print(' '.join(str((len(list(group)), int(key))) for key, group in groupby(input()))) #join only work with str
from itertools import groupby
print(*[(len(list(g)), int(k)) for k, g in groupby(input())])


# 4th method using else if 
inp = input()
cur_num = inp[0]
val = 0
for i in inp:
    if i == cur_num:
        val += 1
    else:
        print(f"({val}, {cur_num})", end=" ")
        cur_num = i
        val = 1
print(f"({val}, {cur_num})")

# Or also 
string = input()
u=1
for i,letter in enumerate(string):
    if i+1 < len(string):           
        if letter == string[i+1]:
            u += 1
        else:
            print((u,int(letter)), end=" ")
            u = 1
    else:
        print((u,int(letter)))

#Or also can be done by without enumerate function
s=input()
s+=' '
c=1 
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        c+=1
    else:
        print((c,int(s[i])),end=' ')
        c=1


string = ""
count = 1
for i in range(len(s)):
    if i < len(s) - 1 and s[i] == s[i + 1]:
        count += 1
    else:
        string += f"({count}, {s[i]}) "
        count = 1
print(string.strip())






####################################################################
####################################################### (Collections)
####################################################################


##################################################################
################## Question #*collections.namedtuple()
# Note :-
"""
*Diffrence between collections and itertools
Purpose:

collections module: The primary purpose of the collections module is to provide additional data structures and tools for working with collections (groups of elements). It offers specialized data types like namedtuple, defaultdict, Counter, and deque, which are optimized for specific use cases.
itertools module: The itertools module, on the other hand, focuses on providing tools for working with iterators. It includes functions to create, combine, and manipulate iterators efficiently. The functions in itertools enable tasks related to iteration, combinations, and permutations.

Data Structures vs. Iterators:
collections deals with data structures like dictionaries (defaultdict, Counter), lists (deque), and named tuples (namedtuple).
itertools deals with iterators and generator functions, allowing you to perform operations on sequences of data without the need to load all elements into memory at once.

Use Cases:
collections is handy for tasks related to data storage, counting, and data manipulation. For example, Counter is great for counting the occurrences of elements in a collection, and deque is useful for implementing efficient queues and stacks.
itertools is useful for solving combinatorial problems, creating complex iterator patterns, and handling large datasets efficiently. For example, product helps generate Cartesian products of multiple iterables, and combinations generates all possible combinations of elements from an iterable.

Input and Output:
collections typically take containers (lists, tuples, etc.) as input and return specialized data structures or dictionary-like objects.
itertools functions usually take iterators or iterables as input and return iterator objects.
While both modules contribute to handling and manipulating data in Python, their specific purposes and functionalities are distinct. Understanding the differences between them helps you choose the right tools for the task at hand, whether it's working with data structures or managing iterations and combinations efficiently.
"""


"""
* collections module :- A built-in module that provides specialized data structures as alternatives to the built-in data types like lists, tuples, sets, and dictionaries.
* --The collections module includes several container data types that offer additional functionality beyond the standard data types.
"""

# Here are some commonly used data structures from the collections module

# * namedtuple: Factory function for creating tuple subclasses with named fields.
from collections import namedtuple
Person = namedtuple('Person', ['name', 'age'])
person = Person(name='John', age=30)
print(person.name)  # Output: 'John'
print(type(Person)) #<class 'type'>


# *Counter: Dict subclass for counting hashable objects.
from collections import Counter
colors = ['red', 'blue', 'red', 'green', 'blue', 'red']
color_count = Counter(colors)
print(color_count)  # Output: Counter({'red': 3, 'blue': 2, 'green': 1})
print(type(color_count)) #Output: <class 'collections.Counter'>


# * ChainMap: A class for combining several mappings into a single view.
from collections import ChainMap
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
chain_map = ChainMap(dict1, dict2)
print(chain_map['a'])  # Output: 1
print(type(chain_map)) #Output: <class 'collections.ChainMap'>


# * OrderedDict: A dictionary subclass that remembers the order in which items were added.
ordered_dict = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(ordered_dict)  # Output: OrderedDict([('a', 1), ('b', 2), ('c', 3)])


# * defaultdict: Dict subclass that calls a factory function to supply missing values.
d = defaultdict(int)
d['a'] += 1
print(d['a'])  # Output: 1


# * deque: A list-like container with fast appends and pops on both ends.
d = deque([1, 2, 3])
d.append(4)
d.appendleft(0)
print(d)  # Output: deque([0, 1, 2, 3, 4])





######################################################################################
########################################## Question #* collections.Counter()
#  Notable point
# symmetric diffrence
#  (XOR) a ^ b == a.difference(b) | b.difference(a) == a.symmetric_difference(b)
"""
collections.Counter()
A counter is a container that stores elements as dictionary keys, and their counts are stored as dictionary values.

Example:-
"""
from collections import Counter
myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
print(Counter(myList)) # Output: Counter({2: 4, 3: 4, 1: 3, 4: 2, 5: 1})
print(type(Counter(myList))) # Output: <class 'collections.Counter'>


print(Counter(myList).items())
# Output: dict_items([(1, 3), (2, 4), (3, 4), (4, 2), (5, 1)])

print(Counter(myList).keys())
# Output: dict_keys([1, 2, 3, 4, 5])

print(Counter(myList).values())
# Output: dict_values([3, 4, 4, 2, 1])


# 1st method without using counter
num_shoes = int(input())
num_size = list(map(int, input().split()))
num_cust = int(input())
count = 0
for i in range(num_cust):
    m, n = map(int, input().split())
    if m in num_size:
        count = n + count
        num_size.remove(m)
print(count)

#Or can be done by index
num_shoes = int(input())
num_size = list(map(int, input().split()))
c = int(input())
count = 0
for i in range(c):
    k = list(map(int, input().split()))
    if k[0] in num_size:
        count += k[1]
        del num_size[num_size.index(k[0])]
print(count)



# 2nd method By using counter
X = int(input())
shoes = Counter(map(int, input().split()))
# "4 5 6 7 7"
# ["4","5","6","7","7"]
# [4,5,6,7,7]
# {4:1,5:1,6:1,7:2}
N = int(input())
count = 0
for i in range(N):
    size, price = map(int, input().split())
    if shoes[size] > 0:
        shoes[size] -= 1
        count += price
print(count)

#Or
from collections import Counter
input()
shoes= list(input().split())
money = 0
for i in range(int(input())):
    size, price = input().split()
    if size in Counter(shoes) and Counter(shoes).values != 0:
        money += int(price)
        shoes.remove(size)
print(money)




##################################################################
####################### Question #* DefaultDict Tutorial

"""
The defaultdict tool is a container in the collections class of Python.
It's similar to the usual dictionary (dict) container,
but the only difference is that a defaultdict will have a default value
if that key has not been set yet. If you didn't use a defaultdict
you'd have to check to see if that key exists, and if it doesn't, set it to what you want.

example
"""
d = defaultdict(list)
d['python'].append("awesome")
d['something-else'].append("not relevant")
d['python'].append("language")
for i in d.items():
    print(i)
# >>> ('python', ['awesome', 'language'])
# >>> ('something-else', ['not relevant'])

# 1st method
from collections import defaultdict
d = defaultdict(list)
n, m = map(int, input().split())
for i in range(1, n + 1):
    key = input()
    d[key].append(i)
for i in range(m):
    key = input()
    if key in d:
        # or print(' '.join(d[val]))
        print(" ".join(str(value) for value in d[key]))
    else:
        print(-1)

        
# Note :- join method cannot be directly applied to integers because it expects an iterable of strings as its argument.
#      -- However, you can convert the integers to strings using the str() function before using join.

numbers = [1, 2, 3, 4, 5]
joined_numbers = " ".join(str(num) for num in numbers)
print(joined_numbers) # Output: 1 2 3 4 5



# 2nd method
n, m = map(int, input().split())
A = defaultdict(list)
for i in range(n):
    A[input()].append(i+1)
for i in range(m):
    k = input()
    print(*(A[k] if k in A else [-1]), sep=' ')



##################################################################
################## Question #*collections.namedtuple() 
"""
collections.namedtuple()
Basically, namedtuples are easy to create, lightweight object types.
They turn tuples into convenient containers for simple tasks.
With namedtuples, you don’t have to use integer indices for accessing members of a tuple.

it basically takes two arguments: the name of the named tuple and a sequence of field names.
The namedtuple is defined with the name 'Student' (using capitalization conventions for class names).
"""
from collections import namedtuple

# You can choose any name for the variable
CarInfoTemplate = namedtuple('CarInfo', ['model', 'year', 'top_speed'])

# Now create instances of the named tuple using the template
car1 = CarInfoTemplate(model='Sedan', year=2022, top_speed=150)
car2 = CarInfoTemplate(model='SUV', year=2023, top_speed=130)

# Access data using names
print(car1.model)      # Output: Sedan
print(car2.top_speed)  # Output: 130

"""
the variable name CarInfoTemplate to store the named tuple template,
The variable name is the one you use in your code when referring to the template,
and the string inside the namedtuple function (like 'CarInfo' in your example) is more like a label for the template.
The string label doesn't affect how you use the variable later on.
"""


# Example 1:-
Point = namedtuple('Point', 'x,y')
pt1 = Point(1, 2)
pt2 = Point(3, 4)
dot_product = (pt1.x * pt2.x) + (pt1.y * pt2.y)
print(dot_product)


from collections import namedtuple
Car = namedtuple('Car', 'Price Mileage Colour Class')
xyz = Car(Price=100000, Mileage=30, Colour='Cyan', Class='Y')
print(xyz)
# >>> Car(Price=100000, Mileage=30, Colour='Cyan', Class='Y')

Car(Price=100000, Mileage=30, Colour='Cyan', Class='Y')
print(xyz.Class)
# >>> Y


# Example 2:-
from collections import namedtuple
Car = namedtuple('Car','Price Mileage Colour Class')
xyz = Car(Price = 100000, Mileage = 30, Colour = 'Cyan', Class = 'Y')
print(xyz)
# >>> Car(Price=100000, Mileage=30, Colour='Cyan', Class='Y')

Car(Price=100000, Mileage=30, Colour='Cyan', Class='Y')
print(xyz.Class)
# >>> Y


# Question answers
# 1st method with simple initilaze list and named tuple
from collections import namedtuple

N = int(input())
name_column = input().split()
Student = namedtuple('Student', name_column)
total_marks = 0
for _ in range(N):
    named_column = input().split()
    student = Student(*named_column)  # Named tuple instance
    total_marks += int(student.MARKS) 
average = total_marks / N
print(average)



# 2nd method by using list comprehension
from collections import namedtuple
N = int(input())
name_column = input().split()
my_namedtupl = namedtuple('Student', name_column)
# my_namedtupl = namedtuple('Student', input().split())
my_list = [int(my_namedtupl(*input().split()).MARKS) for _ in range(N)]
print(sum(my_list)/N)


# 3rd method without using namedtuple
N = int(input())
column_names = input().split()
print(column_names)
"""
output:
['ID', 'MARKS', 'NAME', 'CLASS']
"""
#now 
N = int(input())
column_names = input().split()
print(column_names)
my_index = column_names.index('MARKS')
print(my_index)
"""
output:
['ID', 'MARKS', 'NAME', 'CLASS']
1
"""

#now
N = int(input())
column_names = input().split()
print(column_names)
my_index = column_names.index('MARKS')
print(my_index)
sum_marks = 0
for i in range(N):
    mark = input().split()
    print(mark)
"""
Output:
['ID', 'MARKS', 'NAME', 'CLASS']
1
['1', '97', 'Raymond', '7']
['2', '50', 'Steven', '4']
['3', '91', 'Adrian', '9']
['4', '72', 'Stewart', '5']
['5', '80', 'Peter', '6']

"""
# Now
N = int(input())
column_names = input().split()
print(column_names)
my_index = column_names.index('MARKS')
print(my_index)
sum_marks = 0
for i in range(N):
    mark = input().split()[my_index ]
    print(mark)
"""
Output
['ID', 'MARKS', 'NAME', 'CLASS']
1
97
50
91
72
80
"""

N = int(input())
column_names = input().split()
my_index = column_names.index('MARKS')
sum_marks = 0
for i in range(N):
    mark = input().split()[my_index]
    sum_marks += int(mark)
print(round(sum_marks/N, 2))

# OR also
num_std = int(input())
marks = input().split().index("MARKS")
print(sum(int(input().split()[marks]) for _ in range(num_std))/num_std)


# 4th method using lambda method
(lambda n, i: print(sum([int(input().split()[i]) for _ in range(n)]) / n))
(int(input()), [i for i, column in enumerate(input().split()) if column.lower() == "marks"][0]) 




# Or You can make eve more shorter
from collections import namedtuple
n = int(input())
Student = namedtuple('Student', input().split())
students = [Student(*input().split()) for _ in range(n)]
print('{:.2f}'.format(sum([int(s.MARKS) for s in students])/n))


from collections import namedtuple
N,Sheet = int(input()),namedtuple('Sheet', input().split())
arr = [int(ele.MARKS) for ele in [Sheet(*input().split()) for _ in range(N)]]
print(sum(arr)/N)

from collections import namedtuple
N,Sheet = int(input()),namedtuple('Sheet', input().split())
print(f'{sum([int(ele.MARKS) for ele in [Sheet(*input().split()) for _ in range(N)]])/N:.2f}')

N,idx = int(input()),input().split().index('MARKS')
print(f'{sum(int(input().split()[idx]) for _ in range(N))/N:.2f}')



##########################################################
############## Question #* Collections.OrderedDict()
# 1st
num_items = int(input())
fruit_dict = OrderedDict()
for _ in range(num_items):
    *item_name, net_price = input().split()
    item_name = ' '.join(item_name)
    net_price = int(net_price)
    fruit_dict[item_name] = fruit_dict.get(item_name, 0) + net_price
for name, total_price in fruit_dict.items():
    print(name, total_price)

# 2nd
fruit_dict = {}
num_items = int(input())
for _ in range(num_items):
    fruit, fruit_price = input().rsplit(" ", 1)
    fruit_price = int(fruit_price)
    if fruit in fruit_dict:
        fruit_dict[fruit] = fruit_dict[fruit] + fruit_price
    else:
        fruit_dict[fruit] = fruit_price
for i in fruit_dict:
    print(i, fruit_dict[i])


# 3rd
fruit_sales = OrderedDict()
for _ in range(int(input())):
    fruit_name, fruit_price = input().rsplit(" ", 1)
    # fruit = input().split()
    # fruit_price = int(s[-1])
    # fruit_name = " ".join(s[0:-1])

    fruit_sales[fruit_name] = fruit_sales.get(fruit_name, 0) + int(fruit_price)
for fruit_name, fruit_price in fruit_sales.items():
    print(f"{fruit_name} {fruit_price}")


def print_rangoli(size):
    # Upper side
    alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    n = size
    for i in range(1, n):
        print('-'.join(alph[n-i:n][::-1] + alph[n-i+1:n]).center(4*n-3, '-'))

    # Center line
    print('-'.join(alph[:n][::-1] + alph).center(4*n-3, '-'))

    # Lower side
    for i in range(n-1, 0, -1):
        print('-'.join(alph[n-i:n][::-1] + alph[n-i+1:n]).center(2*n+1, '-'))


size = int(input("Enter the size: "))
print_rangoli(size)


##########################################################
################### Question #* Word Order
# 1st method by using if and elif method
N=int(input())
s={}
for _ in range(N):
    word = input()
    if word in s.keys():
        s[word] += 1
    else:
        s[word] = 1
print(len(s.keys()))
print(*[i for i in s.values()])


# 2nd method by using get method
N = int(input())
words = []
count = {}
for _ in range(N):
    word = input()
    words.append(word)
    count[word] = count.get(word, 0) + 1
print(len(set(words)))
# or directly input() print(len(count.keys()))/print(len(count.values()))
print(*(count.values()))

# occ_list = []
# for k in count.values():
#     occ_list.append(k)
# print(len(distinct_words))
# print(" ".join(str(i) for i in occ_list))
# print(*(count.values()))

#3rd method by using counter
from collections import Counter 
word=[input() for _ in range(int(input()))]
print(len(Counter(word).keys()))
print(*Counter(word).values(), sep=" ")


#4th method By sing OrderDict()

odic = OrderedDict()
for _ in range(int(input())):
    key = input()
    if key in odic:
        odic[key] += 1
    else:
        odic[key] = 1
print(len(odic))
print(*odic.values())



##########################################################
################### Question #* Collections.deque()
"""
A deque is a double-ended queue. It can be used to add or remove elements from both ends.
Deques support thread safe, memory efficient appends and pops from either side of the deque
with approximately the same (O(1)) performance in either direction.
Example:-
"""
from collections import deque
d = deque()
d.append(1)
print(d) # Output: deque([1])

d.appendleft(2)
print(d) # Output: deque([2, 1])

d.clear()
print(d) # Output: deque([])

d.extend('1')
print(d) # Output: deque(['1'])

d.extendleft('234')
print(d) # Output: deque(['4', '3', '2', '1'])


d.count('1')
print(d) # Output: 1

d.pop('1')
print(d) #Output deque(['4', '3', '2'])

d.popleft()
print(d) #Output deque(['3', '2'])

d.extend('7896')
print(d) #Output deque(['3', '2', '7', '8', '9', '6'])

d.remove('2')
print(d) #Output deque(['3', '7', '8', '9', '6'])

d.reverse()
print(d) #Output deque(['6', '9', '8', '7', '3'])

d.rotate(3)
print(d) #Output deque(['8', '7', '3', '6', '9'])


#Questions answer
# 1st method by using gettattr
from collections import deque
d = deque()
for _ in range(int(input())):
    method, *arg = input().split() #better to use bcz input is dynamically
    getattr(d, method)(*arg)
print(" ".join(d))


# if you wouldn't sure about even an input 
from collections import deque
d=deque()
for x in range(int(input())):
    method =input().split()
    if len(method)>1:
        getattr(d, method[0])(method[1])
    else:
        getattr(d, method[0])()
print(" ".join(list(d)))

#2nd method by eval functions
from collections import deque
d = deque()
for _ in range(int(input())):
    method, *arg = input().split()
    eval('d.' + method)(*arg)
print(*d)


# 3rd method by dictionsary
from collections import deque
n = int(input().strip())
d = deque()
method = {
    'append': lambda x: d.append(x),
    'pop': lambda : d.pop(),
    'appendleft': lambda x: d.appendleft(x),
    'popleft': lambda : d.popleft()
}
for i in range(n):
    comm, *args = input().split()    
    operation = method.get(comm, lambda : None)    
    result = operation(*map(int, args))
print(*[x for x in d], end = ' ')


##########################################################
########################## Question #* Company Logo

# 1st method using python in built funtions get and sorted
if __name__ == '__main__':
    s = list(input())
    s.sort()    # type(s.sort()) : Nonetype
    count = {}
    for letter in s:
        count[letter] = count.get(letter, 0) + 1
    sorted_count = sorted(count.items(), key=lambda x:x[1], reverse = True)
    for k in sorted_count[:3]:
        print(*k)
        


# 2nd method using funtions get and sort with list formed by dict items
s = list(input())
s.sort()
count = {}
for letter in s:
    count[letter] = count.get(letter, 0) + 1 
my_list = list(count.items())
my_list.sort(key = lambda x: x[1], reverse = True)
for k in my_list[:3]:
    print(*k)


# 3rd method by forming list of tuple(word, frequency) using list comprehension from a existing list
s = input()		
char_list = sorted(list(set(s.lower())))
count_lst =[(char, s.count(char)) for char in char_list]
count_lst.sort(key=lambda x: x[1], reverse=True)
for i in range (3):
    x,y = count_lst[i]
    print(f'{x} {y}')

# 4th method by forming list of tuple(word, frequency) using list comprehension from a existing dictionary
s = input()
l = list(set(s))
d = {}
for i in l:
    count = s.count(i)
    d[i] = count
new_l = [(i, d[i]) for i in d]
new_l.sort(key=lambda x: (x[1]*-1, x[0]))
for i in new_l[:3]:
    print(*i)

#5th method using Counter function from collections module
s = input()
from collections import Counter
counted = Counter(s)
the_list = list([(i, counted[i]) for i in counted])
the_list = sorted(the_list, key=lambda x: (-x[1], x[0]))
[print(*i) for i in the_list[:3]]    

# 6th method using if and else without args
if __name__ == '__main__':
    s = list(input())
    s.sort()
    count = {}
    for letter in s:
        if letter in count:
            count[letter] = count[letter] + 1
        else:
            count[letter] = 1 
    my_list = list(count.items())
    my_list.sort(key = lambda x: x[1], reverse = True)
    for k in range(3):
        print(f'{my_list[k][0]} {my_list[k][1]}')
        
# 7th method
if __name__ == '__main__':
    s = input()
    count = {}
    for letter in s:
        count[letter] = count.get(letter, 0) + 1
    sorted_count = sorted(count.items(), key=lambda x:x[0],reverse = False)
    sorted_count = sorted(count.items(), key=lambda x:x[1], reverse = True)
    # but it couldn't sorted simultaneously so wouldn't gonna give expected sorted
    for k in sorted_count[:3]:
        print(*k)

# but it couldn't sorted simultaneously so wouldn't gonna give expected result better to do sorted with both(character and occurence and ) directly
#  So .... here you can do this
    s = input()
    count = {}
    for letter in s:
        count[letter] = count.get(letter, 0) + 1
    sorted_count = sorted(count.items(), key=lambda x:(x[1]*-1,x[0]))
    for k in sorted_count[:3]:
        print(*k)

# any way if you want to sort one by one then do by list of dict items here
if __name__ == '__main__':
    s = input()
    count = {}
    for letter in s:
        count[letter] = count.get(letter, 0) + 1
    sorted_count = list(count.items())
    sorted_count = sorted(sorted_count, key=lambda x:x[0])
    sorted_count = sorted(sorted_count, key=lambda x:x[1], reverse = True)
    # but it couldn't sorted simultaneously so wouldn't gonna give expected sorted
    for k,v in sorted_count[:3]:
        print(k,v)


# 8th method
s=input()
char_count = {}
for char in s:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
sorted_char = sorted(char_count.items(), key=lambda x: (-x[1], x[0]))
for i in range(0,3):
    print(sorted_char[i][0] , sorted_char[i][1])

# Or
s=input()
count = {}
for char in s:
    count[char] = count.get(char,0) + 1
sorted_char = sorted(count.items(), key=lambda x: (-x[1], x[0]))
for i in range(0,3):
    print(sorted_char[i][0] , sorted_char[i][1])
    

    
# 9th method
from collections import Counter
[print(*a) for a in Counter(sorted(input())).most_common(3)]

#Or
[print(*s) for s in __import__('collections').Counter(sorted(input())).most_common(3)]


#10th method
#!/bin/python3
from collections import Counter
if __name__ == '__main__':
    s = input()
listOfChars = list()
listOfChars.extend(s)
listOfChars.sort()
charCount = Counter(listOfChars).most_common(3)
for char in charCount:
    print(f"{char[0]} {char[1]}")

#11th method
s = input()
a = ""
d = []
for i in s:
    if i not in a:
        d.append((i, s.count(i)))
        a += i
d.sort()
d.sort(key=lambda n: n[1], reverse=True)
for i in range(3):
    print(*d[i])

#12th method
s = sorted(input())
cache = {}
for e in s:
    cache[e] = s.count(e)
top_Gs = sorted(cache.items(), key=lambda item: (item[1]), reverse=True)[0:3]
for e in top_Gs:
    print(e[0],e[1])
    
    
#######################################################################
################################# #* Questions Piling Up!

# th method
for i in range(int(input())):
    _ = input()
    blocks = list(map(int, input().split()))
    tip = blocks.index(min(blocks))   
    if (all(i >= j for i, j in zip(blocks[:tip], blocks[1:tip])) and  
        all(i <= j for i, j in zip(blocks[tip:], blocks[tip + 1:]))):
        print("Yes")
    else:
        print("No")
        

# 5th method by using deque and while
from collections import deque
for t in range(int(input())):
    m, b = int(input()), deque(map(int, input().split(" ")))
    o = deque()
    while b:
        o.appendleft(b.popleft()) if b[0] > b[-1] else o.appendleft(b.pop()) 
        if len(o) > 1 and o[0] > o[1]:
            print("No")
            break
    else:
        print("Yes")

        
# 6th method
from collections import deque
def piling(d):
    while d:
        large = None
        if d[-1] > d[0]:
            large = d.pop()
        else:
            large = d.popleft()
            
        if len(d) == 0:
            return "Yes"
        
        if d[-1] > large or d[0] > large:
            return "No"
for i in range(int(input())):
    no_of_cubes = int(input())
    d = deque(map(int, input().split()))
    print(piling(d))


# 7th method
from collections import deque
T = int(input())
for _ in range(T):
    n = int(input())
    sideLengths = list(map(int, input().split()))
    d = deque(sideLengths)
    sup = max(d[0], d[-1])
    sup_temp = sup
    while len(d) != 0 and sup == sup_temp:
        if d[0] > d[-1]:
            sup = d.popleft()
        else:
            sup = d.pop()
        if sup <= sup_temp:
            sup_temp = sup
    if len(d) == 0:
        print('Yes')
    else:
        print('No')
        
# 8th method
for x in range(int(input())):
    n=int(input())
    l1= list(map(int, input().split()))
    m=max(l1)
    for x in range(len(l1)+1):
        if len(l1)==0:
            print("Yes")
        elif m<=l1[0]:
            l1.remove(l1[-1])
            #print(l1,"f")
        elif m<=l1[-1]:
            l1.remove(l1[0])
            #print(l1)
        else:
            print("No")
            break

# 9th method
from collections import deque
for _ in range(int(input())):
    _ = int(input())
    d = deque(map(int, input().split()))
    a = max(d[0], d[-1])
    for _ in range(len(d)):
        if d[0] <= d[-1] <= a:
            a = d.pop()
        elif d[-1] <= d[0] <= a:
            a = d.popleft()
        else:
            break
    print('Yes' if len(d) == 0 else 'No')


# 10th method
T = int(input())
def check(data):
    while len(data) >= 3:
        if data[0] < data[1] and data[-1] < data[-2]:
            return "No"
        data = data[1:-1]
    return "Yes"
for _ in range(T):
    n = int(input())
    blocks = list(map(int, input().split()))
    print(check(blocks))
    
# 11th method
tests = int(input())
for _ in range(tests):
    n , blocks = int(input()) , list(map(int, input().split(' ')))
    last = pow(2,32)
    for k in range(n):
        if(blocks[0] >= blocks[-1] and blocks[0] <= last):
            last = blocks.pop(0)
        elif(blocks[-1] <= last):
            last = blocks.pop(-1)     
        else:
            break
    print('No' if len(blocks) else 'Yes')
    
# 12th method
T = int(input())
for i in range(T):
    n = int(input())
    l = list(map(int, input().split()))
    min_val = min(l)
    idx = l.index(min_val)
    t1 = l.copy()
    p1, p2 = t1[idx:], t1[:idx]
    p1.sort()
    p2.sort(reverse=True)
    if (p1 == l[idx:])*(p2 == l[:idx]):
        print('Yes')
    else:
        print('No')

# 13th method
for _ in range(int(input())):
    n, cubes = int(input()), list(map(int, input().split()))    
    A, B = cubes[0:cubes.index(min(cubes))], cubes[cubes.index(min(cubes)):]   
    print('Yes' if sorted(A)[::-1] == A and sorted(B) == B else 'No')

    
# 14th method
for t in range(input()):
    lst = map(int, input().split())
    l = len(lst)
    i = 0
    while i < l - 1 and lst[i] >= lst[i+1]:
        i += 1
    while i < l - 1 and lst[i] <= lst[i+1]:
        i += 1
    print("Yes" if i == l - 1 else "No")


# 15th method
from collections import deque
for _ in range(int(input())):  
    _, queue =input(), deque(map(int, input().split()))    
    for cube in reversed(sorted(queue)):
        if queue[-1] == cube: queue.pop()
        elif queue[0] == cube: queue.popleft()
        else:
            print('No')
            break
    else:
        print('Yes')

    
# 16th method
t=int(input())
while(t!=0):
    t-=1
    n=int(input())
    l=list(map(int,input().split()))[:n]
    if(l[0]==max(l) or l[n-1]==max(l)):print("Yes")
    else: print("No")


####################################################################
#################################################### (Date and Time)
####################################################################

##########################################################
################### Question #* Calendar Module
"""
The calendar module allows you to output calendars and provides additional useful functions for them.
class calendar.TextCalendar([firstweekday])
This class can be used to generate plain text calendars.
"""
import calendar
print(calendar.TextCalendar(firstweekday=6).formatyear(2015))


# Create a calendar object for the current month with Monday as the first day of the week (0 represents Monday).
cal = calendar.Calendar(firstweekday=0)

# Get the weeks of the month as a list of lists, where each inner list represents a week.
# Replace 2023 and 7 with the desired year and month.
weeks = cal.monthdayscalendar(2023, 7)

# Iterate through each week to get the weekdays.
for week in weeks:
    for day in week:
        if day == 0:
            # Print two spaces for days outside the current month.
            print("  ", end="")
        else:
            # Print the day with two spaces padding.
            print(f"{day:2}", end=" ")
    print()  # Move to the next line after each week.


# 1st method
user_input = list(map(int, input().split()))
day = int(user_input[1])
month = int(user_input[0])
year = int(user_input[2])
week_day = calendar.weekday(year, month, day)
print(calendar.day_name[week_day].upper())

# 2nd method
month, day, year = list(map(int, input().split()))
week_day = calendar.weekday(year, month, day)
print(calendar.day_name[week_day].upper())

"""
we can access items from a map object in Python.
The map() function returns an iterator that applies a given function to all the items in an input iterable (e.g., a list)
and generates the results one by one as you iterate through it. we can access items from a map object in Python
"""

""" iterator is an object in Python that allows you to iterate over a sequence of elements one by one.
It's a type of object that implements two methods: __iter__() and __next__().
The __iter__() method returns the iterator object itself,
and the __next__() method returns the next element in the sequence.
"""
# Note:-Iterators are used extensively in Python, and many built-in types, like lists, strings, and dictionaries, are iterable.
# example
my_list = [1, 2, 3, 4, 5]
my_iterator = iter(my_list)
#  my_iterator is an iterator that allows you to access elements from my_list one by one using the next() function or by using it in a loop.

"""
* An iterator in Python is not a function; it is an object. that allows you to iterate over a sequence of elements one by one, enabling you to access each element sequentially.
* In Python, iterators implement two methods: __iter__() and __next__(). These methods define the iterator protocol:
* 1.The __iter__() method returns the iterator object itself. It is called when you use the iter() function on an iterable object, and it is used to obtain the iterator from the iterable.
* 2.The __next__() method returns the next element in the sequence. It is called when you use the next() function on the iterator, and it raises the StopIteration exception when there are no more elements to return.
* Here's an example of how to create and use an iterator in Python:
"""

my_list = [1, 2, 3, 4, 5]

# Create an iterator from the list using the iter() function.
my_iterator = iter(my_list)

# Use the next() function to access elements from the iterator one by one.
print(next(my_iterator))  # Output: 1
print(next(my_iterator))  # Output: 2
print(next(my_iterator))  # Output: 3
# ... and so on.
print("remaining")
# You can also use a for loop to iterate over the elements using the iterator.
for element in my_iterator:
    print(element)  # Output: 4, 5

"""
*In this example, my_iterator is an iterator object created from the list my_list.
*The next() function is used to access elements one by one until there are no more elements,
*at which point it raises the StopIteration exception.
"""



##################################################################
####################### Question #* (Time Delta)

from datetime import datetime
p = dir(datetime)
print(p)
"""
['__add__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__',
'__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__',
'__le__', '__lt__', '__ne__', '__new__', '__radd__', '__reduce__', '__reduce_ex__', '__repr__',
'__rsub__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', 'astimezone', 
'combine', 'ctime', 'date', 'day', 'dst', 'fold', 'fromisocalendar', 'fromisoformat', 'fromordinal',
'fromtimestamp', 'hour', 'isocalendar', 'isoformat', 'isoweekday', 'max', 'microsecond', 'min',
'minute', 'month', 'now', 'replace', 'resolution', 'second', 'strftime', 'strptime', 'time',
'timestamp', 'timetuple', 'timetz', 'today', 'toordinal', 
'tzinfo', 'tzname', 'utcfromtimestamp', 'utcnow', 'utcoffset', 'utctimetuple', 'weekday', 'year']

"""
"""
strptime stands for "string parse time," and it's used to parse a string representing a date and time
and convert it into a datetime object.
General Sytax :=
                datetime_object = datetime.strptime(date_string, format_string)
#* date_string: The string containing the date and time information you want to parse.
#* format_string: A string specifying the expected format of the date_string.
example:-
"""
from datetime import datetime

date_string = "2023-09-04 05:09:08"
format_string = "%Y-%m-%d %H:%M:%S"
datetime_object = datetime.strptime(date_string, format_string)
print(datetime_object)

#2nd 
def time_delta(t1, t2):
    format_string = "%a %d %b %Y %H:%M:%S %z" 
    dt1 = datetime.strptime(t1, format_string)
    dt2 = datetime.strptime(t2, format_string) 
    diff = abs(dt1 - dt2)
    return str(int(diff.total_seconds()))

t1 = 'Sun 10 May 2015 13:54:36 -0700'
t2 = 'Sun 10 May 2015 13:54:36 -0000'


"""
strftime stands for "string format time." It is a method available in Python's datetime module that allows you
to format datetime objects into human-readable date and time strings
Genral syntax :=
                formatted_string = datetime_object.strftime(format_string)
#* datetime_object: The datetime object that you want to format.
#* format_string: A string that specifies the desired format for the output.
example:-
"""
from datetime import datetime

current_datetime = datetime.now()
formatted_string = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_string)


# *Question Answer
import time
from datetime import datetime, timedelta
def time_delta(t1, t2):
    format_string = "%a %d %b %Y %H:%M:%S %z" 
    dt1 = datetime.strptime(t1, format_string)
    dt2 = datetime.strptime(t2, format_string) 
    diff = abs(dt1 - dt2)
    return str(int(diff.total_seconds()))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())
    for t_itr in range(t):
        t1 = input()
        t2 = input()
        delta = time_delta(t1, t2)
        fptr.write(delta + '\n')
    fptr.close()


# 2nd method using dateutil module
import time
from datetime import datetime, timedelta
from dateutil import parser
for _ in range(int(input())):
    d1 = parser.parse(input().strip())
    d2 = parser.parse(input().strip())
    print(abs(int((d2-d1).total_seconds())))


# just as get method from these module
import dateutil
p = dir(dateutil)
print(p)

from dateutil import parser
p = dir(parser)
print(p)


####################################################################
#################################################### (Date and Time)
####################################################################

##################################################################
######################################## Question #* Exceptions
# Key concept
# * (Errors detected during execution are called exceptions.)
# * Buffer structures (or simply “buffers”) are useful as a way to expose the binary data from another object to the Python programmer.

# Example:-
"""
#* ZeroDivisionError:- This error is raised when the second argument of a division or modulo operation is zero.
a = '1'
b = '0'
print(int(a) / int(b))
# >>> ZeroDivisionError: integer division or modulo by zero

#* ValueError:- This error is raised when a built-in operation or function receives an argument that has the right type but an inappropriate value.
a = '1'
b = '#'
print(int(a) / int(b))
>>> ValueError: invalid literal for int() with base 10: '#'

#* Handling Exceptions:- 
The statements try and except can be used to handle selected exceptions.
A try statement may have more than one except clause to specify handlers for different exceptions.

#Code
try:
    print 1/0
except ZeroDivisionError as e:
    print("Error Code:", e)
Output :-Error Code: integer division or modulo by zero

"""

n = int(input())
for i in range(n):
    try:
        M, N = map(int, input().split())
        print(M//N)
    except (ZeroDivisionError, ValueError) as error:
        print('Error Code:', error)
# https://docs.python.org/3/library/exceptions.html


####################################################################
############################################ #* Incorrect Regex
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
test_case = int(input())
for _ in range(test_case):
    my_string = input()
    try:
        re.compile(my_string)
        print('True')
    except re.error:
        print(False)


####################################################################
###################################################### (classes)
####################################################################

####################################################################
########################### #* (Class 2 - Find the Torsional Angle)
import math
class Points(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, no):
        return Points(self.x - no.x, self.y - no.y, self.z - no.z)

    def dot(self, no): # a.b = x1x2 + y1y2 + z1z2
        return self.x*no.x + self.y*no.y + self.z*no.z
    
    def cross(self, no): # a*b = i(a2b3 - a3b2) + j(a3b1 - a1b3) + k(a1b2 - a2b1)
        return Points(self.y*no.z - self.z*no.y, self.z*no.x - self.x*no.z, self.x*no.y - self.y*no.x)
        
    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)

if __name__ == '__main__':
    points = list()
    for i in range(4):
        a = list(map(float, input().split()))
        points.append(a)

    a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))
    print("%.2f" % math.degrees(angle))
    
# 2nd method just using map and operater
import math
from operator import sub, mul

class Points(object):
    def __init__(self, x, y, z):
        self.co = (x, y, z)

    def __sub__(self, no):
        return Points(*map(sub, self.co, no.co))

    def dot(self, no):
        return sum(map(mul, self.co, no.co))

    def cross(self, no):
        x1, x2, x3 = self.co
        y1, y2, y3 = no.co
        return Points(x2*y3-x3*y2, x3*y1-x1*y3, x1*y2-x2*y1)
    
    def absolute(self):
        # return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)
        return self.dot(self)**.5
    
# 3rd method
class Points(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, no):
        vector1 = [self.x, self.y, self.z]
        vector2 = [no.x, no.y, no.z]
        return Points(*[x1 - x2 for x1, x2 in zip(vector1, vector2)])

    def dot(self, no):
        vector1 = [self.x, self.y, self.z]
        vector2 = [no.x, no.y, no.z]
        return sum(x1 * x2 for x1, x2 in zip(vector1, vector2))
    
    def cross(self, no):
        vector1 = [self.x, self.y, self.z]
        vector2 = [no.x, no.y, no.z]
        x = (vector1[1] * vector2[2]) - (vector1[2] * vector2[1])
        y = (vector1[2] * vector2[0]) - (vector1[0] * vector2[2])
        z = (vector1[0] * vector2[1]) - (vector1[1] * vector2[0])
        return Points(x, y, z)
        
    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)
    
####################################################################
######################## #* (Classes: Dealing with Complex Numbers)
# 1st method
import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        
    def __add__(self, no):
        rl = self.real + no.real
        img = self.imaginary + no.imaginary
        return Complex(rl, img)
    
    def __sub__(self, no):
        rl = self.real - no.real
        img = self.imaginary - no.imaginary
        return Complex(rl, img)
        
    def __mul__(self, no):
        new_real = (self.real * no.real) - (self.imaginary * no.imaginary)
        new_complex = (self.real * no.imaginary) + (no.real * self.imaginary)
        return Complex(new_real,new_complex)
        
    def __truediv__(self, no):
        c = Complex(((self.real * no.real) + (self.imaginary * no.imaginary)) / (no.real ** 2 + no.imaginary ** 2), ((self.imaginary * no.real) - (self.real * no.imaginary)) / (no.imaginary ** 2 + no.real ** 2))
        return c
    def mod(self):
        return Complex(math.sqrt(self.real**2 + self.imaginary**2),0)


    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')


# 2nd method
class Complex(object):
    def __init__(self, real, imaginary):
        self.complex = complex(real, imaginary)
        self.real = self.complex.real
        self.imaginary = self.complex.imag

    def __add__(self, no):
        res = self.complex + complex(no.real, no.imaginary)

        return Complex(res.real, res.imag)

    def __sub__(self, no):
        res = self.complex - complex(no.real, no.imaginary)

        return Complex(res.real, res.imag)

    def __mul__(self, no):
        res = self.complex * complex(no.real, no.imaginary)

        return Complex(res.real, res.imag)

    def __truediv__(self, no):
        res = self.complex / complex(no.real, no.imaginary)

        return Complex(res.real, res.imag)

    def mod(self):
        res = abs(self.complex)

        return Complex(res.real, res.imag)




####################################################################
######################################################## (Built-Ins)
####################################################################

####################################################################
################################################# #* Zipped!
# Key concept
"""
#* zip([iterable, ...]) :-
                            This function returns a list of tuples. The th tuple contains the th element from each of the argument
sequences or iterables.If the argument sequences are of unequal lengths,then the returned list is truncated to the length of the shortest argument sequence.
"""
#Example
print(zip([1,2,3,4,5,6],'Hacker'))
# Output: [(1, 'H'), (2, 'a'), (3, 'c'), (4, 'k'), (5, 'e'), (6, 'r')]
print(zip([1,2,3,4,5,6],[0,9,8,7,6,5,4,3,2,1]))
# Output: [(1, 0), (2, 9), (3, 8), (4, 7), (5, 6), (6, 5)]
A = [1,2,3]
B = [6,5,4]
C = [7,8,9]
X = [A] + [B] + [C]
print(zip(*X))
# Output: [(1, 6, 7), (2, 5, 8), (3, 4, 9)]


# Question answer
num_of_student, num_of_subject = map(int, input().split())
my_list = []
for i in range(num_of_subject):
    marks = list(map(float, input().split()))
    my_list.append(marks)
z = list(zip(*my_list))
for j in z:
    average = sum(j) / num_of_subject
    print(round(average, 1))
    
# we can short this code even more 
#OR
num_of_student, num_of_subject = map(int, input().split())
marks = [list(map(float, input().split())) for _ in range(num_of_subject)]
avg = [round(sum(j)/num_of_subject, 2) for j in list(zip(*marks))]
print(*avg, sep='\n')


# faces err due to already assumes there are always exactly three subjects for each student.
num_of_student, num_of_subject = map(int, input().split())
my_list = []
for i in range(num_of_subject):
    marks = list(map(float, input().split()))
    my_list.append(marks)
a = my_list[0]
b = my_list[1]
c = my_list[2]
z = [a] + [b] + [c]
k = list(zip(*z))
for j in k:
    avg = sum(j)/num_of_subject
    print(round(avg,2)) 
    
    
# 2nd method simple else if
num_of_student,num_of_subject=map(int,input().split())
my_list=[]
for i in range(num_of_subject):
    marks_l=list(map(float,input().split()))
    my_list.append(marks_l)

for j in range(num_of_student):
    total=0
    for item in my_list:
        total+=item[j]
    print(total/num_of_subject)



####################################################################
############################################### #* input()
# 1st method using eval function
m, k = map(int, input().split())
p = input()
new_p =  p.replace('x', str(m))
if eval(new_p) == k:
    print(True)
else:
    print(False)
# Or simply directly print evaluting
x,y = map(int,input().split())
print(eval(input().replace('x',str(x)))==y)


# 2nd method Using exec built-in function

"""
exec() function is used for the dynamic execution of Python programs
The exec() function executes the specified Python code.
The exec() function accepts large blocks of code, unlike the eval() function which only accepts a single expression
Genreal syntax: 
                exec(object, globals, locals)

object	A String, or a code object
globals	Optional. A dictionary containing global parameters
locals	Optional. A dictionary containing local parameters
"""
# Example:-
# 1st
x = 5
expression = x**7 + x + 1
result = exec('expression')
print(result)
# output: None
# why? bcz exec() does not return a value. Instead, it executes a Python statement.

# 2nd
x = 5
expression = x**7 + x + 1
exec(f"ans = {expression}")
print(ans) #output : 78131

#
x = 1
expression = x**3 + x**2 + x + 1
exec(f"result = {expression}")
print("Result:", result) #output Result: 4

#Questions answer
x, k = map(int, input().split())
expression = input()
exec(f"result = {expression}")
if result == k:
    print('True')
else:
    print('False')

# Or shorter version 
x, k = map(int, input().split())
exec('result =' + input())
print('True') if result == k else print('False')


### just for knowing
user_input : str = input('You: ')
print(eval(user_input))
# Is same as
user_input = input('You: ')
result = eval(user_input)
print(result)


####################################################################
############################################ #* Python Evaluation

"""
The eval() expression is a very powerful built-in function of Python. 
It helps in evaluating an expression.The expression can be a Python statement, or a code object.
"""
# Note: eval() can also be used to work with Python keywords or defined functions and variables. These would normally be stored as strings.


# Expression VS Statement:
#* Expressions produce values, while statements perform actions or control the flow of a program. Understanding the distinction between the two is crucial in Python programming, as it affects how you structure your code and what you can do with different pieces of code.

"""
Expression: -
            An expression is a piece of code that produces a value when it is evaluated or executed.
Expressions can be used as part of larger expressions, as arguments to functions, or assigned to variables.
#* Or An expression is a combination of variables, operators, and values that evaluates to a single value.For example, the expression 1 + 2 evaluates to the value 3.

Statement:-
            A statement is a complete line of code that performs an action. It doesn't necessarily produce a value.
Statements are used to control the flow of a program, define functions, create classes, and perform various operations.
#* Or A statement is a command that the Python interpreter executes. Statements can be used to create variables, assign values to variables, make decisions, and perform actions. For example, the statement x = 10 creates a variable named x and assigns it the value 10.
"""

# Expression Example:
result = 2 * (3 + 4)  # This is an expression that calculates a value (14) and assigns it to 'result'.


# Statement Example:
if x > 5:  # This is a statement (conditional) that controls the flow of the program.
    print("x is greater than 5")


# eval: Functions
"""
The eval() function evaluates the specified expression, if the expression is a legal Python statement,
it will be executed.

syntax: -
#* eval(expression, globals, locals)
expression:	A String, that will be evaluated as Python code
globals	(Optional). A dictionary containing global parameters
locals (Optional). A dictionary containing local parameters
"""

print(eval("9 + 5")) #Output: 14

x = 2
print(eval("x + 3")) #output: 5
type(eval("len"))
# output: <type 'builtin_function_or_method'>


# Question answers
# 1st method by using eval()
user_input = input()
eval(user_input)

# 2nd method by using exec()
user_input = input()
exec(user_input)

#################################################################################
################################################## (Any or All)
# Slicing is typically used with sequences like strings, lists, or tuples, not with integers. if want change dtype
# Question #*PythonBuilt-Ins Any or All
# * any() method
""" 
    The any() function in Python is a built-in function that takes an iterable (such as a list, tuple, or set)
    as its argument and returns True if at least one element in the iterable is truthy,
    and False if all elements are falsy or the iterable is empty.
    
    This expression returns True if any element of the iterable is true.
    If the iterable is empty, it will return False.
"""

my_int = 41
print(str(my_int)[::-1])

# Example
# Here's the syntax for the any() function:
# *    any(iterable)
# * The iterable parameter is the sequence or collection of values that you want to check for truthiness.
def any(iterable):
    for i in iterable:
        if iterable:
            return True
    return False

#Or
def any(iterable):
    for i in iterable:
        return True
    return False
""" But if you concerning about performance then use 1st line "if iterable:" checks if the iterable is empty.
If it is, the function returns False immediately, without even iterating over the iterable.
This is a good optimization, because it can prevent unnecessary looping if the iterable is empty.
second one does not have this optimization. It will always iterate over the iterable, even if it is empty.

"""

# Example 1;-
numbers = [0, 1, 2, 3, 4]
result = any(numbers)
print(result)  # Output: True (at least one element is truthy)


# Example 2;-
numbers = [0, False, None, '', [], {}]
result = all(numbers)
print(result)  # Output: False (all elements are falsy)

# Example 3;-
names = ['Alice', 'Bob', '']
result = any(names)
print(result)  # Output: True (at least one element is truthy)

# Example 4;-
empty_list = []
result = any(empty_list)
print(result)  # Output: False (empty iterable)

# The any() function is often used when you want to check if at least one element in an iterable
# * -satisfies a certain condition or is considered truthy.

# ex:-
any([1 > 0, 1 == 0, 1 < 0])
# >>> True
any([1 < 0, 2 < 1, 3 < 2])
# >>> False

# * all() method
"""
This expression returns True if all of the elements of the iterable are true.
If the iterable is empty, it will return True.
"""

all(['a' < 'b', 'b' < 'c'])
# >>> True
all(['a' < 'b', 'c' < 'b'])
# >>> False

"""
The all() and any() functions in Python are both built-in functions used to evaluate the truthiness of elements in an iterable.
The main differences between all() and any() are as follows:

all(): Returns True if all elements in the iterable are truthy. If the iterable is empty, it returns True.
any(): Returns True if at least one element in the iterable is truthy. If the iterable is empty, it returns False.
Conditions:


all(): Checks if all elements in the iterable are truthy. If any element is falsy, it immediately returns False. It stops evaluating the remaining elements as soon as it encounters the first falsy element.
any(): Checks if at least one element in the iterable is truthy. It stops evaluating the remaining elements as soon as it encounters the first truthy element.
Empty Iterable:


all(): If the iterable is empty, it returns True because there are no falsy elements to evaluate.
any(): If the iterable is empty, it returns False because there are no truthy elements to evaluate.
Here are some examples to further illustrate the differences:
"""

numbers = [1, 2, 3, 4, 5]
result_all = all(numbers)
result_any = any(numbers)
print(result_all)  # Output: True
print(result_any)  # Output: True

numbers = [0, 1, 2, 3, 4]
result_all = all(numbers)
result_any = any(numbers)
print(result_all)  # Output: False
print(result_any)  # Output: True

names = ['Alice', 'Bob', '']
result_all = all(names)
result_any = any(names)
print(result_all)  # Output: False
print(result_any)  # Output: True

empty_list = []
result_all = all(empty_list)
result_any = any(empty_list)
print(result_all)  # Output: True
print(result_any)  # Output: False

# In the examples above, the all() function returns True
# only when all elements in the iterable are truthy. On the other hand,
# the any() function returns True if at least one element is truthy.


# *Note :- Overall, all() is useful when you need to ensure that all elements in an iterable satisfy a condition,
# *                 while any() is helpful when you only need to check if at least one element satisfies a condition.


# *arg
N, *arg = input().split()
# assign the first value of the split string to the variable N, and the remaining values to the variable arg
# * The *arg syntax is used to capture any number of remaining values into a list.
# For example, if the user enters "1 2 3 4 5", the value of N will be "1", and the value of arg will be a list containing ["2", "3", "4", "5"].

# we can even directly convert to integer by using int funxn
N, *arg = map(int, input().split())  # Now N = 1 and arg = [2,3,4,5]


# 1st method
st = int(input())
ii = input().split().index("MARKS")
print(sum(int(input().split()[ii]) for i in range(st)) / st)


# Question Answer*
# 1st method using simple if else
total_num = int(input())
num_list = map(int, input().split())
all_number = True 
any_palindrome = False  

for num in num_list:
    if num <= 0:
        all_number = False
    if str(num) == str(num)[::-1]:
        any_palindrome = True

if all_number and any_palindrome:
    condition = True
else:
    condition = False
print(condition)

# 2nd method
total_num, num_list, y, z = input(), list(map(int, input().split())), True, False
p, l = [ z for x in num_list if x < 0 ], [ y if x > 0 and str.join('', str(x)) == str.join('', reversed(str(x))) else z for x in num_list]
[print(z) if p else print(any(l))]

# 3rd method using all and any
total_num =  int(input())
num_list = input().split()
positive = all(int(i)>0 for i in num_list)
palindromic = any(i == i[::-1] for i in num_list)
if positive and palindromic:
    print("True")
else:
    print("False")
    
# Or we can make even shorter this code 
total_num = int(input())
num_list = input().split()
print(all((all(int(num)>0 for num in num_list),any(k == k[::-1] for k in num_list))))

# Or
total_num, num_list = input(), input().split()
print(all(all(int(x) > 0 for x in num_list), any(k == k[::-1])))

# or
print(input() and (lambda ns: all(int(n) > 0 for n in ns) and any(n == n[::-1] for n in ns))(input().split()))



###########################################################################
###################################### #* Question Athlete Sort
# 1st method using sorted method
if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    k = int(input().strip())
    sorted_arr = sorted(arr, key=lambda x: x[k])
    for k in sorted_arr:
        print(*k)
        
# 2nd methos using inplace sort method
#!/bin/python3
if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    k = int(input().strip())
    arr.sort(key=lambda x:x[k])
    for k in arr:
        print(*k)
        

m = 'l'
print(dir(m))
###########################################################
############################# Question #*ginortS
# 1st method do all by initializing list for each one
my_string = input()
lower_case = []
upper_case = []
even_digit = []
odd_digit = []
for k in my_string:
    if k.isupper():
        upper_case.append(k)
    elif k.islower():
        lower_case.append(k)
    elif k.isdigit():
        if int(k)%2 == 0:
            even_digit.append(k)
        else:
            odd_digit.append(k)
lower_case.sort()
upper_case.sort()
odd_digit.sort()
even_digit.sort()
new_string = lower_case+upper_case+odd_digit+even_digit
final_string = "".join(x for x in new_string)
print(final_string)


# 2nd method using sorted and list comprhension method
my_string = input()
lower_case = sorted([char for char in my_string if char.islower()])
upper_case = sorted([char for char in my_string if char.isupper()])
odd_digit = sorted([char for char in my_string if char.isdigit() and int(char) % 2 == 1])
even_digit = sorted([char for char in my_string if char.isdigit() and int(char) % 2 == 0])
final_string = ''.join(lower_case + upper_case + odd_digit + even_digit)
print(final_string)


# 3rd method defing custom function
s = input().strip()
def custom_sort_key(char):
    if char.islower():
        return (1,char)
    elif char.isupper():
        return(2,char)
    elif char.isdigit():
        if int(char) % 2 == 1:
            return (3,char)
        else:
            return (4,char)
sorted_string = "".join(sorted(s, key = custom_sort_key))
print(sorted_string)

# or
def custom_sort_key(char):
    if char.islower(): return 0
    elif char.isupper(): return 1
    elif int(char) % 2: return 2
    else: return 3

s = list(input().strip())
print(''.join(sorted(sorted(s), key=custom_sort_key)))


# 4th method Using regex
import re
s = input()
char_list = list(s)
char_list.sort()
temp_str = str(char_list)
lower = re.findall('[a-z]+', temp_str)
upper = re.findall('[A-Z]+', temp_str)
odds = re.findall('[13579]+',temp_str)
evens = re.findall('[02468]+',temp_str)
temp_array = lower + upper + odds + evens
print("".join(temp_array))
        
# Or 
import re
N = input()
lc = "".join(sorted(re.findall(r"[a-z]",N)))
uc = "".join(sorted(re.findall(r"[A-Z]",N)))
o  = "".join(sorted(re.findall(r"[1,3,5,7,9]",N)))
e  = "".join(sorted(re.findall(r"[0,2,4,6,8]",N)))
print(lc+uc+o+e)

# 5th method using lambda

print(*sorted(input(), key=lambda x:(x.isdigit(), x.isupper(), x in "02468", x)), sep="")


####################################################################
############################################## (Python Functionals)
####################################################################

##############################################################################
####################### Question #* Validating Email Addresses With a Filter
# 1st method
cube = lambda x: x**3
def fibonacci(n):
    fibo=[]
    a=0
    b=1
    c=0
    for _ in range(n):
        fibo.append(c)
        a=b
        b=c
        c=a+b
    return fibo
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))


# 2nd method using generator
cube = lambda x: x ** 3 # complete the lambda function 
def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
    
# 3rd method using look
cube = lambda x: x ** 3 # complete the lambda function 
def fibonacci(n):
    fib = list()
    x, y = 0, 1
    for i in range(n):
        fib.append(x)
        x, y = y, x + y
    return fib
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))


###########################################################
############################# Question #*Reduce Function
from fractions import Fraction
from functools import reduce
def product(fracs):
    t = reduce(lambda x,y:x*y, fracs)
    return t.numerator, t.denominator
if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)


################################################################
###### Question #*Validating Email Addresses With a Filter
def fun(s):
    # return True if s is a valid email, else return False
    import re
    pattern = r"^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$"
    # return re.match(pattern, s)
    # pattern = r"\S+@\S+\.\S{1,3}"
    return re.match(pattern, s)
def filter_mail(emails):
    return list(filter(fun, emails))
if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())
filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)



####################################################################
############################################### (Regex and Parsing)
####################################################################
"""
#* A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
#* for pattern testing:- https://regex101.com/

RegEx can be used to check if a string contains the specified search pattern.
RegEx Module:- Python has a built-in package called re used to work with Regular Expressions.
"""

"""
Import the re Module:
To use regular expressions in Python, you need to import the re module.
#* import re

Basic Patterns:
#* .(dot): Matches any character except a newline.
#* *: Matches 0 or more repetitions of the preceding pattern.
#* +: Matches 1 or more repetitions of the preceding pattern.
#* ?: Matches 0 or 1 repetition of the preceding pattern.
#* \: Escape special characters, like . or *.

Character Classes:
#* [abc]: Matches any character a, b, or c.
#* [^abc]: Matches any character except a, b, or c.
#* [a-z]: Matches any lowercase letter.
#* [A-Z]: Matches any uppercase letter.
#* [0-9]: Matches any digit.

Anchors:
#* ^: Matches the start of a string.
#* $: Matches the end of a string.

Quantifiers:
#* {n}: Matches exactly n repetitions of the preceding pattern.
#* {n,}: Matches n or more repetitions of the preceding pattern.
#* {n, m}: Matches between n and m repetitions of the preceding pattern.


Special Sequences:
#* \d: Matches any digit (equivalent to [0-9]).
#* \D: Matches any non-digit.
#* \w: Matches any word character (letters, digits, or underscores).
#* \W: Matches any non-word character.
#* \s: Matches any whitespace character.
#* \S: Matches any non-whitespace character.


Grouping and Capturing:
#* ( ): Create a capturing group.
#* (?: ): Create a non-capturing group.
#* \1, \2, etc.: Refer to captured groups in the regex.


Modifiers:
#* re.IGNORECASE or re.I: Perform case-insensitive matching.
#* re.MULTILINE or re.M: Match at the start or end of each line.
#* re.DOTALL or re.S: Match all characters, including newlines, with ..


Methods in re Module:
#* re.search(pattern, string): Search for a pattern anywhere in the string.
#* re.match(pattern, string): Match the pattern only at the start of the string.
#* re.findall(pattern, string): Find all occurrences of the pattern in the string.
#* re.finditer(pattern, string): Find all occurrences as an iterator.
#* re.sub(pattern, replacement, string): Replace pattern matches with the replacement string.
#* re.compile(pattern): Pre-compile a regex pattern for reuse.
#* re.split(pattern, string, maxsplit=0, flags=0): Returns a list where the string has been split at each match

# Positive Lookbehind Assertion ('(?<= ... )') Syntax: (?<= ... ): 
#* Example: (?<=b)a matches "a" only if it is preceded by "b," but "b" is not included in the match.

# Positive Lookahead Assertion ('(?= ... )') Syntax: (?= ... ): 
#* Example: a(?=b) matches "a" only if it is followed by "b," but "b" is not included in the match.

# Negative Lookbehind Assertion ('(?<! ... )'):
#* pattern = r'(?<!b)\d'  # Match a digit (\d) that is not preceded by 'b'

# Negative Lookahead Assertion ('(?! ... )'):
#* pattern = r'\d(?!a)'  # Match a digit (\d) that is not followed by 'a'

# Word Boundaries ('\b ... \b'):
#* pattern = r'\bword\b'  # Match the word 'word' as a whole word

# Start of String ('^') and End of String ('$'):
#* pattern = r'^start'    # Match 'start' at the beginning of a string
#* pattern = r'end$'      # Match 'end' at the end of a string

# parentheses ():
#* Grouping: Parentheses are used to group together parts of a regular expression so that you can apply quantifiers,
#*-  alternation, or other modifiers to that group as a whole.
For example:
(abc)+ matches one or more repetitions of the sequence "abc."
(x|y) matches either "x" or "y."

# Capturing () :
#* Parentheses are also used to capture portions of the text that match the grouped expression.
#*-  When you use parentheses, the text that matches the grouped part is stored in memory and can be accessed later.

For example:
If you have the pattern (\d{2})-(\d{2})-(\d{4}), it captures a date in the format "dd-mm-yyyy"
into three separate capture groups: day, month, and year.
You can access the captured groups using methods like re.match.group(), re.search.group(), or re.findall() in Python's re module.
"""


import re
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(x) # Output: <re.Match object; span=(0, 17), match='The rain in Spain'>


################## regex important functions
"""
RegEx Functions:-The re module offers a set of functions that allows us to search a string for a match
# * Function	Description
# * findall	    Returns a list containing all matches
# * search	    Returns a Match object if there is a match anywhere in the string
# * split       Returns a list where the string has been split at each match
# * sub	        Replaces one or many matches with a string
"""

################## regex Meta chracters
"""
Metacharacters are characters with a special meaning:-
Character	Description	                                                            Example	
[]	     A set of characters	                                                    "[a-m]"	
\	     Signals a special sequence (can also be used to escape special characters)	"\d"	
.	     Any character (except newline character)	                                "he..o"	
^	     Starts with	                                                            "^hello"	
$	     Ends with	                                                                "planet$"	
*	     Zero or more occurrences	                                                "he.*o"	
+	     One or more occurrences	                                                "he.+o"	
?	     Zero or one occurrences	                                                "he.?o"	
{}	     Exactly the specified number of occurrences	                            "he.{2}o"	
|	     Either or	                                                                "falls|stays"	
()	     Capture and group	 
"""
####################### Special Sequences
# A special sequence is a \ followed by one of the characters in the list below, and has a special meaning:
"""
\A:	Returns a match if the specified characters are at the beginning of the string	"\AThe"
\d:	Returns a match where the string contains digits (numbers from 0-9)	            "\d"	
\D:	Returns a match where the string DOES NOT contain digits	                    "\D"	
\s:	Returns a match where the string contains a white space character	            "\s"	
\S:	Returns a match where the string DOES NOT contain a white space character	    "\S"	
\w:	Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)	"\w"	
\W:	Returns a match where the string DOES NOT contain any word characters	        "\W"	
\Z:	Returns a match if the specified characters are at the end of the string	    "Spain\Z"	

\b (Word Boundary): \b is a word boundary anchor. It matches a position where a word starts or ends.
\B (Non-Word Boundary): \B is the complement of \b. It matches a position where a word does not start or end.
Both does not consume any characters
"""

# Unicode is a character encoding standard that represents text using a set of 16-bit code units. It can be used to represent any character in any language, including emojis, mathematical symbols, and technical symbols.
# Bytecode is a low-level representation of a program that can be executed by a virtual machine. It is generated by a compiler from the source code of a high-level programming language. Bytecode is specific to the programming language that the program is written in.


######################################################################
###########################################  #* Re.split()
regex_pattern = r"[,.]"	# Do not delete 'r'.
import re
print("\n".join(re.split(regex_pattern, input())))


########################################################################
#############################  #* (Group(), Groups() & Groupdict())
# group(): A group() expression returns one or more subgroups of the match.
# Example:-
import re
m = re.match(r'(\w+)@(\w+)\.(\w+)','username@hackerrank.com')
m.group(0)       # Return the entire match 
# >>> Output: 'username@hackerrank.com'

import re
m = re.match(r'\w+@\w+\.\w+','username@hackerrank.com')
print(m.group(0))
# >>> Output: 'username@hackerrank.com'

import re
m = re.match(r'\w+@\w+\.\w+','username@hackerrank.com')
print(m.group(1))
#>>> Output: IndexError: no such group (bcz we haven't grouped)

import re
m = re.match(r'(\w+)@(\w+)\.(\w+)','username@hackerrank.com')
print(m.group(1))      # The first parenthesized subgroup.
# >>> Output: 'username'

import re
m = re.match(r'(\w+)@(\w+)\.(\w+)','username@hackerrank.com')
print(m.group(2) )      # The second parenthesized subgroup.
# >>> Output: 'hackerrank'

import re
m = re.match(r'(\w+)@(\w+)\.(\w+)','username@hackerrank.com')
print(m.group(3))      # The third parenthesized subgroup.
# >>> Output: 'com'

import re
m = re.match(r'(\w+)@(\w+)\.(\w+)','username@hackerrank.com')
print(m.group(1,2,3))   # Multiple arguments give us a tuple.
# >>> Output: ('username', 'hackerrank', 'com')


# groups(): A groups() expression returns a tuple containing all the subgroups of the match.
import re
m = re.match(r'(\w+)@(\w+)\.(\w+)','username@hackerrank.com')
print(m.groups())
# >>> ('username', 'hackerrank', 'com')

# groupdict(): A groupdict() expression returns a dictionary containing all the named subgroups of the match, keyed by the subgroup name.
m = re.match(r'(?P<user>\w+)@(?P<website>\w+)\.(?P<extension>\w+)','myname@hackerrank.com')
print(m.groupdict())
# >>> Output: {'website': 'hackerrank', 'user': 'myname', 'extension': 'com'}


import re 
s = 'ay29020@gmail.com'
match_str = re.findall(r"\d?", s)
print(match_str) #Output: ['', '', '2', '9', '0', '2', '0', '', '', '', '', '', '', '', '', '', '', '']

import re 
s = 'ay29020@gmail.com'
match_str = re.findall(r"\d?", s)
print(match_str) 


# Questions answer
import re
s = input()
m = re.search(r"([a-zA-Z0-9])\1", s)
if m:
    print(m.group(1))
else:
    print(-1)



###########################################################
################ Question #* Re.findall() & Re.finditer()
#Concept and methods:-
# re.findall():The expression re.findall() returns all the non-overlapping matches of patterns in a string as a list of strings.

# Positive Lookahead Assertion ('(?= ... )') Syntax: (?= ... ): 
#* Example: a(?=b) matches "a" only if it is followed by "b," but "b" is not included in the match.

# Negative Lookahead Assertion ('(?! ... )'):
#* pattern = r'\d(?!a)'  # Match a digit (\d) that is not followed by 'a'

# Positive Lookbehind Assertion ('(?<= ... )') Syntax: (?<= ... ): 
#* Example: (?<=b)a matches "a" only if it is preceded by "b," but "b" is not included in the match.

# Negative Lookbehind Assertion ('(?<! ... )'):
#* pattern = r'(?<!b)\d'  # Match a digit (\d) that is not preceded by 'b'

# Word Boundaries ('\b ... \b'):
#* pattern = r'\bword\b'  # Match the word 'word' as a whole word

# Start of String ('^') and End of String ('$'):
#* pattern = r'^start'    # Match 'start' at the beginning of a string
#* pattern = r'end$'      # Match 'end' at the end of a string

# parentheses ():
#* Grouping: Parentheses are used to group together parts of a regular expression so that you can apply quantifiers,
#*-  alternation, or other modifiers to that group as a whole.

"""
# For Example:
(abc)+ matches one or more repetitions of the sequence "abc."
(x|y) matches either "x" or "y."
"""

# More Example
import re
re.findall(r'\w','http://www.hackerrank.com/')
# >>> ['h', 't', 't', 'p', 'w', 'w', 'w', 'h', 'a', 'c', 'k', 'e', 'r', 'r', 'a', 'n', 'k', 'c', 'o', 'm']

# re.finditer(): The expression re.finditer() returns an iterator yielding MatchObject instances over all non-overlapping matches for the re pattern in the string.
import re
re.finditer(r'\w','http://www.hackerrank.com/')
# <callable-iterator object at 0x0266C790>
map(lambda x: x.group(),re.finditer(r'\w','http://www.hackerrank.com/'))
['h', 't', 't', 'p', 'w', 'w', 'w', 'h', 'a', 'c', 'k', 'e', 'r', 'r', 'a', 'n', 'k', 'c', 'o', 'm']

import re
for k in re.finditer(r'\w','http://www.hackerrank.com/'):
    print(k)
""" Output:
<re.Match object; span=(0, 1), match='h'>
<re.Match object; span=(1, 2), match='t'>  
....
...

"""



#* Questions answer
import re
S = input()
p = r'(?<=[bcdfghjklmnpqrstvwxtyzBCDFGHKLMNPQRSTVWXYZ])([aeiouAEIOU]{2,})(?=[bcdfghjklmnpqrstvwxtyzBCDFGHKLMNPQRSTVWXYZ])'
if re.findall(p,S):
    print(*re.findall(p,S), sep = "\n")
else :
    print(-1)
# OR
if re.findall(p,S):
    print("\n".join(re.findall(p,S)))
else:
    print(-1)
#OR
if re.findall(p,S):
    for re in re.findall(p,S):
        print(re)
else:
    print("-1")

# 2nd method we can take one case letter by using re.IGNORECASE
import re
pattern= re.compile(r'(?<=[qwrtypsdfghjklzxcvbnm])[aeiou]{2,}(?=[qwrtypsdfghjklzxcvbnm])',re.IGNORECASE)
matches= re.findall(pattern, input())
[print(*matches,sep="\n") if matches else print(-1)]



###########################################################
###################### Question #* Re.start() & Re.end()
# re.compile():
""" 
re.compile is a function from the re module that is used to create a regular expression object.
When you use re.compile, you provide it with a regular expression pattern as a string,
and it compiles that pattern into a regex object. This compiled regex object can then be used for various operations,
such as searching for matches, replacing text, or extracting information from strings efficiently.
"""

import re
# Create a regex pattern to match an email address
pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
# Compile the pattern into a regex object
regex = re.compile(pattern)
# Use the compiled regex object to search for matches
text = "My email address is john.doe@example.com"
match = regex.search(text)
if match:
    print("Found a match:", match.group())
else:
    print("No match found.")

#Questions answer
import re
S, k = input(), input()
pat = re.compile(k)
m = pat.search(S)
if m:
    while m:
        print((m.start(), m.end()-1))
        i = m.start() + 1
        m = pat.search(S, i)
else:
    print((-1, -1))
    
# 2nd method using forward assertion and backword
import re
s = input()
k = input()
m = re.finditer(f"(?=({k}))", s)
if re.search(k, s):
    for x in m:
        print((x.start(1), x.end(1)-1))
else:
    print((-1, -1))


"""
The re.search() expression scans through a string looking for the first location where the regex pattern produces a match.
It either returns a MatchObject instance or returns None if no position in the string matches the pattern.
"""
import re
print(bool(re.search(r"ly","similarly")))
# Output: True


###########################################################
############ Question #* (Detect Floating Point Number)
# 1st method
import re
for _ in range(int(input())):
    if re.search(r'^[+-]?[0-9]*\.[0-9]+$', input()):
    # OR if re.search(r"^[+-]?\d*\.\d+$", input()):
        print('True')
    else:
        print('False')

# Or
import re
for _ in range(int(input())):
    print(bool(re.search(r'^[\.+\-]?[0-9]*\.[0-9]+$' , input())))


# 2nd method
import re
T = int(input())
for _ in range(T):
    print(bool(re.match(r"^[+-]?\d*\.\d+$",input())))

#Or
import re
for _ in range(int(input())):
    print(re.match(r"^[+\-0-9]?[0-9]*[\.][0-9]+$", input()) != None)    

        
#3rd method
import re
for _ in range(int(input())):
    print(re.fullmatch(r'[+-]?\d*\.\d+', input()) is not None)
    


# Without regex
if __name__=="__main__":
    n=int(input())
    for i in range(n):
        try:
            x=float(input())
            if x==0:
                print("False")
            else:    
                print("True")
        except Exception as e:
            print("False")


###########################################################
######################################################
##################### Question #* Regex Substitution
"""
The re.sub() tool (sub stands for substitution) evaluates a pattern and, for each valid match,
it calls a method (or lambda).The method is called for all matches and can be used to modify strings in different ways.
The re.sub() method returns the modified string as an output.
"""

# Transformation of Strings: -
import re
#Squaring numbers
def square(match):
    number = int(match.group(0))
    return str(number**2)
print(re.sub(r"\d+", square, "1 2 3 4 5 6 7 8 9"))
# Output: 1 4 9 16 25 36 49 64 81

######
####Replacements in Strings: -
import re
html = """
<head>
<title>HTML</title>
</head>
<object type="application/x-flash" 
    data="your-file.swf" 
    width="0" height="0">
    <!-- <param name="movie"  value="your-file.swf" /> -->
    <param name="quality" value="high"/>
</object>
"""
print(re.sub("(<!--.*?-->)", "", html)) #remove comment
# >>> <head>
# >>> <title>HTML</title>
# >>> </head>
# >>> <object type="application/x-flash"      
# >>>     data="your-file.swf" 
# >>>     width="0" height="0">
# >>>     
# >>>     <param name="quality" value="high"/>
# >>> </object>

# Question Answers
# 1st method
import re
n=int(input())
pattern = re.compile(r'(?<=\s)(&&|\|\|)(?=\s)')
# pattern = re.compile(r'(?<=\s)(&&|\|\|)(?=\s)')
# pattern = re.compile(r'(?<=\s)(&){2}|\|{2}(?=\s)')   # wrong just for think
# Or pattern = re.compile(r"(?<= )([&]{2}|[|]{2})(?= )")
# pattern = re.compile(r"(?<=\s?)([&]{2}|[|]{2})(?=\s?)") # wrong just for think 
# bcz ? after whitespace \s makes optional it matches zero or one whitespace character
# Or pattern = re.compile(r"(?<=\s)([&]{2}|[|]{2})(?=\s)")
for _ in range(n):
    print(re.sub(pattern,lambda x: 'and' if x.group(0)=='&&' else 'or',input()))


# 2nd method indualing subs
import re
and_regex = re.compile(r'(?<= )&&(?= )')
or_regex = re.compile(r'(?<= )\|\|(?= )')
for _ in range(int(input())):
    line = input()
    line = re.sub(and_regex, 'and', line)
    line = re.sub(or_regex, 'or', line)
    print(line)
    
# 3rd method
import re
text = []
for _ in range(int(input())):
    text.append(input())
text = "\n".join(text)
text = re.sub(r"(?<= )([&]{2}|[|]{2})(?= )", lambda x: "and" if x.group() == "&&" else "or", text)
print(text)

#4th method
import re
def sub_func(s):
    s = re.sub(r'(?<= )\|\|(?= )', r'or', s)
    s = re.sub(r'(?<= )\&\&(?= )', r'and', s)
    return s
lines = [input() for _ in range(int(input()))]
for line in map(sub_func, lines):
    print(line)
    
# 5th method
import re
repl = lambda x: x.group().replace('&&', 'and').replace('||', 'or')
for _ in range(int(input())):
    print(re.sub(r'(?<= )\&\& |(?<= )\|\| ', repl, input()))


#6th method
import re
trans = {'||': 'or', '&&': 'and'}
for _ in range(int(input())):
    print(re.sub('(?!^)(?<= )(\|\||&&)(?= )', lambda m: trans[m.group(1)], input()))


# 7th method
import re
pattern = re.compile(r"(?<= )(&&|\|\|)(?= )")
ls = lambda x: 'and' if x.group(0) == "&&" else 'or'
for i in range(int(input())):
    s = input()
    m = pattern.sub(ls, s)
    print(m)
    
# 8th method
import re
for i in range(int(input())):
    s = re.sub("(?<=\s)&&(?=\s)", "and", input())
    print(re.sub("(?<=\s)\|\|(?=\s)", "or", s))




# Playing
text = "tapa tap!"
encoded_bytes = text.encode("utf-8")
print(encoded_bytes) # Output: b'tapa tap!'

text = "Abhi!!"
encoded_bytes = text.encode("utf-8")
for byte in encoded_bytes:
    bin_represent = bin(byte)
    print(bin_represent)
    
# Output:
#* 0b1000001 # '0b' is binary representation
#* 0b1100010     
#* 0b1101000     
#* 0b1101001     
#* 0b100001      
#* 0b100001
#* print(binary_representation[2:])

my_string = 'abhishek yadav??'
decode_string1 = my_string.encode("utf-8")
decode_string2 = my_string.encode("utf-16")
decode_string3 = my_string.encode("utf-32")
print(decode_string1)
print(decode_string2)
print(decode_string3)
"""
b'abhishek yadav??'
b'\xff\xfea\x00b\x00h\x00i\x00s\x00h\x00e\x00k\x00 \x00y\x00a\x00d\x00a\x00v\x00?\x00?\x00'
b'\xff\xfe\x00\x00a\x00\x00\x00b\x00\x00\x00h\x00\x00\x00i\x00\x00\x00s\x00\x00\x00h\x00\x00\x00e\x00\x00\x00k\x00\x00\x00 \x00\x00\x00y\x00\x00\x00a\x00\x00\x00d\x00\x00\x00a\x00\x00\x00v\x00\x00\x00?\x00\x00\x00?\x00\x00\x00'
"""

my_string = 'a'
decode_string1 = my_string.encode("utf-8")
decode_string2 = my_string.encode("utf-16")
decode_string3 = my_string.encode("utf-32")
print(decode_string1)
print(decode_string2)
print(decode_string3)
"""
b'a'
b'\xff\xfea\x00'
b'\xff\xfe\x00\x00a\x00\x00\x00'
"""

my_string = 'a'
encode_string1 = my_string.encode("utf-8")
encode_string2 = my_string.encode("utf-16")
encode_string3 = my_string.encode("utf-32")
print(bin(int.from_bytes(encode_string1, byteorder='big')))
print(bin(int.from_bytes(encode_string2, byteorder='big')))
print(bin(int.from_bytes(encode_string3, byteorder='big')))
"""
Output:-
0b1100001
0b11111111111111100110000100000000 #32 here's 0b is binary representation
0b1111111111111110000000000000000001100001000000000000000000000000 # 64
"""

a = '0b1111111111111110000000000000000001100001000000000000000000000000'
print(len(a)) #


"""
Unicode: - Unicode is a common, massive character set for all the world's languages, glyphs and emoji.
formally known as The Unicode Standard, is a text encoding standard maintained by the Unicode Consortium designed to support the use of text written in all of the world's major writing systems.


UTF (Unicode Transformation Format) a character encoding standard, has several encodings to accommodate
different requirements.There are three main types of UTF encoding standard : UTF-8, UTF-16, and UTF-32.

UTF-8:
Variable-length encoding.
Most widely used UTF encoding.
Represents characters using 1 to 4 bytes.
ASCII characters are represented using a single byte (compatible with ASCII).

UTF-16:
Fixed or variable-length encoding (two or four bytes per character).
Commonly used in Windows operating systems.
Represents characters using 2 or 4 bytes.
Can represent a broader range of characters with fixed-length encoding (BMP) or all Unicode characters with variable-length encoding (SMP).

UTF-32:
Fixed-length encoding (four bytes per character).
Simple and straightforward encoding.
Represents all Unicode characters in a consistent manner.
Requires more storage space compared to UTF-8 and UTF-16.

#and so on UTF-7, UTF-EBCDIC, UTF-1 and UTF-9... but not used currently

#* Bytes takes by each 
Character	            UTF-8	UTF-16	UTF-32
ASCII character	        1	       2	    4
Non-ASCII character	    1-4	     2	4

"""


import chardet
encoded_string = b'\xe4\xbd\xa0\xe5\xa5\xbd\xe7\x95\x8c\xe4\xb8\x96\xe7\x95\x8c'
encoding = chardet.detect(encoded_string)
print(encoding['encoding']) # utf-8

"""
This is how encoding happens internally in software by following a series of steps defined
by the chosen character encoding standard. Here's an overview of how encoding typically occurs within software:

Input Text: The process begins with input text in a human-readable form. This text can be entered by a user,
    read from a file, received from a network connection, or generated within the software.

Character Encoding: The software knows or is configured to use a specific character encoding standard (e.g., UTF-8, UTF-16, ASCII).
    This encoding standard defines how characters are mapped to binary representations (usually bytes) and vice versa.

Character Mapping: Each character in the input text is mapped to its corresponding code point according to the selected encoding standard.
    The code point is a unique numerical value assigned to each character in the character set. For example, the character 'A' might be represented as the code point 65 in ASCII.

Encoding: The software converts the code points into binary data based on the rules defined by the encoding standard.
    Depending on the encoding, this may involve fixed-length encoding (e.g., UTF-32) or variable-length encoding (e.g., UTF-8).

Binary Representation: The binary representation of the characters is stored in memory or processed by the software.
    These binary representations are often in the form of bytes, where each byte represents a portion of the encoded text.

Storage or Transmission: The binary data can be stored in files, databases, or transmitted over networks.
    The recipient software or system must know the encoding standard used to interpret the binary data correctly.

Decoding (When Needed): When the software needs to display or process the text,it may decode the binary data back into human-readable characters.
    Decoding follows the reverse process: the binary data is interpreted using the chosen encoding standard to recover the original code points, and then these code points are mapped to characters.

Internally, encoding and decoding typically involve libraries or functions provided by the programming language or the operating system. 
These libraries handle the complexities of the encoding standards, including error handling for invalid input.
It's crucial for software to use the correct encoding standard at each step of the process to ensure that
text is accurately represented and can be correctly interpreted by other systems or software components. Misunderstanding or misusing character encoding can lead to issues such as character corruption, data loss, or interoperability problems between different software systems.

"""


########################################################################
################################ Question (#*Regex Substitution)
# In regular expressions, the dot (.) is a metacharacter:
""" matches any character except a newline character (\n). In other words,
# the dot is used as a wildcard to represent any single character in the input text.

#* Here are some examples of how the dot (.) is used in regular expressions:

Basic Usage:

. matches any single character (except a newline character). For example, the pattern c.t would match "cat," "cut," "cot," and so on.
Quantifiers with Dot:

You can use quantifiers with the dot to specify how many characters you want to match. For example:
a.b matches "axb," "acb," "a1b," etc.
.* matches zero or more of any character.
.+ matches one or more of any character.
Character Classes with Dot:

You can combine the dot with character classes to match specific types of characters. For example:
[A-Z]. matches any uppercase letter followed by any character.
[0-9]. matches any digit followed by any character.
[aeiou]. matches any vowel followed by any character.
Escaping the Dot:

If you want to match a literal dot (period), you can escape it with a backslash (\.). For example, 3\.14 would match the string "3.14."
Dot in Multiline Mode:
In some regex engines, you can enable a multiline mode where the dot also matches newline characters. This behavior depends on the specific regex engine being used.
"""

import re
text = "cat bat rat dot"
pattern = r".at"
matches = re.findall(pattern, text)
print(matches) # ['cat', 'bat', 'rat']


import re
text = "Hello...world. This is a test...with ellipsis."
pattern = r"..."
matches = re.findall(pattern, text)
print(matches) # Output : ['Hel', 'lo.', '..w', 'orl', 'd. ', 'Thi', 's i', 's a', ' te', 'st.', '..w', 'ith', ' el', 'lip', 'sis']

import re
text = "Hello...world. This is a test...with ellipsis."
pattern = r"."
matches = re.findall(pattern, text)
print(matches)
# Output :['H', 'e', 'l', 'l', 'o', '.', '.', '.', 'w', 'o', 'r', 'l', 'd', '.', ' ', 'T', 'h', 'i', 's', ' ', 'i', 's', ' ', 'a', ' ', 't', 'e', 's', 't', '.', '.', '.', 'w', 'i', 't', 'h', ' ', 'e', 'l', 'l', 'i', 'p', 's', 'i', 's', '.']




#######################################################################
######################### Question #* (Validating Roman Numerals)
# I, X, and C can be repeated up to three times (e.g., III, XXX, CCC) and V, L, and D cannot be repeated.
# Large numbers can be written by placing a bar (line) above the numeral to indicate multiplication by 1000. For example, a bar above "V" (with "V̅") represents 5000.
# Symbols should be written from left to right in descending order of value, with the largest values on the left.
regex_pattern = r'^(M{0,3})(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'
import re
print(str(bool(re.match(regex_pattern, input()))))



#######################################################################
######################### Question #* (Validating phone numbers)
# 1st method
import re
pattern = r"^[789]\d{9}$"
N = int(input())
for _ in range(N):
    phone_num = input()
    if re.match(pattern, phone_num):
        print(True)
    else:
        print(False)

# 2nd method we can also use [0-9] instead of \d
import re
pattern = r"^[789]\d{9}$" #mistake done r"^[789]\[0-9]{9}$"
for _ in range(int(input())):
    phone_num = input()
    if re.match(pattern, phone_num):
        print("YES")
    else:
        print("NO")

#########################################################################
#################### Question #*Validating and Parsing Email Addresses
# \w is similar to [a-zA-Z0-9]
"""
#* < and >
< and > are used as literal characters are not like special metacharacters like ^, $, ., *, etc which have special meanings.
for example pattern r"<[a-zA-Z]([\w\.\-])+@([a-zA-Z])+\.([a-zA-Z]){1,3}>$" is using < and > as literal angle brackets
to match email addresses that are enclosed within these angle brackets.
"""
# 1st method without using email.utils
import re
n = int(input())
pattern = r'[a-zA-Z]+\s<[a-z]+[\w._-]{0,}@[a-z]+\.[a-z]{1,3}>'
for line in range(n):
    line = input()
    r = re.search(pattern, line)
    if r: 
        print(line)
        
#OR
import re
for _ in range(int(input())):
    user, email = input().split()
    if re.match(r'^[a-zA-Z]+[\w\-.]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$', email[1:-1]): #Would be okay if you use email.strip('<>')
        print(f'{user} {email}')

#2nd method using utils
import email.utils
import re
def is_valid_email_address(address):
    email_pattern = r'^[a-zA-Z\.\-_]+@[a-zA-Z]+\.[a-zA-Z]{1,3}$'
    return bool(re.match(email_pattern, address)) 
n = int(input())
for _ in range(n):
    line = input()
    name, address = email.utils.parseaddr(line)
    if is_valid_email_address(address):
        print(line)        

# 3rd method
import re
pattern = r'\A[a-zA-Z][\w\-.]+@[a-zA-Z]+\.[a-zA-Z]{1,3}'
value = []
for _ in range(int(input())):
    email = input()
    if re.fullmatch(pattern, email.split()[1].strip("<>")):
        value.append(email)
print(*value, sep='\n')


###########################################################
############################# Question #* Hex Color Code
import re
for _ in range(int(input())): 
    m = re.findall('.(#[A-Fa-f0-9]{6}|#[A-Fa-f0-9]{3})', input())
    if m:
        print(*m, sep="\n")
        
#2nd method
import re
n = int(input())
for i in range(n):
    s = input()   
    w = s.split()
    if len(w)>1 and '{' not in w:
        w = re.findall(r'#[a-fA-F0-9]{3,6}', s)
        [print(i) for i in w]

#3rd method
import re
for i in range(int(input())):
    s=input()
    c=re.findall(r"#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3}",s)
    if(len(c)!=0 and s[0]!='#'):
        for i in c:
            print(i)
# 4th method
import re
code_re = re.compile(r'[: ]+(#[0-9a-f]{6}|#[0-9a-f]{3})', re.I)
for _ in range(int(input())):
    codes = code_re.findall(input())
    if codes:
        print('\n'.join(codes))
        
# 5th method
import re
N = int(input())
for _ in range(N):
    S = input()
    found = re.findall(r"(#[0-9A-Fa-f]{3}|#[0-9A-Fa-f]{6})[,;)]",S)
    if found :
        print(*found,sep="\n")
# 6th method
import re
p = re.compile(r"#[\dA-F]{3,6}(?=[;,)])",re.I)
for _ in range(int(input())):
    for m in p.findall(input()):
        print(m)

# 7th method
import re
n = int(input())
pat = r'(#[a-fA-F\d]{3,6})\S'
for _ in range(n):
    res = re.findall(pat, input())
    for data in res:
        print("".join(data))

# 8th method
import re
pat = re.compile(r'(#[A-Fa-f0-9]{3}|#[A-Fa-f0-9]{6})\s*[,;)]')
n = int(input())
for _ in range(n):
    css_color_codes = pat.findall(input())
    if css_color_codes:
        print(*css_color_codes, sep='\n')

# 9th method       
import re
pattern = re.compile(r"(#[\da-f]{3}|#[\da-f]{6})(?=[;,)])", re.IGNORECASE)
N = int(input())
ls = [input() for _ in range(N)]
S = "\n".join(ls)
if pattern.search(S):
    for match in re.findall(pattern, S):
        print(match)

# 10the method
import re
n = int(input())
pattern = r'\#[a-fA-F0-9]{3,6}(?=[;,)])'
for _ in range(n):
    line = input()
    match = re.findall(pattern, line)
    if match:
        print(*match, sep='\n')
        

# 11th method
import re
pattern = re.compile(r'#([0-9a-fA-F]{1,2}){3}')
res = []
for _ in range(int(input())):
    s = input()
    if s.endswith(';'):
        res += [m.group(0) for m in re.finditer(pattern, s)]
print(*res, sep='\n')

#12th method
import re
p=r'(?<=[:\s])(#{1}[0-9a-fA-F]{3,6}(?=[;\s,)]))'
for i in range(int(input())):
    html=input()
    m=re.findall(p,html)
    if len(m)>0:
        [print (i) for i in m]
        
        
# 13th method
import re
hex_re = re.compile(r".(#([a-f\d]{3}){1,2})", re.I)
for _ in range(int(input())):
    for i in hex_re.finditer(input()):
        print(i.group(1))        

#13th method
import re
pattern = r"\#[A-Fa-f0-9]{6}|(?!^)\#[A-Fa-f0-9]{3}"
for _ in range(int(input())):
    m = re.findall(pattern, input())
    if m: print(*m, sep='\n')
    
# 14th method
import re
n = int(input())
for i in range(n):
    s = input()
    w = s.split()
    if len(w)>1 and '{' not in w:
        w = re.findall(r'#[a-fA-F0-9]{3,6}', s)
        [print(i) for i in w]
    
# 15th method
import re
for _ in range( int(input()) ):    
    input_str = input().strip()
    pattern = re.compile( r"(?<!^)(#([0-9A-Fa-f]{3}){1,2})" )
    matches = pattern.findall(input_str)    
    if matches:
        for m in matches:
            print(m[0]) # print all the matching string (group 0)


# 16th method
css = ""       
for _ in range(int(input())):
    lines = input()
    if not lines.startswith('#') and not lines.startswith('.'):
        css+= lines
[print(_) for _ in re.findall(r'\#[a-fA-F0-9]{3,6}',css)]


# 17th
import re 
n = int(input())
text = '\n'.join([input() for _ in range(n)])
pattern = re.compile(r'(?<=.)#[0-9a-fA-F]{3,6}')
matches = pattern.findall(text)
[print(match) for match in matches]

"""
A whitespace character in programming & text processing refers to any character
that represents horizontal or vertical space in the visual layout of text.
Whitespace characters are used to separate words, lines, and other elements of textual content.
They are typically not visible when rendered but affect the formatting and structure of the text.

whitespace_chars = [' ', '\t', '\n', '\r', '\v', '\f']

Space ( ): The most common whitespace character, used for separating words and elements in text.

Tab (\t): A horizontal tab character used for indentation and aligning text.


Newline (\n): A character used to mark the end of a line of text and create line breaks.

Carriage Return (\r): A character used to move the cursor to the beginning of the current line without starting a new line (less common).

Vertical Tab (\v): A character used for formatting or line separation (less common in regular text).

Form Feed (\f): A character used for page breaks and other formatting purposes (less common in regular text).
"""

###########################################################################
###################################### Question #* HTML Parser - Part 1
# parsing:
"""
#* parser:
A program that's usually part of a compiler.It receives input in the form of sequential source program instructions,
interactive online commands, markup tags or some other defined interface. Parsers break the input they get into parts
such as the nouns (objects), verbs (methods), and their attributes or options.

These are then managed by other programming,such as other components in a compiler.
A parser may also check to ensure that all the necessary input has been provided.

#* How does parsing work?
A parser is a program that is part of the compiler, and parsing is part of the compiling process. Parsing happens during the analysis stage of compilation.
In parsing, code is taken from the preprocessor, broken into smaller pieces and analyzed so other software can understand it. The parser does this by building a data structure out of the pieces of input.
More specifically, a person writes code in a human-readable language like C++ or Java and saves it as a series of text files. The parser takes those text files as input and breaks them down so they can be translated on the target platform.
The parser consists of three components, each of which handles a different stage of the parsing process. The three stages are:

#* Stage 1: Lexical analysis
#* Stage 2: Syntactic analysis
#* Stage 3: Semantic analysis




#* /Or:What is Parsing?
Parsing is the process of converting formatted text into a data structure. A data structure type can be any suitable representation of the information engraved in the source text.

Tree type is a common and standard choice for XML parsing, HTML parsing, JSON parsing, and any programming language parsing. The output tree is called Parse Tree or Abstract Syntax Tree. In HTML context, it is called Document Object Model (DOM).
A CSV file parsing can result in a List of List of values or a List of Record objects.
Graph Type is a choice for natural language parsing.
A piece of program that does parsing is called Parser.

How it works
Parser analyses the source text against the defined format*.
If source text does not match against format, errors are thrown or returned.
If matches, then “data structure” is returned.

"""
"""
HTML
Hypertext Markup Language is a standard markup language used for creating World Wide Web pages.

Parsing
Parsing is the process of syntactic analysis of a string of symbols. It involves resolving a string into its component parts and describing their syntactic roles.

HTMLParser
An HTMLParser instance is fed HTML data and calls handler methods when start tags, end tags, text, comments, and other markup elements are encountered.



.handle_starttag(tag, attrs):-
This method is called to handle the start tag of an element. (For example: <div class='marks'>)
The tag argument is the name of the tag converted to lowercase.
The attrs argument is a list of (name, value) pairs containing the attributes found inside the tag’s <> brackets.


.handle_endtag(tag):-
This method is called to handle the end tag of an element. (For example: </div>)
The tag argument is the name of the tag converted to lowercase.


.handle_startendtag(tag,attrs):-
This method is called to handle the empty tag of an element. (For example: <br />)
The tag argument is the name of the tag converted to lowercase.
The attrs argument is a list of (name, value) pairs containing the attributes found inside the tag’s <> brackets.
"""
from html.parser import HTMLParser
# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Found a start tag  :", tag)
    def handle_endtag(self, tag):
        print("Found an end tag   :", tag)
    def handle_startendtag(self, tag, attrs):
        print("Found an empty tag :", tag)
# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
parser.feed("<html><head><title>HTML Parser - I</title></head>"
            +"<body><h1>HackerRank</h1><br /></body></html>")



#Question answer
from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        for attr in attrs:
            print(f"-> {attr[0]} > {attr[1]}")

    def handle_endtag(self, tag):
        print("End   :", tag)

    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)

        for attr in attrs:
            print(f"-> {attr[0]} > {attr[1]}")
N = int(input())
parser = MyHTMLParser()
parser.feed("\n".join([input() for _ in range(N)]))


###########################################################################
###################################### Question #*HTML Parser - Part 2
# 1st
from html.parser import HTMLParser
n_lines = int(input())
class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if '\n' in data:
            print('>>> Multi-line Comment')
            print(data)
        else:
            print('>>> Single-line Comment')
            print(data)
    def handle_data(self, data):
        if data.strip():  
            print('>>> Data')
            print(data)
parser = MyHTMLParser()
html_input = '\n'.join([input() for _ in range(n_lines)])
parser.feed(html_input)


# 2nd method
from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):    
    def handle_comment(self, data):
        data = data.split('\n')
        if len(data) == 1:
            print('>>> Single-line Comment', *data, sep='\n')
        else:
            print('>>> Multi-line Comment', *data, sep='\n')
            
    def handle_data(self, data):
        if data.strip():
            print('>>> Data', *data.split('\n'), sep='\n')
parser = MyHTMLParser()
n_lines = int(input())
html_input = '\n'.join([input() for _ in range(n_lines)])
parser.feed(html_input)




# 3rd method using sys method
from html.parser import HTMLParser
import sys
class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if '\n' in data:
            print('>>> Multi-line Comment')
        else:
            print('>>> Single-line Comment')
        print(data)
    def handle_data(self, data):
        if data != '\n':
            print(f">>> Data\n{data}")
parser = MyHTMLParser()
N = int(input())
S = sys.stdin.read()
parser.feed(S)


############################################################################
########## Question #* Detect HTML Tags, Attributes and Attribute Values
# Quick revision
from html.parser import HTMLParser
from html.entities import name2codepoint
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start tag:", tag)
        for attr in attrs:
            print("     attr:", attr)
            
    def handle_endtag(self, tag):
        print("End tag  :", tag)

    def handle_data(self, data):
        print("Data     :", data)

    def handle_comment(self, data):
        print("Comment  :", data)

    def handle_entityref(self, name):
        c = chr(name2codepoint[name])
        print("Named ent:", c)

    def handle_charref(self, name):
        if name.startswith('x'):
            c = chr(int(name[1:], 16))
        else:
            c = chr(int(name))
        print("Num ent  :", c)

    def handle_decl(self, data):
        print("Decl     :", data)

parser = MyHTMLParser()
parser.feed('<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" '
            '"http://www.w3.org/TR/html4/strict.dtd">')

# Output: Decl     : DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd"

### Question's answer
# 1st method
from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for attr in attrs:
            print(f'-> {attr[0]} > {attr[1]}')
    
    def handle_startendtag(self, tag, attrs):
        print(tag)
        for attr in attrs:
            print(f'-> {attr[0]} > {attr[1]}')
parser = MyHTMLParser()
for _ in range(int(input())):
    parser.feed(input())
    
# 2nd method
# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser
n_lines = int(input())
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for attr in attrs:
            value_list = list(attr)
            print("->",attr[0],">",attr[1])
parser = MyHTMLParser()
html_input = '\n'.join([input() for _ in range(n_lines)])
parser.feed(html_input)


# Or using format
from html.parser import HTMLParser
# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("{}".format(tag))
        for name,value in attrs:
            print(f"-> {name} > {value}")

    def handle_startendtag(self,tag, attrs):
        print("{}".format(tag))
        for name,value in attrs:
            print(f"-> {name} > {value}")
# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
html = '\n'.join(input() for _ in range(int(input())))
parser.feed(html)



### 3rd method answer Using re
import re
import sys
N = int(input())
S = sys.stdin.read()
S = re.sub(r"<!--[\S\s]+?-->","",S)
tags = re.findall(r"<[^/][\S\s]*?>",S)
for tag in tags:
    attrs = re.findall(r'([\w-]+)="(.+?)"',tag)
    print(*re.findall("(?<=<)\w+",tag))
    for attr in attrs :
        print(f"-> {attr[0]} > {attr[1]}")



##################################################################
############################ Question #* Validating UID
# 1st method
import re
T = int(input())
pattern = r'^(?!.*(.).*\1)(?=(.*[A-Z]){2,})(?=(.*\d){3,})[a-zA-Z0-9]{10}$'
for _ in range(T):
    UID = input()
    if re.match(pattern, UID):
        print('Valid')
    else:
        print('Invalid')

"""
^: Start of the string.
(?!.*(.).*\1): Negative lookahead to ensure that no character repeats.
(?=(.*[A-Z]){2,}): Positive lookahead to ensure at least 2 uppercase English alphabet characters.
(?=(.*\d){3,}): Positive lookahead to ensure at least 3 digits.
[a-zA-Z0-9]{10}: Match exactly 10 alphanumeric characters.
$: End of the string.     
"""

#AND 
"""
#* ^(?!.*(.).*\1)
^: This is the anchor for the start of the string. It indicates that the matching should begin at the start of the string.
(?! ... ): This is a negative lookahead assertion. It asserts that what follows inside the parentheses should not occur for the match to be successful.
.*: This part matches any sequence of characters (0 or more) except for a newline. It essentially matches any part of the string.
(.): This captures a single character and stores it in a capturing group.
.*: Again, this matches any sequence of characters (0 or more) except for a newline.
\1: This is a backreference to the first capturing group (.). It ensures that whatever is captured in the first capturing group must occur again at this point in the string.
"""

# 2nd method 
from re import match
T = int(input())
def check(s):
    if len(s) == len(set(s)) == 10:
        if match(r".*[0-9].*[0-9].*[0-9].*", s) is not None:
            if match(r"^[a-zA-Z0-9]+$", s) is not None:
                if match(r".*[A-Z].*[A-Z].*", s) is not None:
                    return "Valid"
    return "Invalid"
for _ in range(T):
    print(check(input()))


# 3rd method
import re
upper2_re = re.compile(r'[A-Z].*[A-Z]')
digit3_re = re.compile(r'[0-9].*[0-9].*[0-9]')
nonchars_re = re.compile(r'[^0-9a-zA-Z]')
for _ in range(int(input())):
    s = input()
    if 10 == len(s) == len(set(s)) \
            and nonchars_re.search(s) is None \
            and upper2_re.search(s) is not None \
            and digit3_re.search(s) is not None:
        print("Valid")
    else:
        print("Invalid")
        
"""
Positive Lookahead (?= ...): A positive lookahead assertion checks if a pattern is followed by another pattern.
It asserts that what is inside the lookahead must occur but does not include it in the match. For example, A(?=B) would match "A" only if it is followed by "B."

Negative Lookahead (?! ...): A negative lookahead assertion checks if a pattern is not followed by another pattern.
It asserts that what is inside the lookahead must not occur. For example, A(?!B) would match "A" only if it is not followed by "B."

Positive Lookbehind (?<= ...): A positive lookbehind assertion checks if a pattern is preceded by another pattern.
It asserts that what is inside the lookbehind must occur but does not include it in the match. For example, (?<=A)B would match "B" only if it is preceded by "A."

Negative Lookbehind (?<! ...): A negative lookbehind assertion checks if a pattern is not preceded by another pattern.
It asserts that what is inside the lookbehind must not occur. For example, (?<!A)B would match "B" only if it is not preceded by "A."
"""
# Example :
# (?=pattern) :(?=pattern) is the syntax for a positive lookahead assertion.pattern is the condition that needs to be satisfied for the match to occur.
import re
text = "I have 33 apples and 5 bananas."
pattern = r'\d+(?=\sapples)'
matches = re.findall(pattern, text)
for match in matches:
    print(match) # Output: 33
#  It will match and capture "33" because it's followed by "apples" with a space in between, but it won't capture the space or "apples" itself.


# Positive Lookbehind (?<= ...) if you have the regular expression (?<=@)\w+, it will match word characters (\w+) that are preceded by the @ symbol, but the @ symbol itself will not be included in the match.
import re
text = "My email address is john@example.com"
pattern = r'(?<=@)\w+'
matches = re.findall(pattern, text)
for match in matches:
    print(match)  #Output: example




# So As Easier
import re
# .* all except newline and \w only word character(includes letters(both uppercase & lowercase), digits and underscores)
regex = r'^(?=(?:.*[A-Z]){2,})(?=(?:.*\d){3,})(?!.*(.).*\1)[\w]{10}$' 
for i in range(int(input())):
    ID = input()
    if re.match(regex, ID):
        print("Valid")
    else:
        print("Invalid")
        
"""
#* (?: ... )
In regular expressions, (?: ... ) is a non-capturing group. It is used to group a set of characters or sub-patterns together without capturing the matched content. This means that the contents of the non-capturing group are treated as a single unit,
just like a regular capturing group ( ... ), but it doesn't create a capturing group that can be referenced later.

non-capturing groups (?: ... ) are:
Grouping: They allow you to apply quantifiers, alternations, or other operations to a specific portion of the pattern
without creating a capturing group. This can make your regular expressions more efficient and easier to work with.

Performance: Capturing groups require additional memory and processing to store the matched content.
Non-capturing groups can be more efficient when you don't need to capture and reference the matched content.

For example, consider the expression (?:ab)+ which matches one or more occurrences of "ab" in a string. If you used a capturing group, like (ab)+, it would capture each occurrence of "ab" separately. With (?:ab)+, the non-capturing group still allows you to apply the + quantifier to the entire "ab" sequence without creating multiple captures.

In summary, (?: ... ) is a useful tool for organizing and optimizing regular expressions when you don't need to capture specific sub-patterns for later reference.


Suppose you want to match a date in the format "MM/DD/YYYY," but you're only interested in the month and year. You can use a non-capturing group to exclude the day:

Capturing group: (\d{2})/(?:\d{2})/(\d{4})
"""


##################################################################
####################### Question #*Validating Credit Card Numbers
# my test
# Backreference in regular expressions (regex):
# It's a way to find repeated patterns within a string. For example, the pattern (\w)\1 matches repeated letters in words like "letter" (matching "tt") or "banana" (matching "nn").

"""
ramaadan:
backreference: "(\w)(\w)\w*\2\1"
(\w): The first capturing group captures the first word character. In "ramaadan," the first word character is "r." So, \1 now contains "r."

(\w): The second capturing group captures the second word character. In "ramaadan," the second word character is "a." So, \2 now contains "a."

\w*: This matches zero or more word characters. In "ramaadan,"
#* it matches "amaadan" (all characters after the first two).

\2: This is a backreference to the second capturing group, which contains "a." It checks that the same character "a" is present in the text.

\1: This is a backreference to the first capturing group, which contains "r." It checks that the same character "r" is present in the text.

As we go through the steps with the word "ramaadan":

The first word character "r" is captured by \1.
The second word character "a" is captured by \2.
The \w* part matches "amaadan."
The backreference \2 checks for "a," which is present.
The backreference \1 checks for "r," which is present.
"""

"""
#* Example 1: Matching Repeated Characters
# Regular Expression: (\w)\1: -
(\w): This captures a single word character (letter, digit, or underscore).
\1: This is a backreference to the first capturing group, expecting the same character as captured by the first group.
Strings that would match:

"aa" (two identical characters)
"77" (two identical digits)
"c_c" (two identical word characters separated by an underscore)

#* Example 2: Matching Repeated Words
Regular Expression: (\b\w+\b)\s\1 :-

(\b\w+\b): This captures a whole word.
\s: This matches a whitespace character.
\1: This is a backreference to the first capturing group, expecting the same word as captured by the first group.
Strings that would match:

"apple apple" (the same word repeated)
"123 123" (the same numeric word repeated)
"cat cat" (the same word repeated)

#* Example 3: Matching Palindromes
Regular Expression: (\w)(\w)\w*\2\1 :-

(\w): single word character.
(\w): another single word character.
\w*: This matches zero or more word characters.
\2: This is a backreference to the second capturing group, expecting the same character as captured by the second group.
\1: This is a backreference to the first capturing group, expecting the same character as captured by the first group.
Strings that would match:

"level" (a palindrome)
"deified" (another palindrome)
"radar" (yet another palindrome)

# More Example:
[0-9]\1 : will match 11, 33,66,99 and so on
[0-9]\2 : wrong we didn't specified 2nd capturing group
[0-9]\1\1\1: will match 1111 2222 3333 and so on
"""

# 1st method
#1st method
cond1_5 = r"^(4|5|6)[0-9]{3}\-?[0-9]{4}\-?[0-9]{4}\-?[0-9]{4}$"
cond6 = r"([0-9])\1\1\1"
for _ in range(int(input())):
    card_n = input()
    if re.match(cond1_5,card_n) == None:
        print("Invalid")
    else:
        print("Valid" if re.search(cond6, re.sub(r'[-]','',card_n))== None else "Invalid")


# Note: Regular expressions are typically evaluated from left to right.
# 2nd method
import re
N = int(input())
for i in range(N):
    s = input()
    if (re.match(r'^[456][0-9]{3}(-?\d{4}){3}$',s) and not re.search(r'([0-9])(-?\1){3}',s)):
        print('Valid')
    else:
        print('Invalid')
# Note: The "?-" sequence in a regular expression is used to make a character or group optional. In your regular expression (-?\d{4}), the ? means that the hyphen character - is optional.
# -? 0 or 1 "-"

# Example : 
"""
the entire (-?\d{4}) part matches a group of four digits with an optional hyphen before it.
This means it can match patterns like "1234" or "-5678" or "9999," where the hyphen is optional, and the group always contains four digits.
"""

#3rd method
import re
number_of_inputs = int(input())
for i in range(0, number_of_inputs):
    numb1 = input()     
    numb = re.sub(r"^(\d{4})-?(\d{4})-?(\d{4})-?(\d{4})$", r'\1\2\3\4', numb1)    
    cond_1_5 = r"^[456]\d{15}"
    if re.search(cond_1_5, numb):
        cond_6 = r"(\d)\1{3}"
        if re.search(cond_6, numb):
            print("Invalid")
        else:
            print('Valid')
    else:
        print('Invalid')

#4th method
import re
def validCard(num):
    if all([
        re.match('^[456]', num),
        re.match('^\d{4}(-?\d{4}){3}$', num),
        not re.findall(r'(\d)\1\1\1', re.sub('-', '', num))
    ]):
        return True
    else:
        return False
for _ in range(int(input())):
    if validCard(input()):
        print('Valid')
    else:
        print('Invalid')

# 5th method
import re
ccnum_re = re.compile(r'^(?!.*(\d)(-?\1){3})[456]\d{3}(?:-?\d{4}){3}$')
for _ in range(int(input())):
    print('Valid' if ccnum_re.match(input()) else 'Invalid')

# Or
import re
pat = re.compile(r'^(?=[456])(?!.*(\d)(?:-?\1){3})(?:\d{4}(?:-?\d{4}){3})$')
for _ in range(int(input())):
    print('Valid' if re.match(pat, input()) else 'Invalid')


##################################################################
########################### Question #* Validating Postal Codes
"""
#* Positive Lookahead (?= ...):
#* Negative Lookahead (?! ...):
#* Positive Lookbehind (?<= ...):
#* Negative Lookbehind (?<! ...):
"""


regex_integer_in_range = r"[1-9]\d{5}$"	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"	# Do not delete 'r'.
import re
P = input()
print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)


##################################################################
############################ Question #* (Matrix Script)
# zip is used to combine two or more iterables (e.g., string, lists, tuples, or other sequences) into a single iterable. 
# my code
import math
import os
import random
import re
import sys
first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
matrix = []
matrix1 = []
matrix2 = []
for _ in range(n):
    matrix_item = list(input())
    matrix.extend(matrix_item[0])
    matrix1.extend(matrix_item[1])
    matrix2.extend(matrix_item[2])
new_list = matrix + matrix1 + matrix2
string = "".join(str(x) for x in new_list)
print(re.sub("(?<=\w)\W+?(?=\w)", " ", string))

# Or
import math
import os
import random
import re
import sys
first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
matrix = []
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
print(matrix)
print(*matrix)
print(list(zip(matrix)))
print(list(zip(*matrix)))
# ['Tsi', 'h%x', 'i #', 'sM ', '$a ', '#t%', 'ir!']
# Tsi h%x i # sM  $a  #t% ir!
# [('Tsi',), ('h%x',), ('i #',), ('sM ',), ('$a ',), ('#t%',), ('ir!',)]
# [('T', 'h', 'i', 's', '$', '#', 'i'), ('s', '%', ' ', 'M', 'a', 't', 'r'), ('i', 'x', '#', ' ', ' ', '%', '!')]
S = ""
for i in list(zip(*matrix)):
    S += "".join(i)
S = re.sub(r"(?<=\w)([!@#\$%\& ]+?)(?=\w)", " ", S)
print(S)

# Method 1 Create String from Columns Using 2 loops
first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
matrix = []
for _ in range(n):
    matrix.append(list(input()))
S = ""
for i in range(m):
    for j in range(n):
        S += matrix[j][i]
S = re.sub(r"(?<=\w)([!@#\$%\& ]+?)(?=\w)"," ",S)
print(S)

#OR
first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
matrix = []
for _ in range(n):
    matrix.append(list(input()))
S = ''.join([''.join([matrix[j][i] for j in range(n]) for i in range(m)]))
S = re.sub(r"(?<=\w)([!@#\$%\& ]+?)(?=\w)"," ",S)
print(S)

# OR
import re
dimensions = list(map(int,input().split()))
Matrix = []
for _ in range(dimensions[0]):
    Matrix.append(list(input()))
s = "".join()
text = "".join([row[i] for i in range(y) for row in rows])


# Method 2 Create String from Columns Using zip function
first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
matrix = []
for _ in range(n):
    Matrix.append(list(input()))
S = ""
for i in list(zip(*Matrix)):
    S += "".join(i)
S = re.sub(r"(?<=\w)([!@#\$%\& ]+?)(?=\w)"," ",S)
print(S)


# example
my_name = ['abhishek', 'vivek']
print(list(zip(my_name))) # Output :[('abhishek',), ('vivek',)]
print(list(zip(*my_name))) # output : [('a', 'v'), ('b', 'i'), ('h', 'v'), ('i', 'e'), ('s', 'k')]


# 3rd Method  Create String from Columns Using numpy
import re
import numpy
dimensions = list(map(int,input().split()))
r = dimensions[0]
c = dimensions[1]
Matrix = []
for _ in range(r):
    Matrix.append(list(input()))
S = ""
for i in numpy.transpose(numpy.array(Matrix)):
    S += "".join(i)
S = re.sub(r"(?<=\w)([!@#\$%\& ]+?)(?=\w)"," ",S)
print(S)


# 4th method
import re
x, y = list(map(int, input().split()))
rows = [input() for i in range(x)]
# print(rows) ['Tsi', 'h%x', 'i #', 'sM ', '$a ', '#t%', 'ir!']
text = ""
for i in range(y):
    for row in rows:
        text += row[i]
text = re.sub('([A-Za-z1-9])[^A-Za-z1-9]+([A-Za-z1-9])', r'\1 \2', text)
text = re.sub('  ', ' ', text)
print(text)

# Or
import re
x,y = list(map(int,input().split()))
rows =[input() for i in range(x)]
text = "".join([row[i] for i in range(y) for row in rows])
text = re.sub('([A-Za-z1-9])[^A-Za-z1-9]+([A-Za-z1-9])', r'\1 \2', text)
text = re.sub('  ', ' ', text)
print(text)


message_coded = ''.join(sum(zip(*matrix),()))
pat = r'(?<=[a-zA-Z0-9])([^a-zA-Z0-9]+)(?=[a-zA-Z0-9])'
print(re.sub(pat, ' ', message_coded))


text = " "
for j in range(m):
    for i in range(n):
        text += ''.join(matrix[i][j])
print(re.sub(r'\b\W+\b', " ", text))


message = "".join(["".join(_) for _ in zip(*matrix)])
print(re.sub("(?<=[a-zA-Z0-9])[!@#$%&\s]+(?=[a-zA-Z0-9])",' ',message))


matrix = [list(input()) for _ in range(n)]
txt=''.join([''.join(x) for x in list(zip(*matrix))])
print(re.sub('(?<=\w)[^\w]+(?=\w)',' ',txt))


import re
m, n = map(int,input().split())
matrix = [list(input()) for _ in range(m)]
text = ''.join([matrix[j][i] for i in range(n) for j in range(m)])
text = re.sub(r'(?<=\w)[!\@\#\$%&\s]+(?=\w)', ' ', text)
print(text)


m = [input() for _ in range(int(input().split()[0]))]
print(re.sub(r'\b\W+\b', ' ', ''.join(map(''.join, zip(*m)))))


from itertools import chain
n, m = map(int, input().split())
matrix = [input() for _ in range(n)]
print(re.subn(r'(\w)[^\w]+(\w)',r'\1 \2', ''.join(chain.from_iterable([*zip(*matrix)])))[0])



n, m = map(int, input().split())
arr = ''.join([''.join(t) for t in zip(*[input() for _ in range(n)])])
print(re.sub(r'\b[^a-zA-Z0-9]+\b', r' ', arr))


matrix = []
# Get the text from matrix
text = [line[i] for i in range(m) for line in matrix]
text = ''.join(text)
# Find and replace
pattern = r'([A-Za-z0-9])[!@#$%&\s]+(?=[A-Za-z0-9])'
text = re.sub(pattern,r'\1 ', text)
print(text)


n, m = map(int, input().split())
arr = ''.join([''.join(t) for t in zip(*[input() for _ in range(n)])])
print(re.sub(r'\b[^a-zA-Z0-9]+\b', r' ', arr))


import re
count = 0
decode = ''
val = list(map(int, input().split()))
input_val = [input() for x in range(val[0])]
while count != val[1]:
    for y in input_val:
        decode += y[count]
    count += 1
print(re.sub(r'(?<=([a-zA-Z0-9]))[\s$#%&]+(?=[a-zA-Z0-9])',' ', decode))


import re
print(re.sub(r'\b[^\w\d]+\b',' ', ''.join([''.join(t) for t in zip(*[input().replace('\r','') for x in range(int(input().split()[0]))])])))


import re
from itertools import chain
print(re.sub(r'(?<=\w)\W+?(?=\w)',' ',''.join(chain(*zip(*[input() for _ in range(int(input().split()[0]))])))))
# Or
import re
print(re.sub(r"\b[^A-Za-z0-9]+\b", " ", "".join(["".join(x) for x in zip(*[input() for _ in range(int(input().split()[0]))])])))


from re import sub
n, m = map(int, input().split())
message_chars = sum(zip(*(input() for _ in range(n))), ())
print(sub(r'(?<=\w)\W+(?=\w)', ' ', ''.join(message_chars)))


import re
def decode_script(script):
    decoded_script = re.sub(r'(?<=[a-zA-Z0-9])(\W+)(?=[a-zA-Z0-9])', ' ', script)
    return decoded_script


matrix = []
coll, rows = map(int, input().split())
s = ""
for i in range(0, coll):
    matrix.append(list(map(str, input())))
for i in range(0, rows):
    for g in range(0, coll):
        s += matrix[g][i]
print(decode_script(s))


import re
n,m = map(int, input().split())
matrix = []
[matrix.append(list(input())) for _ in range(n)]
matrix = list(zip(*matrix))
result = ''.join([c for s in matrix for c in s])
print(re.sub(r'(?<=[^\W_])([\W]+?)(?=[^\W_])',' ', result))


import re
n, m = map(int, input().split())
matrix = [input() for _ in range(n)]
s = ''.join(matrix[i][j] for j in range(m) for i in range(n))
decoded = re.sub(r'(?<=[a-zA-Z0-9])[\W_]+(?=[a-zA-Z0-9])', ' ', s)
print(decoded)


n, m = map(int, input().rstrip().split())
matrix = [input() for _ in range(n)]
s = ''.join(matrix[j][i] for i in range(m) for j in range(n))
print(__import__('re').sub(r'(?<=\w)[^\w]{1,}(?=\w)', ' ', s))


import re
n, m = (map(int, input().split()))
script = ''.join(list(map(''.join, list(zip(*[input() for _ in range(n)])))))
print(re.sub(r'([a-zA-Z0-9])[^a-zA-Z0-9]+([a-zA-Z0-9])', r'\1 \2', script))



####################################################################
############################################################# (XML)
####################################################################
"""
XML (Extensible Markup Language): XML is a markup language designed to store and transport data. It uses a set of rules for encoding documents in a format that is both human-readable and machine-readable.

1. Elements:
Elements are the fundamental building blocks of an XML document.
They have a start tag, an end tag, and content in between.
Example: <book>Harry Potter</book>

2. Tags:
Tags are used to define elements.
Tags are enclosed in angle brackets < >.
Example: <book>

3. Attributes:
Attributes provide additional information about elements.
They are always specified in the start tag.
Example: <book genre="fantasy">

4. Nesting:
Elements can be nested within other elements, creating a hierarchical structure.
Example:
xml
Copy code
<library>
    <book>Harry Potter</book>
    <book>The Hobbit</book>
</library>

5. Root Element:
Every XML document has a single root element that contains all other elements.
It's the top-level element.

6. Comments:
Comments are enclosed in <!-- -->.
They are used for adding notes or explanations to the XML.

7. XML Declaration:
The XML declaration is optional and specifies the XML version.
Example: <?xml version="1.0"?>

8. CDATA Section:
CDATA sections allow you to include character data that shouldn't be parsed.
It's enclosed in <![CDATA[ ... ]]>.

9. Valid XML:
XML documents must follow a set of rules to be well-formed and valid.
Well-formed XML adheres to basic syntax rules.
Valid XML conforms to a Document Type Definition (DTD) or XML Schema.

10. Parsing XML:
To work with XML in programming, you need to parse it.
Popular XML parsing libraries include:
Python: xml.etree.ElementTree, minidom, and lxml
Java: javax.xml.parsers
JavaScript: Browsers provide built-in XML parsers
C#: System.Xml

11. Serialization:
You can serialize (generate) XML from structured data in your program.
Popular libraries provide methods for creating XML from objects or data structures.

12. XPath:
XPath is a language for navigating and querying XML documents.
It allows you to select elements and attributes using expressions.
Example: /library/book

13. XSLT (Extensible Stylesheet Language Transformations):
XSLT is a language for transforming XML documents into other formats (e.g., HTML).
It uses XSLT stylesheets to define the transformation rules.

14. Namespaces:
Namespaces are used to avoid element name conflicts in XML.
They're defined using xmlns attributes.
Example: <book xmlns="http://example.com">

15. Entity References:
Entities are used to represent special characters in XML.
Example: &lt; represents <, &gt; represents >.
This is just the tip of the iceberg, but it provides you with a basic understanding of XML. To truly master XML, you'll need to practice working with XML documents, using libraries for parsing and generating XML, and delve deeper into more advanced topics like XSLT, namespaces, and XML schema validation.

"""



##################################################################
########################## Question #*(XML 1 - Find the Score)
import sys
import xml.etree.ElementTree as etree
def get_attr_number(node):
    return sum(len(element.attrib) for element in node.iter())
if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))
    
    
# 2nd method
import sys
import xml.etree.ElementTree as etree
def get_attr_number(node):
    counter = 0
    counter = counter + len(node.attrib)
    print(counter)
    for element in node:
        counter = counter + get_attr_number(element)
    return counter
if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))


##################################################################
##################### Question #*(XML2 - Find the Maximum Depth)
import xml.etree.ElementTree as etree
maxdepth = 0
def depth(elem, level):
    global maxdepth
    level += 1
    if level > maxdepth:
        maxdepth = level
    for child in elem:
        depth(child, level) #

if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)


##################################################################
############################ Question #* Find Angle MBC
# Enter your code here. Read input from STDIN. Print output to STDOUT

#######################################################################################
########################################################### (Closures and Decorators)
#######################################################################################


#######################################################################################
######################### Question #* Standardize Mobile Number Using Decorators
def wrapper(f):
    def fun(l):
        formatted_num = []
        for number in l:
            number = str(number)
            if len(number) == 10:
                new_number = '+91 ' + number[:5] + ' ' + number[5:]
            else:
                number = number[-10:]
                new_number = '+91 ' + number[:5] + ' ' + number[5:]
            formatted_num.append(new_number)
        f(formatted_num)
    return fun         
@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 

# 2nd method
def wrapper(f):
    def fun(l):
        return f([('+91 '+ number[-10:-5] + ' ' + number[-5:]) for number in l])
    return fun
@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 
    
# 3rd method using re
import re
def wrapper(f):
    def fun(l):
        pattern = re.compile(r'^(\+91|91|0){0,1}([\d]{5})([\d]{5})$')
        f([re.sub(pattern,r'+91 \2 \3',i) for i in l])
    return fun

# 4th method
def wrapper(f):
    def fun(l):
        f(' '.join(['+91',x[-10:-5],x[-5:]]) for x in l)
    return fun
# Or
def wrapper(f):
    def fun(l):
        f(['+91 {} {}'.format(x[-10:-5],x[-5:]) for x in l])
    return fun


# Or
def wrapper(f):
    def fun(l):
        f(['+91 %s %s' % (x[-10:-5],x[-5:]) for x in l])
    return fun

# 5th method
def wrapper(f):
    def fun(l):
        f([f"+91 {i[-10:-5]} {i[-5:]}" for i in l])
    return fun

#######################################################################################
################################# Question #* Decorators 2 - Name Directory
import operator
def person_lister(f):
    def inner(people):
        return [f(person) for person in sorted(people, key=lambda x: int(x[2]))]
    return inner
@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]
if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')



####################################################################
######################################################### Numpy
####################################################################

"""
NumPy is package for scientific computing in Python.
it's python library that provides a multidimensional array object,
various derived objects (such as masked arrays and matrices), 
and NumPy offers a variety of functions or methods for fast operations on arrays,
including mathematical, logical, shape manipulation, sorting,
selecting, I/O, discrete Fourier transforms, basic linear algebra,
basic statistical operations, random simulation and much more.


At the core of the NumPy package, is the ndarray object. This encapsulates n-dimensional arrays of homogeneous data types,
with many operations being performed in compiled code for performance.

There are several important differences between NumPy arrays and the standard Python sequences:

#* NumPy arrays have a fixed size at creation, unlike Python lists (which can grow dynamically).
Changing the size of an ndarray will create a new array and delete the original.

#* The elements in a NumPy array are all required to be of the same data type, and thus will be the same size in memory.
The exception: one can have arrays of (Python, including NumPy) objects, thereby allowing for arrays of different sized elements.

#* NumPy arrays facilitate advanced mathematical and other types of operations on large numbers of data.
Typically, such operations are executed more efficiently and with less code than is possible using Python’s built-in sequences.

#* A growing plethora of scientific and mathematical Python-based packages are using NumPy arrays;
though these typically support Python-sequence input, they convert such input to NumPy arrays prior to processing,
and they often output NumPy arrays


Why is NumPy Fast? :-
#* Vectorization:
Vectorization describes the absence of any explicit looping, indexing, etc.,
in the code - these things are taking place, of course, just “behind the scenes” in optimized, pre-compiled C code.
Vectorized code has many advantages, among which are:

#* vectorized code is more concise and easier to read

#* fewer lines of code generally means fewer bugs

#* the code more closely resembles standard mathematical notation (making it easier, typically, to correctly code mathematical constructs)

#* vectorization results in more “Pythonic” code. Without vectorization, our code would be littered with inefficient and difficult to read for loops.

#* WE CAN ALSO SEE WITH AN EXAMPLE
import numpy as np
arr = np.array([1,2,3,4])
print(id(arr[0]))
print(id(arr[1]))
print(id(arr[2]))
print(id(arr[3]))
"""
2467347479920
2467347479920
2467347479920
2467347479920
"""

arr = [1,2,3,4]
print(id(arr[0]))
print(id(arr[1]))
print(id(arr[2]))
print(id(arr[3]))
"""
140717874213672
140717874213704
140717874213736
140717874213768
"""

#* Broadcasting:
Broadcasting is the term used to describe the implicit element-by-element behavior of operations; generally speaking, in NumPy all operations, not just arithmetic operations, but logical, bit-wise, functional, etc.
This is a powerful feature that allows you to perform element-wise operations on arrays with different shapes. When you perform operations between arrays that don't have the same shape, NumPy will automatically adjust the dimensions of one or both of the arrays to make the operation possible.

#* If the arrays do not have the same number of dimensions, NumPy will pad the smaller-dimension array with ones on its left side until both shapes have the same length.

#* If, after applying rule 1, the sizes of the dimensions do not match, NumPy will check whether one of the dimensions has a size of 1. If it does, NumPy will stretch that dimension to match the corresponding dimension of the other array.

#* If the sizes of the dimensions do not match, and neither of them is 1, then NumPy will raise a "ValueError" because the operation is not broadcast-compatible.

#* The main features of numpy array is the ability to perform vectorized operations (element-wise operations without the need for explicit loops), which can significantly improve performance for numerical computations.
"""

from numpy import doc
help(doc) # help(np.doc.TOPIC)


"""
#* Note: In NumPy, "scalars" typically refer to individual single values, as opposed to arrays.
Scalars in NumPy can be any individual numerical value, such as an integer, float, or complex number.
These scalar values are not contained within arrays or data structures like NumPy arrays;
they are just individual numeric values.

For example, the following are all examples of scalars:
5 (an integer scalar)
3.14 (a floating-point scalar)
2 + 3j (a complex scalar)
"""


"""
numpy.ndarray :-
#* class numpy.ndarray(shape, dtype=float, buffer=None, offset=0, strides=None, order=None)

An array object represents a multidimensional, homogeneous array of fixed-size items. 
An associated data-type object describes the format of each element in the array (its byte-order, 
how many bytes it occupies in memory, whether it is an integer, a floating point number, or something else, etc.

#* A "buffer" refers to the memory storage that holds the actual data of the array.
The buffer of a NumPy array is a low-level, C-style memory representation of the data.
It allows NumPy to take advantage of efficient memory management and data manipulation,
making it suitable for numerical and scientific computing. When you perform operations on NumPy arrays,
you are often working with the data stored in the buffer.

#* Example: -
"""
import numpy as np

# Create a NumPy array
arr = np.array([1, 2, 3, 4, 5])

# Access the buffer
buffer_data = arr.data

# Display the buffer content (as a bytes-like object)
print(buffer_data.tobytes()) #Output : b'\x01\x00\x00\x00\x02\x00\x00\x00\x03\x00\x00\x00\x04\x00\x00\x00\x05\x00\x00\x00'

# Accessing buffer's memory address
buffer_address = arr.__array_interface__['data'][0]
print(buffer_address) #Output : 2651044743520


# ndarray object attributes :-
"""
Attributes:
T : ndarray
View of the transposed array.

data : buffer
Python buffer object pointing to the start of the array’s data.

dtype : dtype object
Data-type of the array’s elements.

flags : dict
Information about the memory layout of the array.

flat : numpy.flatiter object
A 1-D iterator over the array.

imag : ndarray
The imaginary part of the array.

real : ndarray
The real part of the array.

size : int
Number of elements in the array.

itemsize : int
Length of one array element in bytes.

nbytes : int
Total bytes consumed by the elements of the array.

ndim : int
Number of array dimensions.

shape : tuple of ints
Tuple of array dimensions.

strides : tuple of ints
(the number of bytes needed to jump to the next array element in the corresponding dimension.)
Tuple of bytes to step in each dimension when traversing an array.

ctypes : ctypes object
An object to simplify the interaction of the array with the ctypes module (row major layout).

base : ndarray
Base object if memory is from some other object.
"""

# nbytes : int => Total bytes consumed by the elements of the array.
# Example 1
import numpy as np
arr = np.array([1,2,3,4])
print(arr.nbytes) # Output 16 
print(arr.ctypes) # Output <numpy.core._internal._ctypes object at 0x0000021902B85CD0>
print(arr.dtype) # int32
# means each elements consumed 4 bytes and 32bits memory that measn dtypes int32bit

# Example 2
import numpy as np
arr = np.array([1,2,3,4], np.int64)
print(arr.nbytes) # Output 32
print(arr.ctypes) # Output <numpy.core._internal._ctypes object at 0x0000017CE66B5F10>
print(arr.dtype) # Output int64

# strides: tuple of ints => Tuple of bytes to step in each dimension when traversing an array.
import numpy as np
arr = np.array([1,2,3,4], np.int64)
print(arr.strides) #Output : (8,)

import numpy as np
arr = np.array([1])
print(np.isscalar(arr)) # Output : False

np.isscalar(3.1)
# >>> True
np.isscalar(np.array(3.1))
# >>> False
np.isscalar([3.1])
# >>> False
np.isscalar(False)
# >>> True
np.isscalar('numpy')
# >>> True


# np.array() is a function for creating NumPy arrays from existing data.
# np.ndarray is a class for creating uninitialized NumPy arrays with specific attributes.

"""
np.array() in NumPy can be considered a wrapper around the np.ndarray constructor. When you use np.array() to create a NumPy array, it simplifies the array creation process by inferring the data type and shape from the input data and providing a more user-friendly interface. Internally, np.array() uses np.ndarray to create the array.
"""

####################################################################
##################################### Question #* (Arrays)
# numpy.array() is used to convert a list into a NumPy array. The second argument (float) can be used to set the type of array elements.
# 1st method
import numpy
def arrays(arr):    
    new_arr = arr[::-1]
    result = numpy.array(new_arr, dtype=float)
    # result = numpy.array(arr[::-1], dtype=float) make even shrtoer by this line
    return result
arr = input().strip().split(' ')
result = arrays(arr)
print(result)


# 2nd method
import numpy
def arrays(arr):
    arr.reverse()
    result = numpy.array(arr, dtype=float)
    return result
arr = input().strip().split(' ')
result = arrays(arr)
print(result)

# 3rd method
import numpy
def arrays(arr):
    arr = numpy.array(arr, dtype=float)
    result = numpy.flip(arr, axis=None)
    return result
arr = input().strip().split(' ')
result = arrays(arr)
print(result)

####################################################################
######################## # * Question (Transpose and Flatten)
# numpy.transpose
"""
#*Transpose:- We can generate the transposition of an array using the tool numpy.transpose.
It will not affect the original array, but it will create a new array.
"""
# example:-
import numpy as np
arr = np.array([[1,2,3],
            [4,5,6]])
print(np.transpose(arr))
# >>> [[1 4] 
# >>>  [2 5] 
# >>>  [3 6]]

#* Flatten: The tool flatten creates a copy of the input array flattened to one dimension.
# example:-
import numpy as np
arr = np.array([[1,2,3],
            [4,5,6]])
print(arr.flatten()) # >>> [1 2 3 4 5 6]

### Question's answer
import numpy as np
N, M = map(int, input().split())
matrix_rows = []
for i in range(N):
    row = list(map(int, input().split()))
    matrix_rows.append(row)
arr = np.array(matrix_rows)
transpose_arr = arr.T
print(transpose_arr)
flatten_arr = arr.flatten()
print(flatten_arr)


####################################################################
######################## # * Question (Shape and Reshape)
# shape: The shape tool gives a tuple of array dimensions and can be used to change the dimensions of an array.
# (a). Using shape to get array dimensions
import numpy
my__1D_array = numpy.array([1, 2, 3, 4, 5])
print(my__1D_array.shape)     #(5,) -> 1 row and 5 columns

my__2D_array = numpy.array([[1, 2],[3, 4],[6,5]])
print(my__2D_array.shape)     #(3, 2) -> 3 rows and 2 columns 


# (b). Using shape to change array dimensions
import numpy
change_array = numpy.array([1,2,3,4,5,6])
change_array.shape = (3, 2)
print(change_array)     
# >>> [[1 2] 
# >>>  [3 4] 
# >>>  [5 6]]

# reshape: This tool gives a new shape to an array without changing its data. It creates a new array and does not modify the original array itself.
import numpy
my_array = numpy.array([1,2,3,4,5,6])
print(numpy.reshape(my_array(3,2)))

#Output
# [[1 2]
# [3 4]
# [5 6]]

# Question answers
import numpy as np
arr = np.array(input().split(), dtype=int).reshape(3, 3)
print(arr)

# Or
import numpy as np
print(np.reshape(numpy.array(list(map(int,input().split(' ')))),(3,3)))

####################################################################
######################## # * Question (Concatenate)
# Concatenate : Two or more arrays can be concatenated together using the concatenate function with a tuple of the arrays to be joined:
import numpy
array_1 = numpy.array([1,2,3])
array_2 = numpy.array([4,5,6])
array_3 = numpy.array([7,8,9])
print(numpy.concatenate((array_1, array_2, array_3)))

# If an array has 2D OR more, it is possible to specify the axis along which multiple arrays are concatenated. By default, it is along the first dimension.
import numpy
array_1 = numpy.array([[1,2,3],[0,0,0]])
array_2 = numpy.array([[0,0,0],[7,8,9]])
print(numpy.concatenate((array_1, array_2), axis = 1))
#Output
# [[1 2 3 0 0 0] 
#  [0 0 0 7 8 9]]


import numpy
array_1 = numpy.array([[1,2,3],[0,0,0]])
array_2 = numpy.array([[0,0,0],[7,8,9]])
print(numpy.concatenate((array_1, array_2)))

#Question answer 
# Enter your code here. Read input from STDIN. Print output to STDOUT
#1st method
import numpy
N, M, P = map(int, input().split())
N_arr = []
for _ in range(N):
    j = list(map(int, input().split()))
    N_arr.append(j)

M_arr = []       
for _ in range(M):
    k = list(map(int, input().split()))
    M_arr.append(k)    
result  = numpy.concatenate((N_arr, M_arr), axis = 0)
print(result)

#2nd method using list comprehensions
# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy
N, M, P = map(int, input().split())
N_arr = [list(map(int, input().split())) for _ in range(N)]
M_arr = [list(map(int, input().split())) for _ in range(M)]
result  = numpy.concatenate((N_arr, M_arr), axis = 0)
print(result)


# 3rd method without using concatenate method
import numpy as np
N, M, P = map(int, input().split())
result = np.array([list(map(int, input().split())) for _ in range(N + M)])
print(result)


####################################################################
######################## # * Question (Zeros and Ones)
#* Key Concept
# zeros : The zeros tool returns a new array with a given shape and type filled with 0's.
import numpy
print(numpy.zeros((1,2)))  #Default type is float
#Output : [[ 0.  0.]] 

print(numpy.zeros((1,2), dtype = numpy.int)) #Type changes to int
#Output : [[0 0]]


# ones : The ones tool returns a new array with a given shape and type filled with 1's.
import numpy
print(numpy.ones((1,2)))  #Default type is float
#Output : [[ 1.  1.]] 

print(numpy.ones((1,2), dtype = numpy.int)) #Type changes to int
#Output : [[1 1]]

# Question's answer
import numpy
arr_shape = tuple(map(int, input().split()))
print(numpy.zeros(arr_shape, dtype= int))
print(numpy.ones(arr_shape, dtype=int))


####################################################################
######################## # * Question (Zeros and Ones)
#* Key Concept:
# identity: The identity tool returns an identity array. An identity array is a square matrix with all the main diagonal elements as and the rest as The default type of elements is float.
import numpy
print(numpy.identity(3)) #3 is for  dimension 3 X 3
#Output
#>>> [[ 1.  0.  0.]
#>>> [ 0.  1.  0.]
#>>> [ 0.  0.  1.]]

# eye: 
"""
The eye tool returns a 2-D array with 1's as the diagonal and 0's elsewhere. The diagonal can be main, upper or lower depending on the optional parameter k.
A positive k is for the upper diagonal, a negative is for the lower, and a 0 k(default) is for the main diagonal.
"""
import numpy
print(numpy.eye(8, 7, k = 1))    # 8 X 7 Dimensional array with first upper diagonal 1.
#Output
"""
[[ 0.  1.  0.  0.  0.  0.  0.]
[ 0.  0.  1.  0.  0.  0.  0.]
[ 0.  0.  0.  1.  0.  0.  0.]
[ 0.  0.  0.  0.  1.  0.  0.]
[ 0.  0.  0.  0.  0.  1.  0.]
[ 0.  0.  0.  0.  0.  0.  1.]
[ 0.  0.  0.  0.  0.  0.  0.]
[ 0.  0.  0.  0.  0.  0.  0.]]
"""

import numpy
print(numpy.eye(8, 7, k = -2))   # 8 X 7 Dimensional array with second lower diagonal 1.
"""
[[0. 0. 0. 0. 0. 0. 0.] 
[0. 0. 0. 0. 0. 0. 0.] 
[1. 0. 0. 0. 0. 0. 0.] 
[0. 1. 0. 0. 0. 0. 0.] 
[0. 0. 1. 0. 0. 0. 0.] 
[0. 0. 0. 1. 0. 0. 0.] 
[0. 0. 0. 0. 1. 0. 0.] 
[0. 0. 0. 0. 0. 1. 0.]]
"""

# numpy.fromfunction
import numpy as np
def func(a,b):
    add = a + b
    return add
a = np.fromfunction(function = func(5, 6), shape= [1,2,3,4], dtype = int)
print(a)

#
import numpy as np
def func(x, y):
    return x + y
a = np.fromfunction(func, (1, 2), dtype=int)
print(a)
# >>> [[0 1]]

#* Questions answer
# 1st method
import numpy as np
np.set_printoptions(legacy = '1.13')
shape = tuple(map(int, input().split()))
print(np.eye(*shape))

# 2nd method
import numpy as np
np.set_printoptions(legacy = '1.13')
m,n = list(map(int, input().split()))
print(np.eye(m,n))

####################################################################
################################## # * Question (Array Mathematics)
#* Key concept
import numpy
a = numpy.array([1,2,3,4], float)
b = numpy.array([5,6,7,8], float)

print(a + b)                     #[  6.   8.  10.  12.]
print(numpy.add(a, b))           #[  6.   8.  10.  12.]

print(a - b)                     #[-4. -4. -4. -4.]
print(numpy.subtract(a, b))      #[-4. -4. -4. -4.]

print(a * b)                     #[  5.  12.  21.  32.]
print(numpy.multiply(a, b))      #[  5.  12.  21.  32.]

print(a / b)                     #[ 0.2         0.33333333  0.42857143  0.5       ]
print(numpy.divide(a, b))        #[ 0.2         0.33333333  0.42857143  0.5       ]

print(a % b)                     #[ 1.  2.  3.  4.]
print(numpy.mod(a, b))           #[ 1.  2.  3.  4.]

print(a**b)                      #[  1.00000000e+00   6.40000000e+01   2.18700000e+03   6.55360000e+04]
print(numpy.power(a, b))         #[  1.00000000e+00   6.40000000e+01   2.18700000e+03   6.55360000e+04]

#* Question answer
# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy
N , M = map(int,input().split())
A=[]
B=[]
for _ in range(N):
    A.append(list(map(int,input().split())))
for _ in range(N):
    B.append(list(map(int,input().split())))  
a=numpy.array(A)
b=numpy.array(B)
print(numpy.add(a,b))
print(numpy.subtract(a,b))
print(numpy.multiply(a,b))
print(numpy.floor_divide(a,b))
print(numpy.mod(a,b))
print(numpy.power(a,b))

# 2nd method USing list comprehension
import numpy
N , M = map(int,input().split())
A = [map(int,input().split()))) for _ in range(N)]
B = [map(int,input().split()))) for _ in range(N)]
a=numpy.array(A)
b=numpy.array(B)
print(numpy.add(a,b))
print(numpy.subtract(a,b))
print(numpy.multiply(a,b))
print(numpy.floor_divide(a,b))
print(numpy.mod(a,b))
print(numpy.power(a,b))


####################################################################
############################## # * Question (Floor, Ceil and Rint)
#* Key concept
"""
#* floor
The tool floor returns the floor of the input element-wise.
The floor of x is the largest integer i where i < x .

import numpy
my_array = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
print(numpy.floor(my_array))        #[ 1.  2.  3.  4.  5.  6.  7.  8.  9.]

#* ceil
The tool ceil returns the ceiling of the input element-wise.
The ceiling of x is the smallest integer i where i < x.

#* rint
import numpy
my_array = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
print numpy.rint(my_array)          #[  1.   2.   3.   4.   6.   7.   8.   9.  10.]

#* 
"""
#* Question answer
import numpy as np
np.set_printoptions(legacy='1.13')
arr = list(map(float, input().split()))
my_arr = np.array([*arr])
print(np.floor(my_arr))
print(np.ceil(my_arr))
print(np.rint(my_arr))

# 2ndmethod
import numpy as np
def apply_operations(arr, operations):
    my_arr = np.array(arr)
    results = [operation(my_arr) for operation in operations]
    return results
np.set_printoptions(legacy='1.13')
arr = list(map(float, input().split()))
operations = [
    lambda x: np.floor(x),
    lambda x: np.ceil(x),
    lambda x: np.rint(x)]
results = apply_operations(arr, operations)
for result in results:
    print(result)


####################################################################
##################################### #* Question (Sum and Prod)
#* Key concept
# sum : The sum tool returns the sum of array elements over a given axis.
import numpy
my_array = numpy.array([ [1, 2], [3, 4] ])
print(numpy.sum(my_array, axis = 0))         #Output : [4 6]
print(numpy.sum(my_array, axis = 1))         #Output : [3 7]
print(numpy.sum(my_array, axis = None))      #Output : 10
print(numpy.sum(my_array))   

# Note : By default, the axis value is None. Therefore, it performs a sum over all the dimensions of the input array.

# prod : The prod tool returns the product of array elements over a given axis.
import numpy
my_array = numpy.array([ [1, 2], [3, 4] ])
print(numpy.prod(my_array, axis = 0))            #Output : [3 8]
print(numpy.prod(my_array, axis = 1))            #Output : [ 2 12]
print(numpy.prod(my_array, axis = None))         #Output : 24
print(numpy.prod(my_array))                      #Output : 24

# Note: By default, the axis value is None. Therefore, it performs the product over all the dimensions of the input arra

#* question answer
# 1st method
import numpy as np
N, M = map(int, input().split())
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))
print(np.prod(np.sum(A, axis=0), axis=0))

# 2nd method
import numpy
N,M = list(map(int,input().split()))
arr = numpy.array([input().split() for _ in range(N)],int)
print(numpy.product(numpy.sum(arr,axis=0)))


####################################################################
##################################### #* Question (Min and Max)
#* Key concept
# min: The tool min returns the minimum value along a given axis.
import numpy
my_array = numpy.array([[2, 5], 
                        [3, 7],
                        [1, 3],
                        [4, 0]])
print(my_array.shape)
print(numpy.min(my_array, axis = 0))         #Output : [1 0]
print(numpy.min(my_array, axis = 1))         #Output : [2 3 1 0]
print(numpy.min(my_array, axis = None))      #Output : 0
print(numpy.min(my_array))                   #Output : 0

# By default, the axis value is None. Therefore, it finds the minimum over all the dimensions of the input array.

# max: The tool max returns the maximum value along a given axis.
import numpy
my_array = numpy.array([[2, 5], 
                        [3, 7],
                        [1, 3],
                        [4, 0]])
print(numpy.max(my_array, axis = 0))         #Output : [4 7]
print(numpy.max(my_array, axis = 1))         #Output : [5 7 3 4]
print(numpy.max(my_array, axis = None))      #Output : 7
print(numpy.max(my_array))

#* Question answer
# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
N, M = list(map(int, input().split()))
arr = np.array([list(map(int, input().split())) for _ in range(N)])
result = np.max(np.min(arr, axis=1))

######################################################################
################################## #* Question (Mean, Var, and Std)
#* Key concept
# mean: The mean tool computes the arithmetic mean along the specified axis.
import numpy
my_array = numpy.array([ [1, 2], [3, 4] ])
print(numpy.mean(my_array, axis = 0))        #Output : [ 2.  3.]
print(numpy.mean(my_array, axis = 1))        #Output : [ 1.5  3.5]
print(numpy.mean(my_array, axis = None))     #Output : 2.5
print(numpy.mean(my_array))                  #Output : 2.5

# Note: By default, the axis is None. Therefore, it computes the mean of the flattened array.


# var:The var tool computes the arithmetic variance along the specified axis.
import numpy
my_array = numpy.array([ [1, 2], [3, 4] ])
print(numpy.var(my_array, axis = 0))         #Output : [ 1.  1.]
print(numpy.var(my_array, axis = 1))         #Output : [ 0.25  0.25]
print(numpy.var(my_array, axis = None))      #Output : 1.25
print(numpy.var(my_array))                   #Output : 1.25

# By default, the axis is None. Therefore, it computes the standard deviation of the flattened array.
# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
N, M = list(map(int, input().split()))
arr = np.array([list(map(int, input().split())) for _ in range(N)])
print(np.mean(arr, axis = 1))
print(np.var(arr, axis = 0))
print(round(np.std(arr, axis = None), 11))

#* Question answer 
# # Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
N, M = list(map(int, input().split()))
arr = np.array([list(map(int, input().split())) for _ in range(N)])
print(np.mean(arr, axis = 1))
print(np.var(arr, axis = 0))
print(round(np.std(arr, axis = None), 11))


######################################################################
################################## #* Question (Mean, Var, and Std)
#* Key concept
# dot: The dot tool returns the dot product of two arrays.
import numpy
A = numpy.array([ 1, 2 ])
B = numpy.array([ 3, 4 ])
print(numpy.dot(A, B) )      #Output : 11

# cross : The cross tool returns the cross product of two arrays.
import numpy
A = numpy.array([ 1, 2 ])
B = numpy.array([ 3, 4 ])
print(numpy.cross(A, B))     #Output : -2

# Question answer
import numpy as np
N = int(input())
A = np.array([list(map(int, input().split())) for _ in range(N)])
B = np.array([list(map(int, input().split())) for _ in range(N)])
print(np.dot(A,B))


######################################################################
###################################### #* Question (Inner and Outer)
#* Key concept
# inner : The inner tool returns the inner product of two arrays.
import numpy
A = numpy.array([0, 1])
B = numpy.array([3, 4])
print(numpy.inner(A, B))     #Output : 4


# outer : The outer tool returns the outer product of two arrays.
import numpy
A = numpy.array([0, 1])
B = numpy.array([3, 4])
print(numpy.outer(A, B))     #Output : [[0 0]
                            #          [3 4]]

#* Question asnwer
# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
A = np.array(list(map(int, input().split())))
B = np.array(list(map(int, input().split())))
print(np.inner(A, B))     #Output : 4
print(np.outer(A, B))    #Output : [[0 0]


######################################################################
###################################### #* Question (Inner and Outer)
#* Key concept
# poly: The poly tool returns the coefficients of a polynomial with the given sequence of roots.
print(numpy.poly([-1, 1, 1, 10]))      #Output : [  1 -11   9  11 -10]

# roots: The roots tool returns the roots of a polynomial with the given coefficients.
print(numpy.roots([1, 0, -1]))           #Output : [-1.  1.]

# polyint: The polyint tool returns an antiderivative (indefinite integral) of a polynomial.
print(numpy.polyint([1, 1, 1])) #Output : [ 0.33333333  0.5         1.          0.        ]

# polyder: The polyder tool returns the derivative of the specified order of a polynomial.
print(numpy.polyder([1, 1, 1, 1]))       #Output : [3 2 1]

# polyval :The polyval tool evaluates the polynomial at specific value.
print(numpy.polyval([1, -2, 0, 2], 4))   #Output : 34

# polyfit : The polyfit tool fits a polynomial of a specified order to a set of data using a least-squares approach.
print(numpy.polyfit([0,1,-1, 2, -2], [0,1,1, 4, 4], 2))
#Output : [  1.00000000e+00   0.00000000e+00  -3.97205465e-16]

"""
#* The functions polyadd, polysub, polymul, and polydiv also handle proper addition,
#* subtraction, multiplication, and division of polynomial coefficients, respectively.
"""

#* Question's answer
import numpy
lst=list(map(float,input().split()))
b=float(input())
print(numpy.polyval(lst,b))


######################################################################
######################################## #* Question (Linear Algebra)
#* Key concept 
# linalg.det : The linalg.det tool computes the determinant of an array.
print(numpy.linalg.det([[1 , 2], [2, 1]]))       #Output : -3.0

# linalg.eig : The linalg.eig computes the eigenvalues and right eigenvectors of a square array.
vals, vecs = numpy.linalg.eig([[1 , 2], [2, 1]])
print(vals)                                      #Output : [ 3. -1.]
print(vecs)                                      #Output : [[ 0.70710678 -0.70710678]
                                                #          [ 0.70710678  0.70710678]]

# linalg.inv : The linalg.inv tool computes the (multiplicative) inverse of a matrix.
print(numpy.linalg.inv([[1 , 2], [2, 1]]))       #Output : [[-0.33333333  0.66666667]
                                                #          [ 0.66666667 -0.33333333]]
                                                
#* Question answer
# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
N = int(input())
A = np.array([list(map(float, input().split())) for _ in range(N)])
print(np.linalg.det(A))


####################################################################
#################################################### (Words Score)
####################################################################

####################################################################
################################# Question #* (Words Score)

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
N = int(input())
my_string = input().split()
my_vowels = ['a','e','i','o','u','y']
main_count = 0
for k in my_string:
    count = 0
    for j in k:
        if j in my_vowels:
            count = count + 1
        else:
            count
    if count % 2 == 0:
        main_count = main_count + 2
    else:
        main_count = main_count + 1
print(main_count)
        

# 2nd method using functions
def score_words(words):
    vowel_set = set("aeiouy")
    total_score = 0
    for word in words:
        vowel_count = 0
        for char in word:
            if char in vowel_set:
                vowel_count += 1
        if vowel_count % 2 == 0:
            total_score += 2
        else:
            total_score += 1
    return total_score

N = int(input())
my_words = input().split()
result = score_words(my_words)
print(result)

# 3rd method
def score_words(words):
    vowel_set = set("aeiouy")
    total_score = []
    for word in words:
        vowel_count = 0
        for char in word:
            if char in vowel_set:
                vowel_count += 1
        if vowel_count % 2 == 0:
            total_score.append(2)
        else:
            total_score.append(1)
    return sum(total_score)

N = int(input())
my_words = input().split()
result = score_words(my_words)
print(result)


####################################################################
################################# Question #* (Default Arguments)
class EvenStream(object):
    def __init__(self):
        self.current = 0

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

class OddStream(object):
    def __init__(self):
        self.current = 1

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return
    
def print_from_stream(n, stream=EvenStream()):
    stream.__init__()
    for _ in range(n):
        print(stream.get_next())
        
queries = int(input())
for _ in range(queries):
    stream_name, n = input().split()
    n = int(n)
    if stream_name == "even":
        print_from_stream(n)
    else:
        print_from_stream(n, OddStream())

# 2nd method
class EvenStream(object):
    def __init__(self):
        self.current = 0

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

class OddStream(object):
    def __init__(self):
        self.current = 1

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

def print_from_stream(n, stream=None):
    if stream is None:
        stream = EvenStream()
    for _ in range(n):
        print(stream.get_next())
        
queries = int(input())
for _ in range(queries):
    stream_name, n = input().split()
    n = int(n)
    if stream_name == "even":
        print_from_stream(n)
    else:
        print_from_stream(n, OddStream())






