#testing
from fractions import Fraction
from poly1 import poly1
from poly2 import poly2
from poly3 import poly3
from poly_all import poly_all

if __name__ == '__main__':    
    x = poly_all(3, 2, [(3, 0, 5), (2, 1, 2), (1, 1, 1)], [Fraction(-1,3), Fraction(1, 7)], 6)
    x.getEstimate()
    y = poly2(3, 2, [(3, 0, 5), (2, 1, 2), (1, 1, 1)], [Fraction(-1,3), Fraction(1, 7)], 6)
    y.getEstimate()
    x1 = poly_all(3, 2, [(3, 0, 5), (2, 1, 2), (1, 1, 1)], [Fraction(-1,3), Fraction(1, 7)], 10)
    x1.getEstimate()
    y1 = poly2(3, 2, [(3, 0, 5), (2, 1, 2), (1, 1, 1)], [Fraction(-1,3), Fraction(1, 7)], 10)
    y1.getEstimate()
    x2 = poly3(5, 3, [(3, 0, 2, 5), (2, 1, 1, 2), (1, 1, 1, 1)], [Fraction(-1,3), Fraction(1, 7), Fraction(1, 2)], 6)
    x2.getEstimate()
    y2 = poly_all(5, 3, [(3, 0, 2, 5), (2, 1, 1, 2), (1, 1, 1, 1)], [Fraction(-1,3), Fraction(1, 7), Fraction(1, 2)], 6)
    x2.getEstimate()
