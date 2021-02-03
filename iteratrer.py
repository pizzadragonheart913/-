class myenumerate:
    def __init__(self,data):
        self.data = data
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.data) -1 :
            raise StopIteration

        self.index = self.index + 1
        return self.index, self.data[self.index]

b = myenumerate('abc')

for index, letter in b:
    print(f"{index} : {letter}")