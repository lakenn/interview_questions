# create a list of chunk
import concurrent.futures


def chunk(lst, chunk_size):
    for i in range(0, len(lst), chunk_size):
        yield lst[i:i+chunk_size]


print(list(chunk(list(range(10)), 3)))

# context switch
"""
Context switching overhead:
Switching between threads can be expensive, especially with frequent switches, as it involves saving and loading thread states.

Recall:
Functions
push arguments(a0 - a3),
return address, local variables onto the stack.
"""

# asynchronous tasks use cooperative multitasking

import threading
import time
from concurrent.futures import ThreadPoolExecutor

import requests

thread_local = threading.local()

def main():
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 10
    start_time = time.perf_counter()
    download_all_sites(sites)
    duration = time.perf_counter() - start_time
    print(f"Downloaded {len(sites)} sites in {duration} seconds")


def task(site):
    print(site)
    return site

def download_all_sites(sites):
    with ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_site, sites)

    with ThreadPoolExecutor(max_workers=5) as executor:
        results = executor.map(task, sites)

    print(list(results))

    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(task, site) for site in sites]

    for future in concurrent.futures.as_completed(futures):
        print(future.result())

    print('--------')

def download_site(url):
    session = get_session_for_thread()
    with session.get(url) as response:
        # print(f"Read {len(response.content)} bytes from {url}")
        ...

def get_session_for_thread():
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session

if __name__ == "__main__":
    main()


import asyncio

async def atask(site):
    print(site)

sites = [
    "https://www.jython.org",
    "http://olympus.realpython.org/dice",
] * 20

def chunk_gen(lst, chunk_size):
    for i in range(0, len(lst), chunk_size):
        yield lst[i:i+chunk_size]
async def main():

    tasks = [asyncio.create_task(atask(site)) for site in chunk_gen(sites, 5)]
    asyncio.gather(*tasks)
    print('aaaaaaaaaaa')
    task_done = asyncio.Future()
    await task_done

asyncio.run(main())