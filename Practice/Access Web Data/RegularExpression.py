import re

# A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
# RegEx can be used to check if a string contains the specified search pattern.

# RegEx Module
# Python has a built-in package called re, which can be used to work with Regular Expressions.
# Import the re module : import re

# RegEx in Python
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)  # Check if the string starts with "The" and ends with "Spain":
if x:
    print("YES! We have a match!")
else:
    print("No Match")

# #### RegEx Functions ####
print("\nRegEx Functions : ")
"""
findall(), search(), split(), sub()
"""

# The findall() Function
# The findall() function returns a list containing all matches.
# The list contains the matches in the order they are found.If no matches are found, an empty list is returned:
txt = "The rain in Spain"
x = re.findall("ai", txt)  # Return a list containing every occurrence of "ai":
print(x)

txt = "The rain in Spain"
x = re.findall("Portugal", txt)  # Check if "Portugal" is in the string:
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match")

# The search() Function
# The search() function searches the string for a match, and returns a Match object if there is a match.
# If there is more than one match, only the first occurrence of the match will be returned:
txt = "The rain in Spain"
x = re.search("\s", txt)
print("The first white-space character is located in position:", + x.start())

# If no matches are found, the value None is returned:
txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)

# The split() Function
# The split() function returns a list where the string has been split at each match
txt = "The rain in Spain"
x = re.split("\s", txt)  # Split the string at every white-space character:
print(x)

# You can control the number of occurrences by specifying the maxsplit parameter:
txt = "The rain in Spain"
x = re.split("\s", txt, 1)  # Split the string at the first white-space character:
print(x)

# The sub() Function
# The sub() function replaces the matches with the text of your choice:
txt = "The rain in Spain"
x = re.sub("\s", "9", txt)  # Replace all white-space characters with the digit "9":
print(x)

# You can control the number of replacements by specifying the count parameter:
txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)  # Replace the first two occurrences of a white-space character with the digit 9:
print(x)

# #### Match Object ####
print("\nMatch Object : ")
# A Match Object is an object containing information about the search and the result.
# If there is no match, the value None will be returned, instead of the Match Object.
txt = "The rain in Spain"
x = re.search("ai", txt)  # The search() function returns a Match object:
print(x)

# The Match object has properties and methods used to retrieve information about the search, and the result:
"""
.span() returns a tuple containing the start-, and end positions of the match
.string returns the string passed into the function
.group() returns the part of the string where there was a match
"""

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)

# Print the position (start- and end-position) of the first match occurrence.
print(x.span())  # Search for an upper case "S" character in the beginning of a word, and print its position:

# Print the string passed into the function:
print(x.string)  # The string property returns the search string:

# Print the part of the string where there was a match.
print(x.group())  # Search for an upper case "S" character in the beginning of a word, and print the word:

# #### Metacharacters ####
print("\nMatch Characters : ")

# []	A set of characters	"[a-m]"
txt = "The rain in Spain"
x = re.findall("[a-m]", txt)  # Find all lower case characters alphabetically between "a" and "m":
print(x)

# \	Signals a special sequence (can also be used to escape special characters)	"\d"
txt = "That will be 59 dollars"
x = re.findall("\d", txt)  # Find all digit characters:
print(x)

# .	Any character (except newline character)	"he..o"
txt = "hello world"
x = re.findall("he..o", txt)  # Search for a sequence starts with "he", followed by any two characters, and an "o":
print(x)

# ^	Starts with	"^hello"
txt = "hello world"
x = re.findall("^hello", txt)  # Check if the string starts with 'hello':
if x:
    print("Yes, the string starts with 'hello'")
else:
    print("No match")

# $	Ends with	"world$"
txt = "hello world"
x = re.findall("world$", txt)  # Check if the string ends with 'world':
if x:
    print("Yes, the string ends with 'world'")
else:
    print("No match")

# *	Zero or more occurrences	"aix*"
txt = "The rain in Spain falls mainly in the plain!"
x = re.findall("aix*", txt)  # Check if the string contains "ai" followed by 0 or more "x" characters:
print(x)

if x:
    print("Yes, there is at least one match!")
