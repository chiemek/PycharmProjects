import re
# text = '''
# 123.456.7890
# 321-654-0987
#
# '''
# pattern = re.compile('\b\b\b.\b\b\b.\b\b\b\b ')  #here we put in what we want to search for
# matches = pattern.finditer(text)   # here we put the variable that contain it
#
# for match in matches:
#     print(match)

# . = all character except new lines
# \d = digit of 0-9
# \D = digit of not 0-9
# \w = word character, a-z A_Z 0-9 _
# \W = not word character
# \s = whitespace, tab, newline
# \S = not whitespace,tab, newline
# \b = starts with wordboundary it can be whitespace or alphanumeric characters  we use it like this  (r'\bha') this means that any ha that have word boundary before it
# \B = not word boundary
# ^ = beginning of strings note ^ is used like this (r'^emeka') this will search for emeka in the beginning of the sentence
# [^a-zA-Z]= this will match everything that is not character in the file you are matching
# [^b]at = this will match everything that have at but dont have b in the front
# $ = end of the string  $ is used like this (r'emeka$') this will search for emeka in the end of the sentence
# [] = matches more than one character set, example [.-]  here we want to match charater with - and .  note characterset matches only 1 character at a time.
# [] you can use it to match [89]00 this means that you want to match characters that have 800 and 900 as the beginning./
# [1-5] this will work as a range of values
# [a-zA-Z] this will work as range from a to z
# | = matches either or   this works as or (r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*)  this is used to match mr mrs ms.
# () = group this allows us to match several different characters. if we want to
# * = zero or more
# + = 1 or more
# ? = zero or 1
# ?=  means zero width indexing it is used to specify that the stuffs in the front can appear anywhere in the password
# {3} = exact number this means how many numbers you want to match eg re.compile(r'\d{3}.\d{3}.\d{4}') this is used for phone numbers
# {3,4} = range of number minimium, maximium

email = "Meku-s1085@gmail.com"
urls = '''
https://www.google.com
http://coreyms.com
http://whatsapp.com
'''
# reg = re.compile(r'\b[\w|.|-]+@[\w|.|-]+[\w{2-4}]$')
reg = re.compile(r'\b[\w]+:/+[\w.]+\.[\w{2-4}]+')
final = reg.finditer(urls)

for word in final:
    print(word)
