class ExampleClass:
    a = 1
    def __init__(self , val = 2):
        self.b = val


example_object = ExampleClass()

print(hasattr(example_object, 'b'))
print(hasattr(example_object, 'a'))
print(hasattr(ExampleClass, 'b'))
print(hasattr(ExampleClass, 'a'))

print(ExampleClass.__dict__)
example_object = ExampleClass(2)



print(ExampleClass.__dict__)
print(example_object.__dict__)
print(type(example_object).__name__)
print(type(example_object).__module__)
print(ExampleClass.__bases__)





class ExampleClass2:
    __counter = 0
    def __init__(self, val = 1):
        self.__first = val
        ExampleClass.__counter += 1


example_object_1 = ExampleClass2()
example_object_2 = ExampleClass2(2)
example_object_3 = ExampleClass2(4)

print(example_object_1.__dict__, example_object_1._ExampleClass__counter)
print(example_object_2.__dict__, example_object_2._ExampleClass__counter)
print(example_object_3.__dict__, example_object_3._ExampleClass__counter)













class MyClass:
    def __init__(self , val = 2):
        self.b = val

class MyClass2(MyClass):
    def __init__(self , val = 2):
        super().__init__(val)


obj = MyClass()
obj2 = obj
obj.a = 1
obj.b = 2
obj.i = 3
obj.ireal = 3.5
obj.integer = 4
obj.z = 5


def incIntsI(obj):
    for name in obj.__dict__.keys():
        if name.startswith('i'):
            val = getattr(obj, name)
            if isinstance(val, int):
                setattr(obj, name, val + 1)


print(obj.__dict__)
incIntsI(obj)
print(obj.__dict__)

print(issubclass(MyClass2,MyClass))
print(isinstance(obj, MyClass))
print(obj2 is obj)
    

#polymorphism  The word comes from Greek (polys: "many, much" and morphe, "form, shape"),

class One:
    def do_it(self):
        print("do_it from One")

    def doanything(self):
        self.do_it()


class Two(One):
    def do_it(self):
        print("do_it from Two")


one = One()
two = Two()

one.doanything()
two.doanything()