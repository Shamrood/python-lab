class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return(self.length*self.breadth)
    def compare(self,other):
        if self.area()==other.area():
            return True
        else:
            return False
r1=rectangle(3,9)
r2=rectangle(3,5)
comp=r1.compare(r2)
if comp:
    print("area is same")
else:
    print ("area is not same")
r1.area()
r2.area()
print("area of r1",r1.area())
print("area of r2",r2.area())
