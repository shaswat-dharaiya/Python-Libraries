class newClass:
    def __init__(self,range):
        self.range = range
        print("The range is: {}".format(self.range))

    def __iter__(self):
        for i in range(self.range):
            print("lol: {}".format(i))

a = newClass(10)
for i in a:
    print(i)
