import json

class Person(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr(self):
        return 'Person Object name: %s, age: %s' % (self.name, self.age)


if __name__=='__main__':
    p = Person('zp', 39)
    print p
