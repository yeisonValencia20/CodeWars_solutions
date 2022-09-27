# Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

# Examples:

# solution('abc', 'bc') # returns true
# solution('abc', 'd') # returns false

## MI CODIGO
def solution(string, ending):
    return ending in string[(len(string)-len(ending)):]

print(solution('abcde','abc'))

## MEJORA A MI CODIGO
def solution(string, ending):
    return ending in string[-len(ending):]

## CODIGO CON MEJORES PRACTICAS
def solution(string, ending):
    return string.endswith(ending)