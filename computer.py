class computer:
    def __init__(self,cpu,ram,storage):
        self.cpu=cpu
        self.ram=ram
        self.storage=storage

    def config(self):
        print(self.cpu)
        print(self.ram)
        print(self.storage)

com1=computer("i5","16gb","1tb")
com1.config()
"""
com2=computer("i7","8gb")
com2.config()
com3=computer("i9","24gb")
com3.config()
"""
