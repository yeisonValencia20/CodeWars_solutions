# Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace at the end of the line should also be stripped out.

# Example:

# Given an input string of:

# apples, pears # and bananas
# grapes
# bananas !apples
# The output expected would be:

# apples, pears
# grapes
# bananas
# The code would be called like so:

# result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# # result should == "apples, pears\ngrapes\nbananas"
# MI CODIGO
import re
import codecs
def strip_comments(strng, markers):
    txt = repr(strng)[1:-1] #convert string to raw string, for escape special characters
    txt = re.sub('\\t','',txt)
    for i in markers:
        regex = '\s*\\' + i + '(\s*[#\',^.\-!@?=]*[a-z]*[#\',^.\-!@?=]*){1,}' 
        txt = re.sub(regex, '', txt)
    
    txt = codecs.decode(txt, 'unicode_escape') #convert to normal string
    return txt

strip_comments('\t! @ !\nstrawberries ! avocados ! = ^\noranges oranges', ["'", '=', '@', '.', '^', '#', '?', '-', '!'])


#CODIGO CON MEJORES PRACTICAS
def solution(string,markers):
    parts = string.split('\n')
    for s in markers:
        parts = [v.split(s)[0].rstrip() for v in parts]
    return '\n'.join(parts)

def strip_line(line, markers):
    for m in markers:
        if m in line:
            line = line[:line.index(m)]
    return line.rstrip()
def solution(string,markers):
    stripped = [strip_line(l, markers) for l in string.splitlines()]
    return '\n'.join(stripped)

def strip_comments(strng, markers):
    for num, marker in enumerate(markers):
        strng = '\n'.join([i.split(marker)[0].rstrip() for i in strng.split('\n')])

    return strng