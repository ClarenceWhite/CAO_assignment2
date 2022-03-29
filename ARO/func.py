import math
def my_func(x):
    s = math.sqrt(x)
    return s

# This verbose version shows which process in the pool is running each task. 
def my_func_verbose(x):
    s = math.sqrt(x)
    print("Task", multiprocessing.current_process(), x, s)
    return s