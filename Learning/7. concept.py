Namespace, CGroup (control groups), and Union file-system are the basic building blocks of a container

https://medium.com/@sonalijain0605/linux-kernel-component-to-provide-containerization-54c66e9ed392#:~:text=In%20summary%2C%20namespaces%20provide%20process,lightweight%20and%20shareable%20container%20images.


Docker is an open-source platform that allows you to develop, ship, and run applications in isolated environments called containers. Containers package an application along with all its dependencies, ensuring that it runs consistently across different computing environments.

Key Concepts of Docker
Containers – Lightweight, portable, and self-sufficient environments that run applications with all required dependencies.
Images – A snapshot of a container that includes the application and its dependencies.
Dockerfile – A script that defines how to build a Docker image.
Docker Hub – A public repository where you can find and share Docker images.
Docker Compose – A tool that allows you to define and run multi-container applications.

Why Use Docker?
Portability: Runs on any system that supports Docker (Windows, Mac, Linux).
Consistency: Eliminates "works on my machine" issues.
Scalability: Easily scale applications up or down.
Efficiency: Uses fewer resources than traditional virtual machines.


Docker
------------
Docker Images
A Docker image is a blueprint for creating Docker containers. It contains everything required to run an application:

The application itself
Dependencies
The environment settings
Configuration files
An image is immutable, meaning it doesn't change once it's created. You can think of an image as a snapshot of a filesystem at a particular point in time.


Docker Containers
-----------------------
A Docker container is a running instance of a Docker image. While an image is a static file, a container is a live, executable instance that contains everything needed to run the application.

A container runs the application in a fully isolated environment, with its own filesystem, networking, and process space.
Containers are lightweight and use the host OS's kernel, but they are isolated from the host system and other containers.

How Containers Are Isolated
Filesystem Isolation: Each container has its own isolated filesystem, which is created from the Docker image. Changes inside a container don’t affect the host system or other containers.
Process Isolation: Each container has its own process space. It runs independently, so it can have its own processes and resources.
Network Isolation: Containers can communicate with each other through Docker’s networking, but they are isolated from the host and other containers by default.

*
https://medium.com/@knoldus/unionfs-a-file-system-of-a-container-2136cd11a779
A container is nothing but a process. In Linux, the only way to create a new process is forking the existing process.
The fork operation creates a separate address space for the child. The child process has an exact copy of all the memory segments of the parent process.
In order to create a new container, all the files of image layers would be copied into container namespace.
A container is expected to start in a few milliseconds. If a huge payload is needed to be copied at the time of starting a container it increases the bootstrap time of a container.

So, here we need some mechanism to efficiently share physical memory segments among containers. In order to address these challenges listed above, Union Capable File Systems came into existence.


Docker Daemon
---------------
The Docker daemon is a background process that manages Docker containers and images. It listens for Docker API requests and handles tasks like building, running, and managing containers.

It manages the lifecycle of containers (start, stop, remove, etc.)
The Docker daemon runs on the host machine and manages containers on that system.


Benefit
-------
Benefits of Docker
Portability: Docker containers can run on any system that supports Docker, regardless of the underlying operating system or environment.
Consistency: Developers can be confident that the application will run the same way in any environment (e.g., dev, test, production).
Isolation: Containers provide process and resource isolation, allowing applications to run without interfering with each other.
Efficiency: Containers are lightweight compared to virtual machines because they share the host system’s kernel.
Scalability: Docker containers are easy to scale horizontally across multiple hosts using tools like Kubernetes.



Beind the hood
-------------
1. Namespaces:

Namespaces provide isolation for processes. Docker uses various namespaces to give each container its own isolated space for processes, network, user IDs, and more. Common namespaces used by Docker include:

· PID Namespace: Isolates the process ID number space.

· Network Namespace: Isolates the network interfaces.

· Mount Namespace: Isolates the filesystem mount points.

· UTS Namespace: Isolates the hostname and domain name.

2. cgroups (Control Groups):

