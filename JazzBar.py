class Constructor:
    def __init__(self, name = None):
        self.name = name
        print('Work at Constructor')

    def display(self):
        if self.name:
            print('Hi, I am ' + self.name)
        else:
            print('Hi, I am without name')

    def __del__(self):
        print(self.name, 'destroyed')

x = Constructor()

x.display()
y = Constructor('Navin')

y.display()
del x, y