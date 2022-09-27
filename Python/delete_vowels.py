

def is_triangle(a, b, c):
    
    return abs(b - c) < a < b + c

print(is_triangle(7, 2, 2))