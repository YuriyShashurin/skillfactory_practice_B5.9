##декоратор в качестве объекта класса-секундомера;
import time
class Time_this():
    def __init__(self, num_runs):
        self.num_runs = num_runs

    def __call__(self, f):
        def wrap():

            avg_time = 0
            for _ in range(self.num_runs):
                t0 = time.time()
                f()
                t1 = time.time()
                avg_time += (t1 - t0)

            avg_time /= self.num_runs
            return print("Выполнение заняло %.5f секунд" % avg_time)
        return wrap

@Time_this(10)
def f():
    for j in range(1000000):
        pass


f()