cgroups allow the allocation of resources, such as CPU, memory, disk I/O, and network, among a set of processes.
Docker uses cgroups to limit and isolate resource usage for containers.
For example, you can specify the CPU shares, memory limits, and other resource constraints for a container using cgroups.

3. Union FS
Union File System:

The Union File System, also known as UnionFS, is a file system service that enables file layers to be stacked as layers. Docker uses a union file system to create images as a series of layers. Each layer represents changes to the filesystem, and these layers can be shared among multiple containers to save disk space. Common union file systems used by Docker include:

OverlayFS: This is the default union file system driver in Docker for Linux.

Aufs (Advanced Multi-Layered Unification Filesystem): Was historically used as the default driver in earlier versions of Docker but has been deprecated in favor of OverlayFS.

DeviceMapper, Btrfs, and others: Alternative union file system drivers that can be configured based on the host system and requirements.

In summary, namespaces provide process isolation, cgroups enable resource control, and union file systems facilitate the creation of lightweight and shareable container images. Docker leverages these Linux kernel features to create isolated and efficient container environments, allowing developers to package and distribute applications with their dependencies in a consistent and reproducible manner.


Linux
--------
Q1. if multiple users run an intensive application in your linux server. what should i do

Combining Both for Comprehensive Resource Management:

You can combine both tools for comprehensive resource management. For instance:
Use ulimit to set process-specific limits (e.g., file descriptor limits or process count limits).
Use cgroups to manage broader resource usage across multiple processes or applications.

Create cgroups for each user or application: You can create separate cgroups for each user or application and set appropriate resource limits.

For example, create a memory cgroup for user1:

sudo mkdir /sys/fs/cgroup/memory/user1_cgroup
sudo echo 2G > /sys/fs/cgroup/memory/user1_cgroup/memory.limit_in_bytes
Then, assign user1's processes to this cgroup:

sudo echo <PID> > /sys/fs/cgroup/memory/user1_cgroup/tasks
Similarly, you can create cgroups for CPU and I/O limits.


Q2. Find files with extension

find /path/to/directory -type f -name "*.extension"
find . -type d -name "*.txt"

- Find files and directories with names containing .config (case-insensitive):
find . -iname "*.config"
find /path/to/directory -name "*study*"

- To remove files with a specific extension from a folder (and its subfolders) in Linux, you can use the find command along with -exec to delete them.
find /path/to/directory -type f -name "*.extension" -exec rm {} \;
or

Explanation of the -exec part:
{} is a placeholder for each file found by find. It gets replaced by the actual file path.
\; marks the end of the -exec command. You need to escape the semicolon (\;) with a backslash to prevent it from being interpreted by the shell.


find /path/to/dir -name "*.txt" | xargs rm
find /path/to/dir -name "*.txt" | xargs -I {} cp {} /path/to/destination/

--How do u move a file from a src folder to a destination folder
And what if the destination folder is in an diff server

When moving a file to a different server, you need to copy the file over the network first, and then delete the original from the source location.

Here’s how you can do it using scp (Secure Copy Protocol), which is commonly used for copying files between systems:

mv /home/user/source/file.txt /home/user/destination/

1. Using scp to Copy and Remove the File:
scp /home/user/source/file.txt user@192.168.1.100:/home/user/destination/
This command copies file.txt from the local server to the remote server with IP 192.168.1.100.

After copying, you can remove the original file from the source directory if you want to move the file (not just copy it):

rm /home/user/source/file.txt

Using rsync for More Control:
rsync is another powerful tool that can be used for copying files, with more flexibility and options, such as preserving file permissions and resuming interrupted transfers. The syntax for rsync is:

rsync -avz /path/to/source/file user@destination_server:/path/to/destination/folder/
-a: Archive mode (preserves file attributes).
-v: Verbose (provides details about the transfer).
-z: Compresses file data during the transfer.


-- Search a folder
find /path/to/search -type f -name "filename"

