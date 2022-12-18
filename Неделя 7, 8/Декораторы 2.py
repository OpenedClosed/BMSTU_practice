from functools import wraps
from inspect import getcallargs
import datetime

def logging_decorator(logger):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            func_args = getcallargs(func, *args, **kwargs)
            time = datetime.datetime.now()
            res = func(*args, **kwargs)
            logger.append({
                'name': func.__name__,
                'arguments': func_args,
                'call_time': time,
                'result': res
            })
            return res
        return wrapper
    return decorator

if __name__ == '__main__':

    logger = []

    @logging_decorator(logger)
    def test_simple(a, b=2):
        return 127

    test_simple(1)

    print(logger)