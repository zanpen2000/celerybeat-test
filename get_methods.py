

def method_a():
    """ma"""
    pass


def method_b():
    """mb"""
    pass


def get_method():
    m = __import__(__name__)

    for x in dir(m):
        att = getattr(m, x)
        if att and hasattr(att, 'func_name'):

            print att.func_name, att.__doc__

    return [x for x in dir(m) if x.startswith('method')]

if __name__=='__main__':
    m = get_method()
    print m
