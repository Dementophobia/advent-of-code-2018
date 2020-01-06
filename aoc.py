import time
from re import findall

def get_ints(string):
    return [int(x) for x in findall(r'\d+', string)]

def read_file(name, strip = True):
    with open(f"files/input{name}") as f:
        content = f.readlines()
    if strip:
        return [x.strip() for x in content]
    return content

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        print(f"\nTime required: {(time.time() - start_time)*1000:.2f} ms\n")
        return result
    return wrapper