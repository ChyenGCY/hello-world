#1. import the multiprocessing package
import time, multiprocessing

# process_one
def process_one(num):
    for i in range(num):
        print('yong gan niuniu')
        time.sleep(0.5)
# process_two
def process_two(num):
    for i in range(num):
        print("bu pa kunnan")
        time.sleep(0.5)

if __name__ == '__main__':
# 2. create the process object by the process class
    process1 = multiprocessing.Process(target=process_one,args=(3))
    process2 = multiprocessing.Process(target=process_two,kwargs={"num": 2})

# 3. use start to execute the process
    process1.start()
    process2.start()
