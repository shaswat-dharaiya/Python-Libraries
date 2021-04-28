from functools import wraps

def my_logger(orignal_fn):
  import logging
  logging.basicConfig(filename='{}.log'.format(orignal_fn.__name__), level =logging.INFO)

  @wraps(orignal_fn)
  def wrapper(*args, **kwargs):
      logging.info(
        'Ran with args: {}, and kwargs: {}'.format(args,kwargs))
      return orignal_fn(*args,**kwargs)

  return wrapper

def my_timer(orignal_fn):
    import time

    @wraps(orignal_fn)
    def wrapper(*args,**kwargs):
        t1 = time.time()
        res = orignal_fn(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(orignal_fn.__name__, t2))
        return res
    return wrapper

import time

@my_logger
@my_timer
def display_info(name,age):
    time.sleep(1)
    print('3')
    print('Display Info fn ran w/ args ({} & {})'.format(name,age))

# print(display_info.__name__)

display_info('Shaswat', 23)
