from threading import Thread
def my_function():
    print("Printing from thread")

if __name__ == "__main__":
    t = Thread(target=my_function)
    t.start()
    t.join()
    print("Finished")
