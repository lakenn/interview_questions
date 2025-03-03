# create a list of chunk

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
    ] * 80
    start_time = time.perf_counter()
    download_all_sites(sites)
    duration = time.perf_counter() - start_time
    print(f"Downloaded {len(sites)} sites in {duration} seconds")

def download_all_sites(sites):
    with ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_site, sites)

def download_site(url):
    session = get_session_for_thread()
    with session.get(url) as response:
        print(f"Read {len(response.content)} bytes from {url}")

def get_session_for_thread():
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session

if __name__ == "__main__":
    main()


import asyncio
import time

import aiohttp

async def main():
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80
    start_time = time.perf_counter()
    await download_all_sites(sites)
    duration = time.perf_counter() - start_time
    print(f"Downloaded {len(sites)} sites in {duration} seconds")

async def download_all_sites(sites):
    async with aiohttp.ClientSession() as session:
        tasks = [download_site(url, session) for url in sites]
        await asyncio.gather(*tasks, return_exceptions=True)

async def download_site(url, session):
    async with session.get(url) as response:
        print(f"Read {len(await response.read())} bytes from {url}")

if __name__ == "__main__":
    asyncio.run(main())