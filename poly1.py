# polynomial illconditioning
# poly 1 take any polynomial of any degree with one variable
from fractions import Fraction

class poly1:
    def __init__(self, degree, varNum, listCoeff, listofVal, digRound):
        self.degree = degree
        self.varNum = varNum
        self.LC = listCoeff
        self.LV = listofVal
        self.DR = digRound
        self.pr = []
        

    def getEstimate(self):
        def runEstimate():
            self.pr = []
            for i in range(self.DR+1):
                self.pr.append(0)
            x = 0
            for j in range(self.degree+1):
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
        if(self.degree != len(self.LC)-1):
            raise NameError("Degree and length of the list of Coefficient do not match")
        elif(self.varNum != 1):
            raise NameError("Incorrect polynomal class used.")
        elif(len(self.LV) != 1):
            raise NameError("Amount of values does not match the number of variables")
        elif(10 < self.DR or self.DR < 1):
            raise NameErroe("Choose a different digit to round to: should be between 1 and 10")
        else:
            runEstimate()


if __name__ == '__main__':    
    x = poly1(3, 1, [1, 3, 2, 5], [Fraction(-1,3)], 10)
    x.getEstimate()
    y = poly1(2, 1, [1, -1, 0], [Fraction(-1,3)], 10)
    y.getEstimate()
