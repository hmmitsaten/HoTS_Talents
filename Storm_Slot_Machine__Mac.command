#!/usr/bin/python3
"""This file contains the entire program for getting talents for HoTS."""
from bs4 import BeautifulSoup
import requests
import re
import json
"""
Program flow
Start
Create flag to check if it's time to end the party
Ask user for hero name
Check status code of the request
If bad, tell the user and try again
If good, continue with program
Display results
If user request to go again is true, go again
If not, exit
"""


def main():
    """Process the file."""
    # Get html from website using request raven
    def fetch_talent_html():
        """Return the html for a given request.
		Returns:
            String containing the html of the website
        """

        # instantiate flag to get the party started
        flag = 1

        while flag == 1:

            # request the hero name from user
            heroname = input("Enter hero name:")

            # make a request to the target website
            r = requests.get(
                "https://www.icy-veins.com/heroes/"
                + (heroname.lower().strip()).replace(" ", "-")
                + "-talents"
            )

            # update the flag after making the request
            if r.status_code != 200:
                # request failed - tell user and repeat request
                flag = 1
                print("Request failed. Check your spelling, dude.\n")
            else:
                # request success - continue with the party
                flag = 0

            # if the request is successful return the HTML content
        return r.text
    ######################################################################
    def extract_talents_info(html):
        """Get an array containing the talents from the html.

        Args:
            HTML content(html): Dataset from the IcyVeins website.

        Returns:
            Array containing the talents.
        """
        soup = BeautifulSoup(html, "html.parser")
        builds = []

        for b in soup.select(".heroes_build"):
            # Define the pattern to match " Icon" at the end of the string
            remove = r" Icon$"
            removen = r"\n$"
            builds.append(
                {
                    "Build Name": re.sub(removen, "", b.h3.get_text()),
                    "Use": b.span.text.strip(),
                    "Talents": [
                        {
                            "Level": t.span.get_text(),
                            "Ability": re.sub(remove, "", t.img.get("alt")),
                        }
                        for t in b.select(".heroes_build_talent_tier")
                    ],
                }
            )

        return builds
    ######################################################################
    # fetch HTML content from the website
    html = fetch_talent_html()

    # parse the html for the talent data
    builds = extract_talents_info(html)

    # display the scraper results
    for build in builds:
        pretty_output = json.dumps(build, indent=2)
        print(pretty_output)


# check if user wants to repeat the program
while True:
    main()
    if input("Repeat the program? (Y/N)").strip().upper() != "Y":
        break
