# poly_all -  all variable polynomials
from fractions import Fraction

class poly_all:
        def __init__(self, degree, varNum, listCoeff, listofVal, digRound):
        # the input should be the degree,
        # the number of variables,
        # list of coefficients: each a tuple the length of varNum + 1
        #       the first varNum of the tuple are the degree of individual
        #       variables
        # list of values of the variables,
        # and the number of digits to round to
                self.degree = degree
                self.varNum = varNum
                self.LC = listCoeff
                self.LV = listofVal
                self.DR = digRound
                self.pr = []
                self.frac = []

        def getEstimate(self):
                def runEstimate():
                        self.pr = []
                        for i in range(self.DR):
                                self.pr.append(0)
                        x = 0
                        magnitudeLC = self.LC[0][self.varNum]
                        magnitudeLV = self.LV[0]
                        # The list of values should not be different from each other by more than a magnitude of 2.
                        for i in self.LV:
                                if(abs(magnitudeLV * 100) < abs(i) or abs(magnitudeLV / 100) > abs(i)):
                                        raise NameError("magnitude of values is larger than allowed: " + str(i))
                        for i in self.LC:
                                if(len(i) != self.varNum+1):
                                        raise NameError("length of tuple in list of coeficient is not correct: " + str(i))
                                # The list of coefficients shouldn’t be different from each other by more than 2 orders of magnitude.
                                if(abs(magnitudeLC * 100) < abs(i[self.varNum]) or abs(magnitudeLC / 100) > abs(i[self.varNum])):
                                        raise NameError("magnitude of coefficient is larger than allowed: " + str(i))
                                y = 1           # used for exact
                                z = 1           # used for rounded values
                                total = 0       # making sure degree is less than or equal to expected amount
                                for j in range(len(i)-1):
                                        y = y * (self.LV[j] ** i[j])
                                        total = total + i[j]    # degree check
                                        if(total > self.degree):
                                                raise NameError("degree is greater than expected")
                                y = y * i[len(self.LV)]
                                x = x + y
                        if(type(x) is Fraction):
                                self.pr[0] = round(x.numerator/x.denominator, 10)
                                self.frac.append(x)
                        else:
                                self.pr[0] = round(x, 10)

                        x = 0
                        for k in range(1, self.DR):
                                x = 0
                                z = z * i[len(self.LV)]
                                for i in self.LC:
                                        z = 1 # used for rounded values
                                        for j in range(len(i)-1):
                                                if(type(self.LV[j]) is Fraction):
                                                        y = round(self.LV[j].numerator/self.LV[j].denominator, k)
                                                        z = z * round((y ** i[j]), self.DR)
                                                else:
                                                        z = z * (self.LV[j] ** i[j])
                                        z = z * i[len(self.LV)]
                                        x = x + z
                                self.pr[k] = round(x, 10)
                        print(self.pr)
        #runEstimate()        
        # run check to see if all condition met - which function to use,
        # all variable present, etc. Make sure there are no errors
                if(len(self.LV) != self.varNum):
                        raise NameError("Amount of values does not match the number of variables")
                elif(10 < self.DR or self.DR < 1):
                        raise NameError("Choose a different digit to round to: should be between 1 and 10")
                else:
                        runEstimate()
        def printEQ(self):
                print(self.degree)
                print(self.varNum)
                print(self.LC)
                print(self.LV)
                print(self.DR)
        def printExact(self):
                print(self.frac)
                print(round(self.frac[0].numerator/self.frac[0].denominator, 10))


    

if __name__ == '__main__':    
    x = poly_all(3, 2, [(3, 0, 5), (2, 1, 2), (1, 1, 1)], [Fraction(-1,3), Fraction(1, 7)], 6)
    x.getEstimate()

    
