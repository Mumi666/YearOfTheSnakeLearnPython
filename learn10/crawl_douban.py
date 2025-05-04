import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import time

def main():
    url = "https://movie.douban.com/cinema/later/beijing/"
    headers = {'user-agent': UserAgent().random}
    init_page = requests.get(url, headers=headers).content

    init_soup = BeautifulSoup(init_page, "lxml")


    all_movie = init_soup.find("div", id="showing-soon")

    for movie in all_movie.find_all('div', class_="item"):
        all_a_tag = movie.find_all("a")
        all_li_tag = movie.find_all("li")

        movie_name = all_a_tag[1].text
        image_url = all_a_tag[0].find("img")["src"]
        movie_time = all_li_tag[0].text

        print('{} {} {}'.format(movie_name, movie_time, image_url))


start = time.time()
main()
end = time.time()

print("Total execution time: {:.2f} seconds".format(end - start))