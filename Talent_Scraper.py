from bs4 import BeautifulSoup
import requests
import re
import json

def main():

    heroname = input("Enter hero name:")

    def fetch_talent_html():
        # make a request to the target website
        r = requests.get("https://www.icy-veins.com/heroes/" + heroname.lower() + "-talents")
        if r.status_code == 200:
            # if the request is successful return the HTML content
            return r.text
        else:
            # throw an exception if an error occurred
            raise Exception("an error occurred while fetching icyveins html")

    def extract_talents_info(html):
        soup = BeautifulSoup(html, 'html.parser')
        builds = []
        for b in soup.select('.heroes_build'):
                # Define the pattern to match " Icon" at the end of the string
                remove = r' Icon$'  
                removen = r'\n$'
                builds.append({
                'Build Name': re.sub(removen, '', b.h3.get_text()),
                'Use': b.span.text.strip(),
                'Talents': [
                    {
                        'Level':t.span.get_text(),
                        'Ability': re.sub(remove, '', t.img.get('alt'))
                    } 
                    for t in b.select('.heroes_build_talent_tier')
                ] 
            })

        return builds

    # fetch talent's HTML content
    html = fetch_talent_html()

    # extract our data from the HTML document
    builds = extract_talents_info(html)

    # display the scraper results
    for build in builds:
        pretty_output = json.dumps(build, indent=2)
        print(pretty_output)

while True:
    main()
    if input("Repeat the program? (Y/N)").strip().upper() != 'Y':
        break