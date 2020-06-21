import time
def time_this(num_runs):
    def decorator(func):
        def wrap():

            avg_time = 0
            for _ in range(num_runs):
                t0 = time.time()
                func()
                t1 = time.time()
                avg_time += (t1 - t0)

            avg_time /= num_runs
            return print("Выполнение заняло %.5f секунд" % avg_time)
        return wrap
    return decorator


@time_this(10)
def f():
    for j in range(1000000):
        pass

f()