Decorators in Python
A decorator in Python is a function that modifies the behavior of another function or class without changing its code.
It allows for reusable and readable modifications to functions, such as logging, access control, or memoization.

========================
Q1. Python List


Yes, Python lists can hold any data type, including integers, strings, objects, and even other lists.
This is because Python lists are heterogeneous, meaning they can store elements of different types in a single list.
The primary reason for this flexibility is that Python is a dynamically-typed language,
which allows variables (including list elements) to change types during runtime.

Why can Python lists hold any data type?
Dynamic Typing:

Python is dynamically typed, meaning you don’t need to declare the type of a variable (or list element) when you create it.
The interpreter determines the type at runtime. This allows lists to store elements of different types without needing
to explicitly define their types.
Object References:

In Python, everything is an object. Whether it's an integer, string, list, or custom class, all are objects.
A list doesn't hold the actual value of each element directly but instead holds references (or pointers) to the objects.
This is why a list can store a reference to any type of object without issues.


Flexible Memory Allocation:
-------------------------------------+
Python’s memory model allows lists to store objects in a flexible manner. A list doesn’t care about the internal
structure of the objects it contains, so you can mix types in the same list.

Q2. Deepcopy vs Reference Copy
While reference copying is efficient, there are cases where you may want to actually duplicate the object, such as when you need to make changes to one object without affecting the other. In this case, you'd use a deep copy, which copies the entire object along with all its nested objects.

Reference Copy: Fast and memory efficient (only copies the reference).
Deep Copy: Slower and more memory-intensive (copies the entire object and its contents).

Q3 Dynamic Array (List)
Dynamic Array Mechanism
Unlike static arrays, which have a fixed size, dynamic arrays can grow or shrink as needed. Here’s how Python achieves this with its list implementation:

Initial Allocation: When you create a list, Python allocates a certain amount of memory for it. This memory might be more than what is immediately required to store the initial elements of the list, providing space for the list to grow.
Automatic Resizing: As elements are added to a Python list, it checks whether the underlying array’s current allocation is sufficient to accommodate the new elements. If there isn’t enough space, Python creates a new, larger array. It then copies the elements from the old array to the new one and finally adds the new elements. This process is known as “resizing” or “reallocating memory.”
Growth Factor: The size to which a Python list grows with each reallocation is governed by a growth factor, which is a balance between too much and too little memory allocation. The growth factor for Python lists has typically been around 1.125 (though this can vary by implementation), meaning that each time the list needs to grow, it increases its size by approximately 12.5%. This strategy aims to minimize the number of memory reallocations (which are expensive operations) while also avoiding the over-allocation of memory.


Q4 Immutable vs mutable:
In summary, immutability leads to faster performance mainly because:

Memory is used more efficiently.
There's less overhead for resizing and modifying the structure.
Immutable objects can be cached, reducing the need to create new instances.
They are inherently thread-safe, reducing the need for synchronization.
These factors make immutable objects like tuples faster, especially when dealing with large collections or concurrent environments.
However, if you need to modify the collection, mutable objects like lists are still necessary despite the performance trade-offs.

Q5 abstract base class
An Abstract Base Class (ABC) in Python is a class that defines a common interface for its subclasses
but cannot be instantiated itself. It enforces that any subclass must implement certain methods.

Q6 Python threading
import threading

# create a thread
t1 = threading.Thread(target, args)

# start a thread
t1.start()

# Wait for the thread
t1.join()


import threading


def print_cube(num):
    print("Cube: {}" .format(num * num * num))


def print_square(num):
    print("Square: {}" .format(num * num))


