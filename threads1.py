from threading import Thread

def my_function(thread_num):
    print(f"Hello from thread {thread_num}!")

if __name__ == "__main__":
    num_threads = 10
    threads = [Thread(target=my_function, args=(i+1,)) for i in range(num_threads)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    print(f"Total threads: {num_threads}")
