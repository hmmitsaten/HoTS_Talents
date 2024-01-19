from bs4 import BeautifulSoup
import requests

#heroname = input("Enter hero name:")

def fetch_talent_html():
    # make a request to the target website
    r = requests.get("https://www.icy-veins.com/heroes/hogger-talents")
    if r.status_code == 200:
        # if the request is successful return the HTML content
        return r.text
    else:
        # throw an exception if an error occurred
        raise Exception("an error occurred while fetching icyveins html")
    
def extract_talents_info(html):
    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(html, 'html.parser')

   # talentdiv = soup.find(class_='heroes_builds')
   # print(talentdiv.prettify())
    heroes_builds_collection = soup.find(class_='heroes_builds')
    heroes_builds = heroes_builds_collection.find_all("heroes_build")
    #print(heroes_builds)
    # iterate through our builds
    builds = []
    for builds in heroes_builds:  
        talent_collection = builds.find("div", {"class": "heroes_build_talents"})
        talents = talent_collection.find_all("heroes_build_talent_tier")[1:]
        talent = []
        for talent in talents:
            img_tag = talent.find('img')
            talent.append({
            "Level": talent.class_,
            "Ability": img_tag.get('alt'),
           # "name": talent.find("h3", {"class": "toc_no_parsing"})["data-sort"],
        })
        # extract the information needed using our observations
        builds.append({
            "Talent Build Name": builds.h3,
           # "name": talent.find("h3", {"class": "toc_no_parsing"})["data-sort"],
            "Category": builds.span.text.strip(),
            "Category2": builds.span.text.strip(),
            "Talents": talent
           # "change_24h": talent.find("td", {"class": "td-change24h"}).text.strip(),
        })
    return builds


# fetch talent's HTML content
html = fetch_talent_html()

# extract our data from the HTML document
builds = extract_talents_info(html)

# display the scraper results
for build in builds:
    print(build, "\n")

print(builds)
