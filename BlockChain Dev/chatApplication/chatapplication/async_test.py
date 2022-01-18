import asyncio
import time

async def greet(name, delay):
    await asyncio.sleep(delay)
    print(f'{name}: I waited {delay} seconds before saying')

async def main():
    task1 = asyncio.create_task(greet('bubu', 11))
    task2 = asyncio.create_task(greet('bitu', 6))
    task3 = asyncio.create_task(greet('mama', 3))

    start_time = time.time()

    print('0.00s program exicution starts')

    await task1
    await task2
    await task3

    print(f'{time.time() - start_time:.2f}s program exicution ends')

asyncio.run(main())