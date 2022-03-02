import time
from threading import Thread
from multiprocessing import Process

from hw_1.top_fibonacci_numbers import top_fibonacci_numbers

N = 100_000


def measure_time(function, *args):
    t = time.process_time()
    function(*args)
    return time.process_time() - t


def fibonacci_synchronized(n):
    for _ in range(10):
        top_fibonacci_numbers(n)


def fibonacci_threading(n):
    threads = [Thread(target=top_fibonacci_numbers, args=(n, )) for _ in range(10)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()


def fibonacci_multiprocessing(n):
    threads = [Process(target=top_fibonacci_numbers, args=(n, )) for _ in range(10)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()


def main():
    result = f'''Synchronized:
{measure_time(fibonacci_synchronized, N)} seconds
Threading:
{measure_time(fibonacci_threading, N)} seconds
Multiprocessing:
{measure_time(fibonacci_multiprocessing, N)} seconds
'''
    with open('artifacts/eazy_performance.txt', 'w') as f:
        f.write(result)


if __name__ == '__main__':
    main()
