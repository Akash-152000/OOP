class A:

    def __init__(self):
        print("init of A")

    def feature1(self):
        return print("Feature one ")

    def feature2(self):
        print("Feature two ")

class B():
    def __init__(self):
        print("init of B")

    def feature3(self):
        print("Feature three ")

    def feature4(self):
        print("Feature four ")

class C(A,B):
    def __init__(self):
        super().__init__()
        print("init of C")

    def feature4(self):
        print("Feature four ")

    def feature5(self):
        print("Feature five ")


s1 = C()
s1.feature1()
