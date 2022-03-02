import math
import multiprocessing
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import logging


logging.basicConfig(filename='artifacts/medium.log', filemode='w', level=logging.INFO)
logger = logging.getLogger(__name__)


class ExecuteWithLog:
    def __init__(self, f):
        self.f = f

    def execute_f(self, v):
        logger.info(f'Calculating for {v} in {time.process_time()}')
        return self.f(v)


def integrate(f, a, b, *, n_jobs=1, n_iter=1000, pool_executor_class=ThreadPoolExecutor):
    step = (b - a) / n_iter
    points = [a + i * step for i in range(n_iter)]
    executor = pool_executor_class(max_workers=n_jobs)

    with_log = ExecuteWithLog(f)
    values = executor.map(with_log.execute_f, points)
    return sum(values) * step


def measure_time(n_jobs, pool_executor_class):
    t = time.process_time()
    logging.info(pool_executor_class.__name__)
    res = integrate(math.cos, 0, math.pi / 2, n_jobs=10, pool_executor_class=ThreadPoolExecutor)
    logging.info(res)
    passed_time = time.process_time() - t
    return f'{pool_executor_class.__name__} with {n_jobs} jobs - {passed_time} seconds'


def main():
    result = ''
    for pool_executor_class in [ThreadPoolExecutor, ProcessPoolExecutor]:
        for n_jobs in range(1, 2 * multiprocessing.cpu_count() + 1):
            result += measure_time(n_jobs, pool_executor_class) + '\n'
    with open('artifacts/medium_performance.txt', 'w') as f:
        f.write(result)


if __name__ == '__main__':
    main()
