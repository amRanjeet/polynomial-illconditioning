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

    def getEstimate(self):
        def runEstimate():
            self.pr = []
            for i in range(self.DR +1):
                self.pr.append(0)
            x = 0
            for j in range(len(self.LC)+1):
                if(len (self.LC[j]) != varNum+1):
                    raise NameError("length of tuple in list of coeficient is not correct in index: " + j)
                z = self.LC[j]
                total = 0
                for i in range(varNum):
                    total =  total + z[i]
                    if(total > degree):
                        raise NameError("degree is greater than expected")
                    self.LV[i] ** z[i]
                    
                self.pr[0] = self.pr[0] + self.LC[j] * (self.LV[0]**(self.degree - j))
                for i in range(self.DR):
                    if(type(self.LV[0]) is Fraction):
                        x = round(self.LV[0].numerator/self.LV[0].denominator, i)
                    else:
                        x = self.LV[0]
                    self.pr[i+1] = self.pr[i+1] + self.LC[j] * round((x**(self.degree - j)), self.DR)
            self.pr[0] = round(self.pr[0].numerator/self.pr[0].denominator, 10)
            print(self.pr)
        #runEstimate()        
        # run check to see if all condition met - which function to use,
        # all variable present, etc. Make sure there are no errors
        if(len(self.LV) != self.varNum):
            raise NameError("Amount of values does not match the number of variables")
        elif(10 < self.DR or self.DR < 1):
            raise NameErroe("Choose a different digit to round to: should be between 1 and 10")
        else:
            runEstimate()
    
