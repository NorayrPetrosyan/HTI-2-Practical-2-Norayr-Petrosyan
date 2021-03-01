import time

def warn_slow(func):
    def inner(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        duration = time.time() - start
        if duration > 2:
            if args:
                print(f"execution of {func.__name__} with {args} arguments took more than 2 seconds.")
            elif kwargs:
                print(f"execution of {func.__name__} with {kwargs} arguments took more than 2 seconds.")
            else:
                print(f"execution of {func.__name__} with no arguments took more than 2 seconds.")

        return result

    return inner

@warn_slow
def func_slow(x, y):
    time.sleep(3)

@warn_slow
def func_fast(x, y):
    print(x, y)

func_slow(1, 2)
func_fast(1, 2)