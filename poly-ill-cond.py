# polynomial illconditioning

class poly:
    def __init__(self, degree, varNum, listCoeff, listofVal, digRound):
        self.degree = degree
        self.varNum = varNum
        self.LC = listCoeff
        self.LV = listofVal
        self.DR = digRound
        

    def getEstimate(self):
        # run check to see if all condition met - which function to use,
        # all variable present, etc. Make sure there are no errors
        if(self.degree != len(self.LC)):
            raise NameError("Degree and length of the list of Coefficient do not match")
        


