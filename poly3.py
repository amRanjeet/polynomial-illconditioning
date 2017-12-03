from fractions import Fraction

class poly3:
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
            for i in range(self.DR):
                self.pr.append(0)
            w = 0
            x = 0
            y = 0
            for j in range(len(self.LC)):
                if(len (self.LC[j]) != self.varNum+1):
                    raise NameError("length of tuple in list of coeficient is not correct in index: " + str(j))
                z = self.LC[j]
                if(z[0] + z[1] + z[2] > self.degree):
                    raise NameError("degree is greater than expected")
                    
                self.pr[0] = self.pr[0] + z[3] * (self.LV[0]**(z[0])) * (self.LV[1]**(z[1])) *(self.LV[2]**(z[2]))
                for i in range(1,self.DR):
                    if(type(self.LV[0]) is Fraction):
                        w = round(self.LV[0].numerator/self.LV[0].denominator, i)
                        x = round(self.LV[1].numerator/self.LV[1].denominator, i)
                        y = round(self.LV[2].numerator/self.LV[2].denominator, i)
                    else:
                        raise NameError("you are not using fractions for the list of values")
                        w = self.LV[0]
                    self.pr[i] = round( (self.pr[i] + z[3] *
                                           round((w**(z[0])), self.DR) *
                                           round((x**(z[1])),self.DR) *
                                           round((y**(z[2])),self.DR)), 10)
            self.pr[0] = round(self.pr[0].numerator/self.pr[0].denominator, 10)
            print(self.pr)
        #runEstimate()        
        # run check to see if all condition met - which function to use,
        # all variable present, etc. Make sure there are no errors
        if(len(self.LV) != 3):
            raise NameError("Number of values given in the list of Coefficient does not match the expected amount")
        elif(10 < self.DR or self.DR < 1):
            raise NameError("Choose a different digit to round to: should be between 1 and 10")
        else:
            runEstimate()
    
if __name__ == '__main__':    
    x = poly3(5, 3, [(3, 0, 2, 5), (2, 1, 1, 2), (1, 1, 1, 1)], [Fraction(-1,3), Fraction(1, 7), Fraction(1, 2)], 6)
    x.getEstimate()
