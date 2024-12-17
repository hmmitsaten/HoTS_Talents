# Storm Slot Machine

Storm Slot Machine is a program which will assist Heroes of the Storm users.
A difficulty with filthy casual players is in the selection of talents, akin to the ten kinds of nut butter offered in a grocery store.
Upon launch, the user is introduced to a DOS window. 
The program will ask the user to enter a hero name. For example, it will say "Enter hero name: " upon launch.
When entered, a list of recommended hero talents are printed in plain text with only the necessary information shown. 
This program helps focus to go more towards gameplay and reaction times, and less on the selection of talents.

## Getting Started

Install Prerequisites by following the steps below, then run the .py file with Python.
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

1. Install Python by following the steps below:
  A. Navigate to website https://www.python.org/downloads/
  B. Click the Download "Python XX.XX.X" button
  C. Follow the prompts of the installer
  D. On Windows, install the system variable 
2. Open command
3. pip install bs4
4. pip install requests
5. Navigate to the folder containing the .py file
6. Run the python file for testing
  A. Open a command prompt at said folder
  B. Type the name of the python file, including extension, and hit enter to run it. It should request the hero name.
```
For example, the following will appear: "Enter hero name:"
```
7. Create an exe file
  A. Open a command prompt at the .py file location
  B. Run the following command: pyinstaller --onefile <py file name>
  C. In the same folder, open the dist folder to find the exe (optional: the spec file is a list of the modules needed to build the whole thing)

### Prerequisites

Python - Follow python website.
Pip - Should come with Python. If not, follow Pip website instructions.
bs4 - Follow bs4 website in Built With section or install with pip using "pip install bs4"
requests - Follow requests website in Built With section or install with pip using "pip install bs4"

### Installing

Find the appropriate exe file for your operating system.
Optional: For development, follow the "Getting Started" section.

## Running the tests

Run tests manually by launching the exe or launching the .py file with Python, or for automated testing install AutoIT

Optional: Use this for automated testing:
https://www.autoitscript.com/site/autoit/

### Break down into end to end tests

Test case #
Expected Result

10A - Launch exe on test machine
      Command window should open with a prompt to enter hero name.
```
Enter hero name:
```

10B - Enter a hero name
      Talents should be displayed.
```
Enter hero name:Jaina
{
  "Build Name": "Standard Build",
  "Use": "Recommended",
  "Talents": [
    {
      "Level": "Level 1",
      "Ability": "Fingers of Frost"
    },
```

11A - Enter the wrong spelling
      An error should come up and user should have another prompt to enter the hero name.
```
Enter hero name:vala
Request failed. Check your spelling, dude.

Enter hero name:
```

12A - Enter y to continue using the program
      Another prompt should be printed to enter the hero name.
```
      "Level": "Level 20",
      "Ability": "Wintermute"
    }
  ]
}
Repeat the program? (Y/N)y
Enter hero name:
```

### And coding style tests

1. Ensure there are no extra whitespaces at the end of each line
2. Check for extra blank lines after each function and class
3. Docstrings after each function should give a description of said function, with args and returns explained.
```
def get_stock_level(book):
    """Return the stock level for the given book.

    This calculates the stock level across multiple stores in the city,
    excluding books reserved for customers.

    Args:
        book (str): Name of the book.

    Returns:
        String of publication date in the format of 'DD/MM/YYYY'.
    """
```

## Deployment

1. Check your operating system.
2. Download and place the exe that corresponds with your operating system.

## Built With

* [Python](https://www.python.org/downloads/) - Programming language used
* [PyInstaller](https://pyinstaller.org/) - The web framework used
* [bs4](https://pypi.org/project/beautifulsoup4/) - Dependency Management
* [requests](https://docs.python-requests.org/) - Assists in requesting http

## Contributing

Your beautiful faces. The bastards of HoTS.
Please create a fork if you would like to contribute, then we can discuss farther.

## Versioning

We use [SemVer](http://semver.org/) for versioning.
Change log is included.

## Authors

* **Alan Mispagel** - *Creator and initial prototype - [Hmmitsaten](https://github.com/hmmitsaten)
* **Hedgehog** - *Dataset retrieval assistance
* **PurpleBooth** - *Readme template

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

*The Degenerates were a huge inspiration. I would have never come up with the idea or need had it not been for them. They helped immensely with gameplay and will continue to be an inspiration for future ventures. They are the true heroes.
*My university helped make me the man I am today. They unlocked the nerdy side of me and helped me continue to learn while also learning how to learn.
*My family gave me numerous words of encouragement towards computer work which made me always feel like I was on the right track.
*Hedgehog was a miracle for coding the dataset portion. They knew exactly what was needed when things weren't working quite right. By the end, we practically finished each other's sentences.
*https://python.land/deployment/pyinstaller/ helped me understand the behavior of pyinstaller and why it was spitting out extra folders

* Hat tip to anyone whose code was used
* Inspiration
* etc
