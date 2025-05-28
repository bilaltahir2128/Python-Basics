import threading
import time

def sleeper(no, sec):
    print(f"Thread {no} sleeping for {sec} seconds.")
    time.sleep(sec)
    print(f"Thread {no} woke up after {sec} seconds.")

threads = []

for i in range(5):
    t = threading.Thread(target=sleeper, args=(i, i + 1))  
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("All threads have finished.")
