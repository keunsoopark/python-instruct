class MultipleIterator:
    def __init__(self, stop, multiple):
        self.current = 0
        self.stop = stop
        self.multiple = multiple

    def __iter__(self):
        return self

    def __next__(self):
        self.current = self.current + self.multiple
        if self.current < self.stop:
            return self.current
        else:
            raise StopIteration


for i in MultipleIterator(20, 3):
    print(i, end=' ')

print()
for i in MultipleIterator(30, 5):
    print(i, end=' ')
