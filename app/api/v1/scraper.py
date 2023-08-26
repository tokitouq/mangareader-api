import requests
from bs4 import BeautifulSoup, element

# Scrape popular mangas
class PopularManagasScraper:
    def __init__(self):
        self.URL = "https://mangareader.to/home"

    def _scrape_ranking(self, element):
        ranking_container = element.find("div", {"class", "number"})
        rank = ranking_container.find("span")
        if rank:
            return rank.text.strip()
        return "Ranking not found"

    def _scrape_title(self, element):
        title_element = element.find("div", {"class": "anime-name"})
        if title_element:
            return title_element.text.strip()
        return "No title found"

    def _scrape_image(self, element):
        cover = element.find("img", {"class", "manga-poster-img"})
        if cover:
            return cover["src"]
        return "Cover image not found"

    def scrape(self):
        data = []

        response = requests.get(self.URL)
        soup = BeautifulSoup(response.content, "html5lib")
        container = soup.find("div", {"id": "manga-trending"})

        if container:
            element_list = container.find_all("div", {"class": "swiper-slide"})

            for element in element_list:
                manga_data = {
                    "rank": self._scrape_ranking(element),
                    "title": self._scrape_title(element),
                    "cover": self._scrape_image(element)
                }

                data.append(manga_data)
        return data