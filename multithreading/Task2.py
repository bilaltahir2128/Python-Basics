import threading
import time

def sleeper(no, sec):
    print(f"Thread {no} sleeping for {sec} seconds.")
    time.sleep(sec)
    print(f"Thread {no} woke up.")

threads = []

for i in range(5):
    t = threading.Thread(target=sleeper, args=(i, i + 1))
    threads.append(t)
    t.start()
    print(f"Active threads after starting thread {i}: {threading.active_count()}")

for t in threads:
    t.join()

print(f"Final active thread count (should be 1): {threading.active_count()}")
print("All threads have finished.")
