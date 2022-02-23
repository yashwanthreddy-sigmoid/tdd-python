class area:

    def areaofsquare(self,side):

        if side < 0:
            raise Exception("Bad Input")
        else:
            return side*side



    def fromfile(self,filename):
        f=open(filename,"r")
        line=f.readline()
        return line

