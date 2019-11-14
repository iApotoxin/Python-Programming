def triangle2(height, base):
    return 1/2 * height * base

def equilateral2(width):
    return 3**(1/2) * width * width

def isosceles2(base, sidebase):
    return base/4 * 4 * (((sidebase*sidebase) - (base*base)))**(1/2)

def pythagorean2(perpendicular):
    return 0.5 * perpendicular * perpendicular