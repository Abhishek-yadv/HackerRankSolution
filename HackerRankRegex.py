####################################################################
#################################################### (Introduction)
####################################################################

####################################################################
############################# Question1 #* Matching Specific String
# Regular expression (or RegEx) A regular expression is a sequence of characters that define a search pattern, mainly used for string pattern matching.
"""
Task :
You have a test string . Your task is to match the string hackerrank. This is case sensitive.
"""
import re
Regex_Pattern = r'hackerrank'  # Do not delete 'r'.

Test_String = input()
match = re.findall(Regex_Pattern, Test_String)
print("Number of matches :", len(match))

####################################################################
###################### Question 2 #* Matching Anything But a Newline
# dot: The dot (.) matches anything (except for a newline).
"""
Task :
You have a test string S.
Your task is to write a regular expression that matches only and exactly strings of form: abc.def.ghi,
where each variable a,b,c,d,e,f,g,h,i,j,k,x can be any single character except the newline.
"""
regex_pattern = r"^(.{3}\.?){4}$"	# Do not delete 'r'.
# regex_pattern = r"^...\....\....\....$"

import re
import sys
test_string = input()
match = re.match(regex_pattern, test_string) is not None
print(str(match).lower())

####################################################################
#################### Question 3 #* Matching Anything But a Newline
#* The expression \d matches any digit [0-9].
# * The expression \D matches any character that is not a digit.
"""
Task :
You have a test string S. Your task is to match the pattern xxXxxXxxxx 
Here x denotes a digit character, and X denotes a non-digit character.
"""
Regex_Pattern = r"[0-9]{2}[^0-9][0-9]{2}[^0-9][0-9]{4}"	# Do not delete 'r'.
# Regex_Pattern = r"\d{2}[^0-9]\d{2}[^0-9]\d{4}"
# Regex_Pattern = r"\d{2}\D\d{2}\D\d{4}"

import re
print(str(bool(re.search(Regex_Pattern, input()))).lower())
# TestCase : 06-11-2015

####################################################################
##### Question 4 #* Matching Whitespace & Non-Whitespace Character
#* \s matches any whitespace character [ \r\n\t\f ].
#* \S matches any non-white space character.
"""
Task :
You have a test string S. Your task is to match the pattern XXxXXxXX
Here, x denotes whitespace characters, and X denotes non-white space characters.
"""
Regex_Pattern = r"\S{2}\s\S{2}\s\S{2}"	# Do not delete 'r'.

import re
print(str(bool(re.search(Regex_Pattern, input()))).lower())


####################################################################
##### Question 5 #* Matching Whitespace & Non-Whitespace Character
#* \w The expression \w will match any word character. Word characters include alphanumeric characters (a-z, A-Z and 0-9) and underscores (_).
"""
#* \W matches any non-word character.Non-word characters include characters other than alphanumeric characters (a-z, A-Z and 0-9) and underscore (_). 
Task :
You have a test string S. Your task is to match the pattern xxxXxxxxxxxxxxXxxx
Here, x denotes any word character and X denotes any non-word character.
"""
Regex_Pattern = r"\w{3}\W\w{10}\W\w{3}"	# Do not delete 'r'.

import re
print(str(bool(re.search(Regex_Pattern, input()))).lower())


####################################################################
############################ Question 6 #* Matching Start & End
#* The ^ symbol matches the position at the start of a string.
#* The $ symbol matches the position at the end of a string.
"""
Task :
You have a test string S. Your task is to match the pattern Xxxxx
Here, x denotes a word character, and X denotes a digit.
S must start with a digit and end with . symbol.
S should be 6 characters long only.
"""
Regex_Pattern = r"^\d\w{4}\.$"	# Do not delete 'r'.

import re
print(str(bool(re.search(Regex_Pattern, input()))).lower())


####################################################################
################################################# (Character Class)
####################################################################

########################################################################
############################ Question 1 #* Matching Specific Characters
#* The character class [] matches only one out of several characters placed inside the square brackets.
"""
You have a test string S. Your task is to write a regex that will match S with following conditions:

S must be of length: 6
First character: 1, 2 or 3
Second character: 1, 2 or 0
Third character: x, s or 0
Fourth character: 3, 0 , A or a
Fifth character: x, s or u
Sixth character: . or ,
"""
Regex_Pattern = r'^[123][120][xs0][30Aa][xsu][\.\,]$'	# Do not delete 'r'.

import re
print(str(bool(re.search(Regex_Pattern, input()))).lower())


#########################################################################
############################ Question 2 #* Excluding Specific Characters
#* The negated character class [^] matches any character that is not in the square brackets.
"""
Task

You have a test string S.
Your task is to write a regex that will match S with the following conditions:

S must be of length 6.
First character should not be a digit (1,2,3,4,5,6,7,8,9 or 0).
Second character should not be a lowercase vowel (a,e,i,o or u).
Third character should not be b, c, D or F.
Fourth character should not be a whitespace character ( \r, \n, \t, \f or <space> ).
Fifth character should not be a uppercase vowel (A,E,I,O or U).
Sixth character should not be a . or , symbol.
"""
Regex_Pattern = r'^\D[^aeiou][^bcDF][^\s][^AEIOU][^.,]$'	# Do not delete 'r'.

import re
print(str(bool(re.search(Regex_Pattern, input()))).lower())



#########################################################################
############################ Question 3 #* Matching Character Ranges
#* A hyphen (-) inside a character class specifies a range of characters

"""
a character class is a set of characters enclosed within square brackets that allows you to match one character in the set.
A hyphen (-) inside a character class specifies a range of characters where the left and right operands are the respective lower and upper bounds of the range.
For example:
[a-z] equal to abcdefghijklmnopqrstuvwxyz
[A-Z] equal to ABCDEFGHIJKLMNOPQRSTUVWXYZ
[0-9] is equal to 0123456789


Task :
Write a RegEx that will match a string satisfying the following conditions:

The string's length is >= 5 .
The first character must be a lowercase English alphabetic character.
The second character must be a positive digit. Note that we consider zero to be neither positive nor negative.
The third character must not be a lowercase English alphabetic character.
The fourth character must not be an uppercase English alphabetic character.
The fifth character must be an uppercase English alphabetic character.
"""

Regex_Pattern = r'^[a-z][1-9][^a-z][^A-Z][A-Z]$'	# Do not delete 'r'.

import re
print(str(bool(re.search(Regex_Pattern, input()))).lower())




import string
print(string.__all__)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)
print(dir(string))

import math
print(dir(math))