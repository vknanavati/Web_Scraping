import requests
import pandas as pd
from bs4 import BeautifulSoup
from random import randint
from time import sleep

URL = [
    "https://www.hostelworld.com/st/hostels/north-america/mexico/mexico-city/",
    "https://www.hostelworld.com/st/hostels/north-america/mexico/mexico-city/p/2/",
]

links_list = []
for url in range(0, 2):
    page = requests.get(URL[url], timeout=10)
    soup = BeautifulSoup(page.content, "html.parser")
    soup.prettify()

    # for link in soup.find_all("a"):
    #     print(link.get("href"))
    #     print()

    link_elements = soup.find_all("div", class_="gallery")

    for link in link_elements:
        results = link.find_all("a")
        for result in results:
            link_url = result["href"]
            links_list.append(link_url)
# print(links_list)
# print(links_list)

name_list = []
hostel_scores = []
composite_hostel_scores = []

for url in range(0, 49):
    page = requests.get(links_list[url], timeout=10)

    soup = BeautifulSoup(page.content, "html.parser")
    soup.prettify()

    hostel_name = soup.find("h1")
    hostel_name = hostel_name.text.strip()
    name_list.append(hostel_name)
    # print(f"\nHostel Name List: {name_list}\n")

    breakdown_scores = soup.find_all("div", class_="rating-score")

    for breakdown_score in breakdown_scores:
        breakdown_score = breakdown_score.text.strip()
        hostel_scores.append(breakdown_score)
    # print(f"\nList of scores: {hostel_scores}")

    composite_hostel_scores.append(hostel_scores)

    # print(f"\nComposite scores: {composite_hostel_scores}")

    lists_to_join = zip(name_list, composite_hostel_scores)
    # print(f"\nLists to join: {lists_to_join}\n")
    specific_ratings = list(lists_to_join)
    # print(f"\nSpecific ratings: {specific_ratings}\n")
    ratings_dict = dict(specific_ratings)

    # print(f"\nComplete Dictionary: {ratings_dict}\n")
    seconds = randint(2, 10)
    sleep(seconds)
    print(f"\nI waited {seconds} seconds\n")
    # sleep(randint(2, 10))

df = pd.DataFrame(ratings_dict)
# print(df)
df.to_csv("Mexico_City_Hostels.csv")
print("\nCSV created! YAY!!\n")

######NEXT STEPS#######
# 1. automize populating URL addresses from each page that lists the hostels of that city
# 2. Based on the total number of hostels for each city the range of the URL list should change
# 3. PANDAS: Make bar graphs !!!! :)
