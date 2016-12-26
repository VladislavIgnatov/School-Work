import threading
import os
import time
import queue

def byte_counter(value, filename, start, end):
    count = 0
    with open(filename, "rb") as f:
        f.seek(start)
        byte = f.read(1)
        while byte != b"" and f.tell() <= end:
            if byte == value:
                count += 1
            byte = f.read(1)
    workQueue.put(count)

if __name__ == "__main__":
    #Search Value
    value = b'\x11'

    #Search filename
    filename = "1381171523547.jpg"

    #Queue
    workQueue = queue.Queue(4)

    # Size of the search file
    sizeoffile = os.stat(filename).st_size
    position = int(sizeoffile/4)
    position2 = position *2
    position3 = position *3
    
    # NOT Threaded
    t = time.time()
    byte_counter(value, filename, 0, sizeoffile)
    t = time.time() - t
    # Adding the total count
    total = 0
    while not workQueue.empty():
        total += workQueue.get()
    print("Threading count: " + str(total) + " Time : " + str(t))
    
    # Threading
    t = time.time()
    t1 = threading.Thread(target=byte_counter,args=(value, filename, 0, position))
    t2 = threading.Thread(target=byte_counter,args=(value, filename, position, position2))
    t3 = threading.Thread(target=byte_counter,args=(value, filename, position2, position3))
    t4 = threading.Thread(target=byte_counter,args=(value, filename, position3, sizeoffile))
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t = time.time() - t
    # Adding the total count
    total = 0
    while not workQueue.empty():
        total += workQueue.get()
    print("Threading count: " + str(total) + " Time : " + str(t))


