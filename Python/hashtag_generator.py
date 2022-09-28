# The marketing team is spending way too much time typing in hashtags.
# Let's help them with our own Hashtag Generator!

# Here's the deal:

# It must start with a hashtag (#).
# All words must have their first letter capitalized.
# If the final result is longer than 140 chars it must return false.
# If the input or the result is an empty string it must return false.
# Examples
# " Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
# "    Hello     World   "                  =>  "#HelloWorld"
# ""                                        =>  false

# MI CODIGO
def generate_hashtag(s):
    if(len(s) > 140 or len(s) < 0):
        return False
    return '#'+''.join([word.capitalize() for word in s.split(' ')])

generate_hashtag(" Hello there thanks for trying my Kata")


#CODIGO CON MEJORES PRACTICAS
def generate_hashtag(s):
    output = "#"
    
    for word in s.split():
        output += word.capitalize()
    
    return False if (len(s) == 0 or len(output) > 140) else output

def generate_hashtag(s):
    ans = '#'+ str(s.title().replace(' ',''))
    return s and not len(ans)>140 and ans or False

def generate_hashtag(s): return '#' +s.strip().title().replace(' ','') if 0<len(s)<=140 else False