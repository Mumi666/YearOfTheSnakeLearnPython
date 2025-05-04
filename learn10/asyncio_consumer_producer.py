import asyncio
import random
import time


async def consumer(queue, id):
    while True:
        item = await queue.get()
        print(f'consumer {id} got {item}')
        await asyncio.sleep(1)

async def producer(queue, id):
    for i in range(5):
        item = random.randint(1, 10)
        await queue.put(item)
        print(f'producer {id} put {item}')
        await asyncio.sleep(1)

async def main():
    queue = asyncio.Queue()
    consumer_task1 = asyncio.create_task(consumer(queue, 'consumer_1'))
    consumer_task2 = asyncio.create_task(consumer(queue, 'consumer_2'))

    producer_task = asyncio.create_task(producer(queue, 'producer_1'))
    producer_task2 = asyncio.create_task(producer(queue, 'producer_2'))

    await asyncio.sleep(10)

    consumer_task1.cancel()
    consumer_task2.cancel()

    await asyncio.gather(consumer_task1, consumer_task2, producer_task, producer_task2, return_exceptions=True)

start = time.time()
asyncio.run(main())
end = time.time()
print('Total time: {:.2f} seconds'.format(end - start))
