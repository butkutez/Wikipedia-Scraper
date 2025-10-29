# Wikipedia Scraper 

- Repository: `wikipedia-scraper`
- Type: `Consolidation`
- Duration: `3 days`
- Deadline: `31/10/2025 4:00 PM`
- Show and Tell: 2-3 people will present their work during debrief
- Team: `solo`

## Mission Objectives

In this project, we will guide you step by step through the process of:

1. Creating a self-contained development environment (virtual environment)
2. Retrieving some information from an API
3. Leveraging your knowledge to scrape a website that does not provide an API
4. Saving the output for later processing

More specifically, in this project we will query an API to obtain a list of countries and their past political leaders. We then extract and sanitize their short bio from Wikipedia. Finally, we save the data.

Scraping data is often the first coding step of a data science project (meaning, the data collection) and you will likely come back to it in the future.

![scraping](https://media4.giphy.com/media/Xe02toxlUsztG7iQgb/giphy.gif?cid=ecf05e47lixeo6qe5y4ooabkh0hfdz0t1pio4h0qgbngjq0n&ep=v1_gifs_search&rid=giphy.gif&ct=g)

## Learning Objectives

- Use [venv](https://docs.python.org/3/library/venv.html) to isolate your Python environment
- Use [requests](https://requests.readthedocs.io/en/latest/) to call an external API are any internet link
- Use [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) to extract text from HTML
- Use proper exception handling
- Get comfortable with JSON 
- (_Optional_) Use OOP to split functionalities into classes and methods
- (_Optional_) Use regex to clean text data
- (_Optional_) Use multiprocessing to speedup your code

## The Mission

Create a scraper that builds a JSON file with the political leaders of each country you get from [this API](https://country-leaders.onrender.com/docs).

Include in this file the first paragraph of the Wikipedia page of these leaders (you'll retrieve the Wikipedia page URL from the API, which you then have to scrape yourself).

### Must-have features (MVP)

- You should have a working `wikipedia_scraper.ipynb` notebook that calls the API and creates a JSON file
- Create your own exception to include proper exception handling
- Have a nice README that explains your project.

### Nice-to-have features

- Use [Session()](https://requests.readthedocs.io/en/latest/user/advanced/) from the `requests` library instead of `get()`
- A switch to store the output as CSV instead of JSON
- Speed up the execution using multiprocessing

### Steps

Let's get to the heart of it. **Read through all of the below before starting!**

#### 0. Setup and preparation
- Create a GitHub repo with a name that makes sense (for example, `wikipedia-scraper`)
- Create a virtual environment using [venv](https://docs.python.org/3/library/venv.html) or through VS Code directly. Don't forget to add it to your `.gitignore` file. Note: If you create it through VS Code, normally .gitignore will be automatically created!
- **Read the docs from the [API](https://country-leaders.onrender.com/docs)!**
- Copy the `wikipedia_scraper.ipynb` file from your fork into your new project repo.

You're ready to go!

#### 1. Complete the first MVP (Notebook)
- Activate your environment and install the required modules (e.g. request, and beautifulsoup). 
- Create a `requirements.txt` file with the required libraries (hint: pip freeze and pipreqs might be helpful here!)

- **Now work your way through the `wikipedia_scraper.ipynb` notebook.** This notebook contains hints on calling the API endpoint, handling cookies, and extracting text with `BeautifulSoup`. Try to fill in the cells with appropriate and working code. 

Once ready, move on to the next step and integrate your code into functions, create a `src` folder where you'll put the `leaders_scraper.py` 

#### 2a. A `leaders_scraper.py` module (Second MVP - OOP)

Now that you've made sure your code works! Let's practice restructuring your solution as a class.

Code up a `WikipediaScraper` scraper object that allows you to structurally retrieve data from the API.

The object should contain at least these six attributes: 
- `base_url: str` containing the base url of the API (https://country-leaders.onrender.com)
- `country_endpoint: str` → `/countries` endpoint to get the list of supported countries
- `leaders_endpoint: str` → `/leaders` endpoint to get the list of leaders for a specific country
- `cookies_endpoint: str` → `/cookie` endpoint to get a valid cookie to query the API
- `leaders_data: dict` is a dictionary where you store the data you retrieve before saving it into the JSON file
- `cookie: object` is the cookie object used for the API calls

The object should contain at least these five methods:
- `refresh_cookie() -> object` returns a new cookie if the cookie has expired
- `get_countries() -> list` returns a list of the supported countries from the API
- `get_leaders(country: str) -> None` populates the `leader_data` object with the leaders of a country retrieved from the API
- `get_first_paragraph(wikipedia_url: str) -> str` returns the first paragraph (defined by the HTML tag `<p>`) with details about the leader
- `to_json_file(filepath: str) -> None` stores the data structure into a JSON file

#### 2b. A `main.py` script

Bundle everything together in a `main.py` file that calls the `WikipediaScraper` object and saves the data into a JSON file.

### Quality Assurance

Read our ["Coding Best Practices Manifesto"](../../guidelines/PythonCodingBestPractices/coding-best-practices-manifesto.ipynb) and apply what's in there!

As an exercise, keep the must-have version separate from the nice-to-have version by using a different branch on GitHub. Please specify that in your README too.


## Deliverables

1. Publish your source code on your personal GitHub repository
    - `main.py`
    - `src/leaders_scraper.py`
    - `leaders_data.json` → the results file with a sensible structure containing the list of historical leaders for each country together with their details and the first paragraph (`<p>`) of the Wikipedia page
2. Pimp up the README file
   - Description
   - Installation
   - Usage
   - Visuals
   - ... anything else you find useful
3. Show case your repo! We will pseudo-randomly 2-3 colleagues to share their work during Friday's debrief (4:00 PM).

## Evaluation

| Criterion      | Indicator                                                    | Yes/No |
| -------------- | ------------------------------------------------------------ | ------ |
| 1. Is complete | Executes whithout errors                                     |        |
|                | Stores the correct information from the API in the file      |        |
| 2. Is correct  | The code is well typed                                       |        |
|                | Good usage of OOP                                            |        |
| 3. Is great    | Possibility to store output as a CSV file                    |        |
|                | Correct usage of `Session()`                                 |        |
|                | Multi-processing                                             |        |

## You got this!

![You've got this!](https://media.tenor.com/Y56BShm-6V0AAAAi/wikipedia-wikipedian.gif)