# Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

# * url = "http://github.com/carbonfive/raygun" -> domain name = "github"
# * url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
# * url = "https://www.cnet.com"                -> domain name = cnet"

# MI CODIGO
def domain_name(url):
    return url.replace('www.','').replace('https://','').replace('http://','').split('.')[0]



# CODIGO CON MEJORES PRACTICAS
def domain_name(url):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]

import re
def domain_name(url):
    return re.search('(https?://)?(www\d?\.)?(?P<name>[\w-]+)\.', url).group('name')

def domain_name(url):
    from re import findall, VERBOSE
    
    try:
        url = findall("""\A
                        (?: http
                        s?
                        ://)?         # matches http:// or https:// or nothing
                        
                        (?: www.)?    # matches www. or nothing
                        
                        ([- a-z]+)    # matches a sequence of letters and dashes
                        
                        (?: .com|.ru)     # matches either .com or .ru
                        (?: [/ a-z]+)?    # matches a sequence or letters and slashes
                        \Z""", url, VERBOSE)
        return url[0]
    except:
        return "Invalid URL."