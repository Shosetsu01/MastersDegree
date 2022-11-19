import string
import random
import re
import threading
import hashlib as h
import time


ans = ''
flag = False
locker = threading.Lock()
NUM_THREADS = 1

def generat_str(num):
    random.seed(num, version=2)
    global flag
    str1 = ''
    global ans
    while not flag:
        char = random.randint(32, 126)
        str1 += chr(char)
        hashed_str = h.sha256(str1.encode('utf-8')).hexdigest()
        if re.search(r"^000[\w]*1$", hashed_str) is not None :
            locker.acquire()
            flag = True
            ans = str1
            locker.release()


if __name__ == '__main__':
    treads = [threading.Thread(target = generat_str, args = (time.time() + i,)) for i in range(0, NUM_THREADS)]
    for thr in treads:
        thr.start()  
    for thr in treads:
        thr.join()    
    with open("msg.txt", "w") as f:
        f.write(ans)

    print(h.sha256(ans.encode('utf-8')).hexdigest())
    print("finish")