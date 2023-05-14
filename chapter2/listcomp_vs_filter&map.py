from contextlib import contextmanager
import time


@contextmanager
def timer(*args, **kwargs):
    mnt1 = time.perf_counter()
    try:
        yield mnt1
    finally:
        mnt2 = time.perf_counter()
        print(mnt2 - mnt1)


symbols = "$¢£¥€¤^*&$%#(*))@**(^##JklNJKDBJDBJ&*(&*4848"

with timer():
    beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]

print(f'listcomp:\n\t{beyond_ascii}')

with timer():
    beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))

print(f'filter & map:\n\t{beyond_ascii}')
