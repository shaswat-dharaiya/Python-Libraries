# def outer_fn(msg):
#     def inner_fn():
#         print(msg)
#     return inner_fn
#
# hi_fn = outer_fn('Hi')
# bye_fn = outer_fn('Bye')
#
# hi_fn()
# bye_fn()

def decorator_fn(orignal_fn):
    import time
    def wrapper_fn(*args, **kwargs):
        print('1')
        print('wrapper executed this before \'{}\' method'.format(orignal_fn.__name__))
        time.sleep(1)
        return orignal_fn(*args, **kwargs)
    time.sleep(1)
    return wrapper_fn

class decorator_class(object):
    def __init__(self,orignal_fn):
        self.orignal_fn = orignal_fn

    def __call__(self, *args, **kwargs):
        print('1')
        print('call executed this before \'{}\' method'.format(self.orignal_fn.__name__))
        return self.orignal_fn(*args, **kwargs)

@decorator_fn
def display():
    print('2')
    print('Display fn ran')


# decorator_disp = decorator_fn(display)
display()

# @decorator_class
@decorator_fn
def display_info(name,age):
    print('3')
    print('Display Info fn ran w/ args ({} & {})'.format(name,age))

display_info('Shaswat', 23)
