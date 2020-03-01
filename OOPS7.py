class visualstudio():
    def execute(self):
        print("compliling")
        print("Running")

class Pycharm():
    def execute(self):
        print("Spell check")
        print("conventions")
        print("compiling ")
        print("running")

class laptop:
    def code(self,ide):
        ide.execute()

ide = Pycharm()

s1 = laptop()
s1.code(ide)