else:
    print("No match")

# +	One or more occurrences	"aix+"
txt = "The rain in Spain falls mainly in the plain!"
x = re.findall("aix+", txt)  # Check if the string contains "ai" followed by 1 or more "x" characters:
print(x)

if x:
    print("Yes, there is at least one match!")
else:
    print("No match")

# {}	Exactly the specified number of occurrences	"al{2}"
txt = "The rain in Spain falls mainly in the plain!"
x = re.findall("al{2}", txt)  # Check if the string contains "a" followed by exactly two "l" characters:
print(x)

if x:
    print("Yes, there is at least one match!")
else:
    print("No match")

# |	Either or	"falls|stays"
txt = "The rain in Spain falls mainly in the plain!"
x = re.findall("falls|stays", txt)  # Check if the string contains either "falls" or "stays":
print(x)

if x:
    print("Yes, there is at least one match!")
else:
    print("No match")

# ()	Capture and group

# #### Special Sequences ####
# A special sequence is a \ followed by one of the characters in the list below, and has a special meaning:
print("\nSpecial Sequences : ")

# \A	Returns a match if the specified characters are at the beginning of the string	"\AThe"
txt = "The rain in Spain"
x = re.findall("\AThe", txt)  # Check if the string starts with "The":
print(x)

if x:
    print("Yes, there is a match!")
else:
    print("No match")

# \b	Returns a match where the specified characters are at the beginning or at the end of a word
# (the "r" in the beginning is making sure that the string is being treated as a "raw string")
# r"\bain" or r"ain\b"
txt = "The rain in Spain"
x = re.findall(r"\bain", txt)  # Check if "ain" is present at the beginning of a WORD:
print(x)

if x:
    print("Yes, there is at least one match!")
else:
    print("No match")

x = re.findall(r"ain\b", txt)  # Check if "ain" is present at the end of a WORD:
print(x)

if x:
    print("Yes, there is at least one match!")
else:
    print("No match")

# \B	Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
# (the "r" in the beginning is making sure that the string is being treated as a "raw string")
# r"\Bain" or r"ain\B"
txt = "The rain in Spain"
x = re.findall(r"\Bain", txt)  # Check if "ain" is present, but NOT at the beginning of a word:
print(x)

if x:
    print("Yes, there is at least one match!")
else:
    print("No match")

x = re.findall(r"ain\B", txt)  # Check if "ain" is present, but NOT at the end of a word:
print(x)

if x:
    print("Yes, there is at least one match!")
else:
    print("No match")

# \d	Returns a match where the string contains digits (numbers from 0-9)	"\d"
txt = "The rain in Spain"
x = re.findall("\d", txt)  # Check if the string contains any digits (numbers from 0-9):
print(x)

if x:
    print("Yes, there is at least one match!")
else:
    print("No match")

# \D	Returns a match where the string DOES NOT contain digits	"\D"
txt = "The rain in Spain"
x = re.findall("\D", txt)  # Return a match at every no-digit character:
print(x)

if x:
    print("Yes, there is at least one match!")
else:
    print("No match")

# \s	Returns a match where the string contains a white space character	"\s"
txt = "The rain in Spain"
x = re.findall("\s", txt)  # Return a match at every white-space character:
print(x)

if x:
    print("Yes, there is at least one match!")
else:
    print("No match")

# \S	Returns a match where the string DOES NOT contain a white space character	"\S"
txt = "The rain in Spain"
x = re.findall("\S", txt)  # Return a match at every NON white-space character:
print(x)

if x:
    print("Yes, there is at least one match!")
else:
    print("No match")

# \w	Returns a match where the string contains any word characters     "\w"
# (characters from a to Z, digits from 0-9, and the underscore _ character)
txt = "The rain in Spain"
x = re.findall("\w", txt)  # Return a match at every word character (a to Z, 0-9,underscore(_)):
print(x)

if x:
    print("Yes, there is at least one match!")
else:
    print("No match")

# \W	Returns a match where the string DOES NOT contain any word characters	"\W"
txt = "The rain in Spain"
x = re.findall("\W",
               txt)  # Return a match at every NON word character (NOT between a and Z. Like "!", "?" white-space etc.):
