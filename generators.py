class fibiterator:
    def __init__(self, a=1, b=0, maxvalue=50):
        self.a =a
        self.b =b
        self.maxvalue =maxvalue

    def __iter__(self):
        return self

    def __next__(self):
        n = self.a +self.b
        if n > self.maxvalue:
            raise StopIteration
        self.a = self.b