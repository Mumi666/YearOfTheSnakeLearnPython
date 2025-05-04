import time

def crawl_page(url):
    print("Crawling page at {}".format(url))
    sleep_time = int(url.split("_")[-1])
    time.sleep(sleep_time)
    print("Done crawling page at {}".format(url))

def main(urls):
    for url in urls:
        crawl_page(url)


start_time = time.time()
main(['url_1', 'url_2', 'url_3', 'url_4', 'url_5'])
end_time = time.time()
print(f"Total execution time: {end_time - start_time:.2f} seconds")
