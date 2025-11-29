import requests
from bs4 import BeautifulSoup
import pandas as pd


def scrape_suumo(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")

    titles = []
    locations = []
    prices = []
    floorplans = []

    cards = soup.find_all("div", class_="cassetteitem")

    for card in cards:
        title = card.find("div", class_="cassetteitem_content-title").get_text(strip=True)
        address = card.find("li", class_="cassetteitem_detail-col1").get_text(strip=True)
        price = card.find("span", class_="cassetteitem_other-emphasis").get_text(strip=True)
        madori = card.find("span", class_="cassetteitem_madori").get_text(strip=True)

        titles.append(title)
        locations.append(address)
        prices.append(price)
        floorplans.append(madori)

    df = pd.DataFrame({
        "物件名": titles,
        "住所": locations,
        "家賃": prices,
        "間取り": floorplans
    })

    return df


if __name__ == "__main__":
    url = "https://suumo.jp/chintai/tokyo/sc_shinjuku/"
    df = scrape_suumo(url)
    df.to_csv("sample_output.csv", index=False, encoding="utf-8-sig")
    print(df.head())
