import hashlib
import imp
import yadisk
import json
import os.path
from datetime import datetime, timezone
BLOCK_SIZE = 65536 


def compare(a, b):
    cnt = 0
    for el1, el2 in zip(a, b):
        cnt += 1 if el1 == el2 else 0

    return (f'идентичных элементов {cnt} в', a, b) 


def hash(msg):
    hashedList.append(hashlib.sha256(msg.encode('utf-8')).hexdigest())


def chek_hash(file_path, disk_path):
    file_hash = hashlib.sha256() 
    with open(file_path, 'rb') as f: 
        fb = f.read(BLOCK_SIZE) 
        while len(fb) > 0: 
            file_hash.update(fb) 
            fb = f.read(BLOCK_SIZE)
    print(y.get_meta(disk_path).sha256)
    print(file_hash.hexdigest())
    print(y.get_meta(disk_path).sha256 == file_hash.hexdigest())
    
    return y.get_meta(disk_path).sha256 == file_hash.hexdigest()


def chek_upload(file_path, disk_path): 
    if y.get_meta(disk_path).modified > datetime.fromtimestamp(os.path.getmtime(file_path), timezone.utc):
        return False
    return True   


def synchronization(file_path, disk_path):
    if y.exists(disk_path):
        if not chek_hash(file_path, disk_path):
            if  chek_upload(file_path, disk_path):
                y.upload(file_path, disk_path, overwrite=True)
                
            else:
                y.download(disk_path, file_path)
                
    else:
        y.upload(file_path, disk_path)


y = yadisk.YaDisk(token="y0_AgAAAABkbXYjAAhmPgAAAADOV1UZCUOZWUHgS9SC_ik7wDTzQBrFlJk")

msgList = ["ahkhfsnfskohrljfldjf", "iogknilnrehvexljpoer", "zvdgdawaadfggwjcvfdh", "oifdgodhfgclvpojrlldslsdfjlhkvnkfgienv"]
msgListNext = ["iogknilnrehvexljpoer", "fdggfdgdfgdfgfdgfdgf", "bhkhkbkhbhkbhhkbkkbh", "oifdgodhfgclvpojrlldslsdfjlhkvnkfgienv"]
hashedList = []

file_path = '/Users/romaryin/Downloads/Blockcheyn.docx'
disk_path = 'block/Blokcheyn.docx'


if __name__ == '__main__':
    for msg in msgList:
        hash(msg)
    
    print("\n first 4 hash", hashedList[0:4])

    for msg in msgListNext:
        hash(msg)

    print("\n second 4 hash", hashedList[4:8])

    for a, b in zip(hashedList[0:4], hashedList[4:8]):
        print("\n compare", *compare(a, b))

    print("\n hashed list", hashedList)
    
    if os.path.exists(file_path) and y.check_token():
        synchronization(file_path, disk_path)
        print("\n finish")
    else: print("\n obshibka")

