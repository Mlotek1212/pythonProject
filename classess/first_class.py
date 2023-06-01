class MyClassBase:
    """A simple example class"""
    i = 12345

    def hello(self):
        return 'hello world'

    def print(self):
        print(self.i)


class MyClass(MyClassBase):
    i = 980

    def hello(self):
        return 'hello Bartek'


base = MyClassBase()
obj = MyClass()
breakpoint()
...
