import time           

def time_decorator(func):
    def wrapper():
        start_time = time.time()
        res = func()
        end_time = time.time()
        delta = end_time - start_time
        print(int(delta))
        return res
    return wrapper

@time_decorator
def sleep_1_sec():
    time.sleep(1)
    print("function")
    return 25


if __name__ == '__main__':
    result = sleep_1_sec()
    print(result)