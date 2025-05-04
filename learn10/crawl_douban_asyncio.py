import asyncio
import aiohttp
import time

from bs4 import BeautifulSoup
from fake_useragent import UserAgent

async def fetch_content(url):
    headers = {'user-agent': UserAgent().random}
    async with aiohttp.ClientSession(
        headers=headers,
        connector=aiohttp.TCPConnector(ssl=False)
    ) as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
    url = "https://movie.douban.com/cinema/later/beijing/"
    init_page = await fetch_content(url)
    init_soup = BeautifulSoup(init_page, "lxml")

    movie_names, image_urls, movie_times = [], [], []

    all_movies = init_soup.find("div", id="showing-soon")
    if not all_movies:
        return
    for movie in all_movies.find_all('div', class_="item"):
        all_a_tag = movie.find_all("a")
        all_li_tag = movie.find_all('li')

        movie_names.append(all_a_tag[1].text)
        image_urls.append(all_a_tag[0].find("img")["src"])
        movie_times.append(all_li_tag[0].text)

    tasks = [fetch_content(url) for url in image_urls]
    image_contents = await asyncio.gather(*tasks)

    for movie_name, image_content, movie_time in zip(movie_names, image_contents, movie_times):
        print('{} {} {}'.format(movie_name, movie_time, image_content))

start = time.time()
asyncio.run(main())
end = time.time()

print("Total execution time: {:.2f} seconds".format(end - start))