if __name__ =="__main__":
    t1 = threading.Thread(target=print_square, args=(10,))
    t2 = threading.Thread(target=print_cube, args=(10,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Done!")

----------------------
from concurrent.futures import ThreadPoolExecutor

def task(n):
    return n * n

# Create a thread pool with 3 threads
with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(task, [1, 2, 3, 4, 5])

print(list(results))  # Output: [1, 4, 9, 16, 25]

# Cost of thread

The cost of using multithreading includes:

Context switching overhead:
Switching between threads can be expensive, especially with frequent switches, as it involves saving and loading thread states.

Synchronization overhead:
Managing access to shared resources (e.g., with locks or mutexes) can introduce delays and potential bottlenecks.

Increased memory usage:
Each thread has its own stack, leading to higher memory consumption, which can be problematic with many threads.

Thread creation and management cost:
Creating and managing threads is relatively slow compared to simple function calls, especially if threads are short-lived.

Debugging complexity:
Multithreaded programs are harder to debug due to issues like race conditions and deadlocks.

False sharing and cache contention: Threads on different cores might interfere with each other’s cache, causing performance degradation.

Recall:
Functions push arguments (a0-a3), return
address, local variables, and temporary use registers onto the
stack.
============================

Q7 Lock
Summary of Locking Mechanisms:
Lock: Basic mutual exclusion; one thread can access a resource at a time.
RLock (Reentrant Lock): Same thread can acquire the lock multiple times.
- RLock (Reentrant Lock)
An RLock is a type of lock that can be acquired multiple times by the same thread without causing a deadlock.

Semaphore: Allows a limited number of threads to access the critical section at once.
- A Semaphore controls access to a shared resource through the use of a counter. It allows a certain number of threads to access the critical section simultaneously.
It is useful for managing access to a fixed number of resources, like a database connection pool.

Event: Allows threads to wait for a signal before continuing.
- Event
An Event is a simple synchronization primitive that allows one or more threads to wait for an event to be set.
It is typically used when threads need to wait for a signal from another thread to proceed.

Condition: Synchronizes threads based on a condition becoming true.
Barrier: Ensures that multiple threads all reach a specific point in the code before proceeding.



what is preemptive multithreading:
Preemptive threading requires the OS to manage thread switching, context switching, and scheduling.
Cooperative threading still involves the OS, but threads themselves control when they switch.


Question
Python decorator

in simple terms, a decorator is a function that takes another function as input and returns a new function
with modified behavior—without changing the original function’s code.

Think of it like a wrapper that adds extra functionality before or after the original function runs.


Yes! 🎯 Python treats functions as first-class objects, meaning functions can be:
✅ Assigned to variables
✅ Passed as arguments
✅ Returned from other functions

This is what makes decorators possible!

Q8 Fork vs Thread
Threads share memory and resources, making their creation lightweight and fast.
Forked processes require independent memory space, resource duplication, and additional system calls, making their creation slower.

FORK
Forking is nothing but creating a new process. We create a new process that copies all the elements of old process.

THREAD
Threading is a light weight process which shares all the section of the process except for the stack. A process can have multiple threads.

Elements of a process
Each process is made up of few sections.

text: This is where the code of the process reside. This is a read-only section.

data: This is where global and static initialized variables are stored.

rodata: This is where constant variables are stored.

bss: This is where global and static un-initialized variables are stored.

stack: This is where the local variables and function calls are stored.

heap: This is where user allocated memory is stored. When the user uses malloc, calloc, new etc.


Q10. Asyncio
For Threading: The most common ways are using threading.Thread or concurrent.futures.ThreadPoolExecutor.
For CPU-bound tasks that require true parallelism, consider using multiprocessing for process-based parallelism.
For I/O-bound tasks and asynchronous programming, asyncio is a highly effective option.

asyncio is a Python module that provides support for asynchronous programming using an event loop.
It allows you to write concurrent code using coroutines, which are special functions defined with async def.
The event loop runs coroutines and handles tasks like I/O operations without blocking the program.
This is especially useful for I/O-bound tasks, such as network requests or file operations,
where the program can continue executing other tasks while waiting for I/O to complete.

The main benefits of asyncio are its efficiency and the ability to handle many tasks concurrently with a single thread,
avoiding the overhead of threading or multiprocessing.


Question
Multi-threading involves running multiple threads within a single process.
Multi-processing involves running multiple independent processes, each with its own memory space.

Q11 GIL
The reason Python can be slow with multithreading is primarily due to the Global Interpreter Lock (GIL).

What is the GIL?
The GIL is a mutex (a mutual exclusion lock) that allows only one thread to execute Python bytecode at a time, even on multi-core systems.
While Python threads can be created and managed, the GIL prevents true parallel execution of Python bytecode across multiple threads.


Q12 how to achieve immutability
# Immutable types: Use built-in types like tuples, frozensets, and strings.
# @property decorator: Make class attributes read-only.
# namedtuple: Simple, immutable, named objects.
- namedtuple from the collections module allows you to create simple immutable objects. It's similar to defining a lightweight class but provides immutability for its attributes.

# Custom class with __setattr__: Create a fully custom immutable class.
class Immutable:
    def __init__(self, value):
        object.__setattr__(self, "value", value)

    def __setattr__(self, name, value):
        raise AttributeError("Cannot modify immutable object")

    def __repr__(self):
        return f"Immutable(value={self.value})"

# Usage
obj = Immutable(100)
print(obj.value)  # Output: 100
# obj.value = 200  # This will raise an AttributeError


# dataclasses with frozen=True: Easily create immutable data classes.
# final: Indicate that a class or method should not be subclassed or overridden.

Question
Python pass by reference ?

Python’s argument-passing model is neither “Pass by Value” nor “Pass by Reference” but it is “Pass by Object Reference”.

Depending on the type of object you pass in the function, the function behaves differently.
Immutable objects show “pass by value” whereas mutable objects show “pass by reference”.

In both Java and Python:

Modifying the object inside the method will affect the original object because both the method and the caller are working with the same object.
Reassigning the reference inside the method to a new object will not affect the caller’s reference.
The caller’s reference will still point to the original object, just as in Java, where changing the reference inside the method does not change the caller's reference to the object.


Question
In Python, iterators, iterables, and generators are all related but distinct concepts. Let’s break down each one clearly.

1. Iterable
Definition: An iterable is any object in Python that can return an iterator. In other words, an iterable is an object that you can loop over (like a list, tuple, string, etc.).
How to recognize: If an object has an __iter__() method (or __getitem__() for sequences), it is an iterable.
Example: Lists, tuples, dictionaries, and strings are all iterable objects.

2. Iterator
Definition: An iterator is an object that represents a stream of data. An iterator can only be traversed in one direction and must implement two methods:
__iter__() (returns the iterator object itself)
__next__() (returns the next item in the sequence or raises StopIteration when the sequence ends)
How to recognize: All iterators are iterables, but not all iterables are iterators.

An iterator must return itself in __iter__() and implement __next__().
An iterable must define __iter__() but doesn't need __next__().
Yes! When you call iter(list), it returns a built-in list iterator that implements __next__() by default.

3. Generator
Definition: A generator is a special type of iterator that is defined using a function (with the yield keyword) instead of returning a complete list. It generates values one at a time as you iterate over them.

How to recognize: Generators are iterators, but they are defined using the yield keyword.

Benefits: Generators are lazy, meaning they don’t store all values in memory at once and only generate values when needed. This is efficient for large datasets.

A generator expression is a concise way to create a generator in Python, similar to list comprehensions, but instead of creating an entire list in memory, it yields items one at a time, making it more memory efficient.

Syntax of Generator Expression:
(expression for item in iterable if condition)


Coding q
1. Data Structures & Algorithms
Arrays & Strings
Reverse a string without using .reverse() or slicing.
Check if two strings are anagrams.
Find the first non-repeating character in a string.
Find the longest substring without repeating characters.
Rotate an array k times to the right.
Merge two sorted arrays without extra space.
Find the maximum product of two integers in an array.
Find the majority element (appears more than n/2 times).
Find the kth smallest/largest element in an unsorted array.
Find a subarray with the maximum sum (Kadane's Algorithm).
Find the missing number in an array of size n with numbers 1 to n.
Find the intersection of two arrays.
Find pairs in an array that sum to a given value.
Find the median of two sorted arrays.
Find the longest palindrome substring.
Linked Lists
Reverse a linked list (iterative & recursive).Ï
Detect a cycle in a linked list.
Find the intersection point of two linked lists.
Remove the nth node from the end of a linked list.
Find the middle of a linked list.
Merge two sorted linked lists.
Add two numbers represented by linked lists.
Flatten a linked list.
Stacks & Queues
Implement a stack with push(), pop(), and getMin().
Implement a queue using two stacks.
Evaluate a postfix expression.
Check if a given expression has balanced parentheses.
Find the largest rectangle in a histogram.
Implement a circular queue.
Trees & Graphs
Find the height of a binary tree.
Check if a binary tree is balanced.
Check if a binary tree is a valid BST.
Find the lowest common ancestor (LCA) of two nodes in a BST.
Find the level order traversal of a binary tree.
Find the zigzag level order traversal of a binary tree.
Implement DFS (depth-first search) for a graph.
Implement BFS (breadth-first search) for a graph.
Find the shortest path in an unweighted graph using BFS.
Detect a cycle in a directed graph.
Find the number of connected components in a graph.
Sorting & Searching
Implement merge sort and quicksort.
Find the kth largest element in an array.
Find a peak element in an array.
Binary search in a rotated sorted array.
Search for an element in a nearly sorted array.
Dynamic Programming
Find the nth Fibonacci number (memoization & bottom-up approach).
Find the longest common subsequence of two strings.
Find the maximum sum subarray (Kadane’s Algorithm).
Find the minimum number of coins needed to make a given amount.
Find the number of ways to climb a staircase (1 or 2 steps at a time).
2. System Design & OOP
Object-Oriented Programming (OOP)
Design a parking lot system with different vehicle types.
Design a library management system (books, users, borrow/return).
Design a URL shortening service (like TinyURL).
Implement a Least Recently Used (LRU) Cache using a dictionary & linked list.
Design a social media news feed.
Design an elevator control system.
Design a hotel booking system.
Design an ATM machine system.
Concurrency & Multithreading
Implement a producer-consumer problem using threading.
Write a thread-safe Singleton class.
Implement a rate limiter using a token bucket algorithm.
Design a thread pool executor.
Implement a concurrent read/write system using locks.
Use condition variables to synchronize multiple threads.
3. Python-Specific Questions
Python Built-ins & Collections
What is the difference between deepcopy and copy?
Implement a function that groups anagrams together using defaultdict.
What is the difference between Counter.most_common() and sorted(Counter.items())?
Implement a custom dictionary that tracks insertion order.
Generators & Iterators
Implement a generator that yields Fibonacci numbers indefinitely.
Convert a normal function into a generator using yield.
Explain yield from with an example.
Write a function that returns an infinite stream of prime numbers.
Decorators & Metaclasses
Write a decorator that caches function results (memoization).
Implement a decorator that times function execution.
What is a metaclass, and when would you use one?
Implement a metaclass that restricts the number of instances of a class.
File Handling & Serialization
Write a function to read a large file line by line without loading it into memory.
Serialize and deserialize a Python object using pickle.
Implement a log file rotation system.
Python Memory & Performance
Explain how Python manages memory.
What is a memory leak, and how can you prevent it in Python?
Optimize a function using functools.lru_cache.
Explain the difference between is and ==.
4. Databases & SQL
Write an SQL query to find the second-highest salary from an employee table.
Find the duplicate emails in a table.
Explain the difference between INNER JOIN, LEFT JOIN, and RIGHT JOIN.
Design a database schema for an e-commerce website.
5. Web Scraping & APIs
Write a web scraper to fetch article titles from a news website.
Use requests to call an API and process the JSON response.
Rate limit API requests to avoid getting blocked.
6. Data Science & Pandas
Load a CSV file into a Pandas DataFrame and filter rows.
Group data by a column and compute aggregate statistics.
Handle missing data in a Pandas DataFrame.
Merge two DataFrames on a common column.
Pivot and reshape data in Pandas.

