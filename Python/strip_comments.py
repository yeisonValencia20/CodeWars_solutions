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
import re
import codecs
def strip_comments(strng, markers):
    txt = repr(strng)[1:-1] #convert string to raw string, for escape special characters
    txt = re.sub('\\t','',txt)
    for i in markers:
        regex = '\s*\\' + i + '(\s*[#\',^.\-!@?]*[a-z]*[#\',^.\-!@?]*){1,}' 
        txt = re.sub(regex, '', txt)
    
    txt = codecs.decode(txt, 'unicode_escape') #convert to normal string
    return txt

strip_comments('\t! @ !\nstrawberries ! avocados ! = ^\noranges oranges', ["'", '=', '@', '.', '^', '#', '?', '-', '!'])