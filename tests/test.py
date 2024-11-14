import collections

def worker(f):
    tasks = collections.deque()
    value = None
    while True:
        batch = yield value
        value = None
        if batch is not None:
            tasks.extend(batch)
        else:
            if tasks:
                args = tasks.popleft()
                value = f(*args)

w = worker(str)
w.send(None)
w.send([(1,), (2,), (3,)])
# w.throw(ValueError)
w.close()
next(w)