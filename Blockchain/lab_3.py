import string
import random
import threading
import hashlib
import time
import zlib

answer = ''
hesh_answer = ''
flag = False
locker = threading.Lock()
NUM_THREADS = 10
pool = {}

def generat_str(num):
    random.seed(num, version=2)
    global flag
    str1 = ''
    global answer
    global pool
    global hesh_answer
    thread_pool = {}
    while not flag:
        for i in range(150):
            size = random.randint(1, 9999)
            for j in range(size):
                char = random.randint(32, 126)
                str1 += chr(char)
            hashed_str = hashlib.shake_256(str1.encode('utf-8')).hexdigest(3)
            if hashed_str in thread_pool:
                locker.acquire()
                flag = True
                answer = str1
                hesh_answer = hashed_str
                locker.release()
            else:
                thread_pool[hashed_str] = str1
        locker.acquire()
        pool_set = set(pool.keys())
        thread_pool_set = set(thread_pool.keys())
        if  pool_set and  pool_set & thread_pool_set:
            flag = True
            hesh_answer = (pool_set & thread_pool_set).pop()
            answer = thread_pool[hesh_answer]
        else: 
            pool.update(thread_pool)
            thread_pool = {}
           
        locker.release()    


treads = [threading.Thread(target = generat_str, args = (time.time() + i,)) for i in range(0, NUM_THREADS)]
for thr in treads:
    thr.start()  
for thr in treads:
    thr.join()    
with open("msglab3a.txt", "w") as f:
    f.write(str(answer))
with open("msglab3b.txt", "w") as f:
    f.write(str(pool[hesh_answer]))
print(hashlib.shake_256(answer.encode('utf-8')).hexdigest(3))
print(hashlib.shake_256(pool[hesh_answer].encode('utf-8')).hexdigest(3))
