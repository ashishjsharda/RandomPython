import threading

def print_numbers():
    for i in range(10):
        print(i)

def print_letters():
    for letter in ['a', 'b', 'c', 'd', 'e']:
        print(letter)

# Create threads
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

# Start threads
t1.start()
t2.start()

# Wait for threads to complete
t1.join()
t2.join()
