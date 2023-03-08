import requests
from bs4 import BeautifulSoup

URL = "https://www.cia.gov/the-world-factbook/countries/switzerland/travel-facts"
page = requests.get(URL, timeout=10)

soup = BeautifulSoup(page.content, "html.parser")
soup.prettify()

headings = []
data = []
for topic in soup.find_all("h3"):
    headings.append(topic.text)

    info = topic.find_next_sibling("p")
    data.append(info.text)

lists_to_join = zip(headings, data)
joint_list = list(lists_to_join)


country_dict = dict(joint_list)

country_dict = {
    "US State Dept Travel Advisory": "The US Department of State currently recommends US citizens exercise normal precautions in Switzerland. Consult its website via the link below for updates to travel advisories and statements on safety, security, local laws, and special circumstances in this country.https://travel.state.gov/content/travel/en/traveladvisories/traveladvisories.html",
    "Passport/Visa Requirements": "US citizens should make sure their passport will not expire for at least 6 months after they enter the country even if they do not intend to stay that long. They should also make sure they have at least 2 blank pages in their passport for any entry stamp that will be required. A visa is not required as long as you do not stay in the country more than 89 days.",
    "US Embassy/Consulate": "[41] (031) 357-70-11; US Embassy Bern, Sulgeneckstrasse 19, CH-3007 Bern, Switzerland; https://ch.usembassy.gov/",
    "Telephone Code": "41",
    "Local Emergency Phone": "Ambulance: 144; Fire: 118; Police: 117",
    "Vaccinations": "See WHO recommendationshttp://www.who.int/",
    "Climate": "Temperate, but varies with altitude; cold, cloudy, rainy/snowy winters; cool to warm, cloudy, humid summers with occasional showers",
    "Currency (Code)": "Swiss francs (CHF)",
    "Electricity/Voltage/Plug Type(s)": "230 V / 50 Hz / plug types(s): C, J",
    "Major Languages": "German (or Swiss German), French, Italian, English, Portuguese, Albanian, Serbo-Croatian, Spanish",
    "Major Religions": "Roman Catholic 34.4%, Protestant 22.5%, other Christian 5.7%, Muslim 5.5%",
    "Time Difference": "UTC+1 (6 hours ahead of Washington, DC, during Standard Time); daylight saving time: +1hr, begins last Sunday in March, ends last Sunday in October",
    "Potable Water": "Yes",
    "International Driving Permit": "Suggested",
    "Road Driving Side": "Right",
    "Tourist Destinations": "Matterhorn; Jungfraujoch; Interlaken; Lucerne; Lake Geneva; Chateau de Chillon; Zurich; Lake Lugano; Bern",
    "Major Sports": "Soccer, ice hockey, tennis, skiing, schwingen (wrestling)",
    "Cultural Practices": "Speaking too loudly in public, especially on cell phones, is frowned upon.",
    "Tipping Guidelines": "A service charge is typically added at restaurants so no tipping is needed, but you can round up the bill for the wait staff. Round up a taxi fare or add 5%. Tipping is usually expected for hotel staff. A bellhop should receive 1-2 francs for each bag carried.",
    "Souvenirs": "Chocolate; cuckoo clocks, music boxes, and other wood carved items; cheese; Swiss army knives; watches/clocks; paper cut pictures; embroidered fabric; schnapps spirits\t",
    "Traditional Cuisine": "Rösti — grated potato patties sometimes including herbs and spices, onions, ham, or cheese and pan-fried in butter or oil; the dish is cut into wedges for serving",
}

keys = {
    "US State Dept Travel Advisory",
    "Climate",
    "Currency",
    "Major Languages",
    "Road Driving Side",
    "Tourist Destinations",
    "Cultural Practices",
    "Tipping Guidlines",
    "Traditional Cuisine",
}
new_dict = {key: value for key, value in country_dict.items() if key in keys}
print(new_dict)