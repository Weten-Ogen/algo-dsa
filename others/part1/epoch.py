from time import time

start_time = time()

for i in range(10):
    print(i)

stop_time = time()

running_time = stop_time - start_time

print(running_time)

