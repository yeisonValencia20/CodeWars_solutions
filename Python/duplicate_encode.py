# The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string, or ")" if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.

# Examples
# "din"      =>  "((("
# "recede"   =>  "()()()"
# "Success"  =>  ")())())"
# "(( @"     =>  "))((" 

## MI CODIGO
def duplicate_encode(word):
    word = word.lower()
    word_replaced = list(word)
    for i in word:
        indices = [index for index, x in enumerate(list(word)) if x == i]
        if(len(indices) > 1):
            for index in indices:
                word_replaced[index] = ')'

        else:
            word_replaced[indices[0]] = '('

    return ''.join(word_replaced)

print(duplicate_encode("uCdnwhkkTDXoMcZg)!)qwprW!r)oT wwn(jBYVN"))


## CODIGO CON MEJORES PRACTICAS
def duplicate_encode(word):
    return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])
    

import collections
def duplicate_encode(word):
    new_string = ''
    word = word.lower()
    #more info on defaultdict and when to use it here:
    #http://stackoverflow.com/questions/991350/counting-repeated-characters-in-a-string-in-python
    d = collections.defaultdict(int)
    for c in word:
        d[c] += 1
    for c in word:
        new_string = new_string + ('(' if d[c] == 1 else ')')
    return new_string