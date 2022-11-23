from requests_html import HTMLSession
from bs4 import BeautifulSoup
import pandas as pd

r = HTMLSession()
data = []
url = "https://www.booking.com/searchresults.html?aid=304142&label=gen173nr-1FCAEoggI46AdIM1gEaHaIAQGYATG4ARfIAQzYAQHoAQH4AQKIAgGoAgO4AsGR9JsGwAIB0gIkZWMxYzYxNjUtYjBlNy00MDllLWFhNzgtMWNmYjlhOGUwNDE32AIF4AIB&checkin=2022-11-25&checkout=2022-11-26&dest_id=-2258072&dest_type=city&group_adults=null&req_adults=null&no_rooms=null&group_children=null&req_children=null"


def getpage(url):
    page = r.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    return soup


def getcontent(soup):
    items = soup.find_all("div", {"data-testid": "property-card"})
    for item in items:
        name = item.find("div", {"data-testid": "title"}).text
        price = item.find("span", {"class": "fcab3ed991 bd73d13072"}).text
        link = item.find("a")["href"]
        size = item.find("span", class_="df597226dd").text
        spec = item.find("div", class_="cb5b4b68a4").text
        place = item.find("span", class_="f4bd0794db b4273d69aa").text
        distance = item.find("span", {"data-testid": "distance"}).text
        info = {
            "place name": name,
            "price": price,
            "Rooms": size,
            "interior": spec,
            "location": place,
            "distance from location": distance,
            "place link": link,
        }
        data.append(info)
    return


soup = getpage(url)
getcontent(soup)

fr = pd.DataFrame(data)
fr.to_csv("booking.csv",index=False)
