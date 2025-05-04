import asyncio
import time


async def crawl_page(url):
    print('crawling {}'.format(url))
    sleep_time = int(url.split('_')[-1])
    await asyncio.sleep(sleep_time)
    print('done crawling {}'.format(url))

async def main(urls):
    tasks = [ asyncio.create_task(crawl_page(url)) for url in urls]
    # for task in tasks:
    #     await task
    # 等价于上一种写法
    await asyncio.gather(*tasks)


start = time.time()
asyncio.run(main(['url_1', 'url_2', 'url_3', 'url_4', 'url_5']))
end = time.time()
print('Total time: {:.2f} seconds'.format(end - start))
