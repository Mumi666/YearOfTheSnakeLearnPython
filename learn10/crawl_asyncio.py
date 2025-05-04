import asyncio

async def crawl_page(url):
    print('crawling {}'.format(url))
    sleep_time = int(url.split('_')[-1])
    await asyncio.sleep(sleep_time)
    print('done crawling {}'.format(url))

async def main(urls):
    start_time = asyncio.get_event_loop().time()
    for url in urls:
        await crawl_page(url)
    end_time = asyncio.get_event_loop().time()
    print('Total time: {:.2f} seconds'.format(end_time - start_time))


asyncio.run(main(['url_1', 'url_2', 'url_3', 'url_4', 'url_5']))