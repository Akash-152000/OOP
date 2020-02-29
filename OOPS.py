class computer:

    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram

    def config(self):
        print("cpu is", self.cpu)
        print("ram is", self.ram)


class phone:

    def __init__(self, camera, processor):
        self.cpu = camera
        self.ram =processor

    def config(self):
        print("camera is", self.cpu)
        print("processor is", self.ram)

com1=computer('i5',16)
com2=phone('60gb','snapdragon')


com1.config()
com2.config()

