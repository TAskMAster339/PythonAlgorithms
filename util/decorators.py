__all__ = ["timer"]

import functools
import time


def timer(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        start = time.perf_counter_ns()
        result = f(*args, **kwargs)
        print(f"Time: {(time.perf_counter_ns() - start) / (10**9):.7f}s")
        return result

    return wrapper
