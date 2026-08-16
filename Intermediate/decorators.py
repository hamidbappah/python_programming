# decorator: wrap extra behaviour
import time
def timed(fn):
    def wrapper(*a, **kw):
        t = time.time()
        out = fn(*a, **kw)
        print(fn.__name__, time.time()-t)
        return out
    return wrapper

@timed
def train_model():
    print("trainingmodel")
