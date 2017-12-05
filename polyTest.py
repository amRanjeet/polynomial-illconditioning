#testing
from fractions import Fraction
from poly1 import poly1
from poly2 import poly2
from poly3 import poly3
from poly_all import poly_all
import random


def generateRandPoly():
    polyLst = []
    value = []
    a = random.randint(1,100)   # number of variables
    b = random.randint(1,200)   # degree
    d = random.randint(1,100)
    for j in range(d):
        y = []
        c = 0
        for i in range(a):
            if (c >= b):
                z = 0
            else:
                z = Fraction(random.randint(1,10),random.randint(1,10))
                if(z + c > b):
                    z = 0
            c = c + z
            y.append(z)
        y.append(random.randint(1,100))
        polyLst.append(list(y))
    for i in range(a):
        value.append(Fraction(random.randint(1,10), random.randint(1,10)))
    return poly_all(b, a, polyLst, value, 10)

if __name__ == '__main__':
##    x = poly1(3, 1, [1, 3, 2, 5], [Fraction(-1,3)], 10)
##    x.getEstimate()
##    y = poly1(2, 1, [1, -1, 0], [Fraction(-1,3)], 10)
##    y.getEstimate()
##    x = poly_all(3, 2, [(3, 0, 5), (2, 1, 2), (1, 1, 1)], [Fraction(-1,3), Fraction(1, 7)], 6)
##    x.getEstimate()
##    y = poly2(3, 2, [(3, 0, 5), (2, 1, 2), (1, 1, 1)], [Fraction(-1,3), Fraction(1, 7)], 6)
##    y.getEstimate()
##    x1 = poly_all(3, 2, [(3, 0, 5), (2, 1, 2), (1, 1, 1)], [Fraction(-1,3), Fraction(1, 7)], 10)
##    x1.getEstimate()
##    y1 = poly2(3, 2, [(3, 0, 5), (2, 1, 2), (1, 1, 1)], [Fraction(-1,3), Fraction(1, 7)], 10)
##    y1.getEstimate()
##    x2 = poly3(5, 3, [(3, 0, 2, 5), (2, 1, 1, 2), (1, 1, 1, 1)], [Fraction(-1,3), Fraction(1, 7), Fraction(1, 2)], 6)
##    x2.getEstimate()
##    y2 = poly_all(5, 3, [(3, 0, 2, 5), (2, 1, 1, 2), (1, 1, 1, 1)], [Fraction(-1,3), Fraction(1, 7), Fraction(1, 2)], 6)
##    y2.getEstimate()
##    x3 = poly_all(7, 3, [(4, 3, 0, 1), (2,0,2,4), (0,4,3,10), (1,1,0,5)], [Fraction(1,17), Fraction(2,3), Fraction(1,9)], 10)
##    x3.getEstimate()
##    x4 = poly_all(7, 4,[(4,0,0,0,5), (0, 4, 2, 0, 7), (0,0,4,2,2), (4, 0, 0, 3, 6), (1, 1, 1, 1, 7)],[Fraction(1,13), Fraction(5, 18), Fraction(2,3), Fraction(6,7)], 10)
##    x4.getEstimate()
##    x5 = poly_all(7, 4,[(-4,0,0,0,5), (0, 4, 2, 0, 7), (0,0,4,2,2), (4, 0, 0, 3, 6), (1, 1, 1, 1, 7)],[Fraction(1,13), Fraction(5, 18), Fraction(2,3), Fraction(6,7)], 10)
##    x5.getEstimate()
##    x = poly_all(28, 7, [(1, 1, 1, 1, 1, 1, 1, 2), (2, 0, 0, 6, 0, 0, 0, 7), (0, 3, 0, 4, 0, 0, 2, 3), (0, 0, 10, 15, 0, 3, 0, 7), (1, 0, 0, 0, 0, 0, 5, 9), (0, 2, 0, 1, 0, 3, 0, 2)], [Fraction(1, 2), Fraction(2, 3), Fraction(1, 4), Fraction(19, 5), Fraction(1, 6), Fraction(5, 7), Fraction(1, 8)], 10)
##    x.getEstimate()
##    x.printExact()
##    x7 = poly_all(7, 4,[(-4,0,0,0,5), (0, 4, 2, 0, 7), (0,0,4,2,2), (4, 0, 0, 3, 6), (1, 1, 1, 1, 7)],[Fraction(1,8), Fraction(1,8), Fraction(1,8), Fraction(1,8)], 10)
##    x7.getEstimate()

#    randPoly = generateRandPoly()
#    randPoly.printEQ()
#    randPoly.getEstimate()
    
