import math
question = '''
https://www.testdome.com/d/python-interview-questions/9 
 
2. Quadratic EquationARITHMETIC   Easy 
Implement the function find_roots to find the roots of the quadratic equation: ax2 + bx + c = 0. The function should return a tuple containing roots in any order. If the equation has only one solution, the function should return that solution as both elements of the tuple. The equation will always have at least one solution.

The roots of the quadratic equation can be found with the following formula: A quadratic equation.

For example, find_roots(2, 10, 8) should return (-1, -4) or (-4, -1) as the roots of the equation 2x2 + 10x + 8 = 0 are -1 and -4.

'''


def find_roots(a, b, c):
    delta = (b * b) - (4 * a * c)
    if delta >= 0:
        radicaldelta = math.sqrt(delta)
    else:
        radicaldelta = math.sqrt(delta * -1) * 1j
    x1 = (-1 * b + radicaldelta)/(2 * a)
    x2 = (-1 * b - radicaldelta)/(2 * a)
    
    if x1.imag == 0:
        strx = (x1) 
    else:
        strx =   (x1.real) + (x1.imag)* 1j

     
    if x2.imag == 0:
        stry = (x2) 
    else:
        stry = (x2.real) + (x2.imag) * 1j

    strf = (strx, stry)
    return strf


print(find_roots(1, 2, 1))