print(x)

if x:
    print("Yes, there is at least one match!")
else:
    print("No match")

# \Z	Returns a match if the specified characters are at the end of the string	"Spain\Z"
txt = "The rain in Spain"
x = re.findall("Spain\Z", txt)  # Check if the string ends with "Spain":
print(x)

if x:
    print("Yes, there is at least one match!")
else:
    print("No match")

# #### Sets ####
# A set is a set of characters inside a pair of square brackets [] with a special meaning:
print("\nSet : ")

# [arn]	Returns a match where one of the specified characters (a, r, or n) are present
txt = "The rain in Spain"
x = re.findall("[arn]", txt)  # Check if the string has any a, r, or n characters:
print(x)

if x:
    print("Yes, there is at least one match!")
else:
    print("No match")

# [a-n]	Returns a match for any lower case character, alphabetically between a and n
txt = "The rain in Spain"
x = re.findall("[a-n]", txt)  # Check if the string has any characters between a and n:
print(x)

if x:
    print("Yes, there is at least one match!")
else:
    print("No match")

# [^arn]	Returns a match for any character EXCEPT a, r, and n
txt = "The rain in Spain"
x = re.findall("[^arn]", txt)  # Check if the string has other characters than a, r, or n:
print(x)

if x:
    print("Yes, there is at least one match!")
else:
    print("No match")

# [0123]	Returns a match where any of the specified digits (0, 1, 2, or 3) are present
txt = "The rain in Spain"
x = re.findall("[0123]", txt)  # Check if the string has any 0, 1, 2, or 3 digits:
print(x)

if x:
    print("Yes, there is at least one match!")
else:
    print("No match")

# [0-9]	Returns a match for any digit between 0 and 9
txt = "8 times before 11:45 AM"
x = re.findall("[0-9]", txt)  # Check if the string has any digits:
print(x)

if x:
    print("Yes, there is at least one match!")
else:
    print("No match")

# [0-5][0-9]	Returns a match for any two-digit numbers from 00 and 59
txt = "8 times before 11:45 AM"
x = re.findall("[0-5][0-9]", txt)  # Check if the string has any two-digit numbers, from 00 to 59:
print(x)

if x:
    print("Yes, there is at least one match!")
else:
    print("No match")

# [a-zA-Z]	Returns a match for any character alphabetically between a and z, lower case OR upper case
txt = "8 times before 11:45 AM"
x = re.findall("[a-zA-Z]", txt)  # Check if the string has any characters from a to z lower case, and A to Z upper case:
print(x)

if x:
    print("Yes, there is at least one match!")
else:
    print("No match")

# [+]	In sets, +, *, ., |, (), $,{} has no special meaning,
# so [+] means: return a match for any + character in the string
txt = "8 times before 11:45 AM"
x = re.findall("[+]", txt)  # Check if the string has any + characters:
print(x)

if x:
    print("Yes, there is at least one match!")
else:
    print("No match")

# The match Function:
line = "Cats are smarter than dogs"

matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)

if matchObj:
    print("matchObj.group() : ", matchObj.group())
    print("matchObj.group(1) : ", matchObj.group(1))
    print("matchObj.group(2) : ", matchObj.group(2))
else:
    print("No match!!")
print()

# Matching Versus Searching:
# match checks for a match only at the beginning of the string,
# while search checks for a match anywhere in the string.

mystr = """A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
        RegEx can be used to check if a string contains the specified search pattern."""
patt = re.compile(r'Reg')
matches = patt.finditer(mystr)
for match in matches:
    print(match)
print(mystr[2:5])
print(mystr[12:15])
print(mystr[97:100])

"""
The 'r' in front tells Python the expression is a raw string. In a raw string, escape sequences are not parsed. 
For example, '\n' is a single newline character. ... Raw strings are handy in regex, in which the backslash 
is used often for its own purposes.
Prefixing with an r merely indicates to the string that backslashes '\' should be treated literally and not as 
escape characters for python.
"""

r = "<p>Please click <a href=\"http://www.dr-chuck.com\">here</a></p>"
print(re.findall('href="(.+)"', r))
