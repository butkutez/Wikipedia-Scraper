# Wikipedia Scraper 
[![Wikipedia_Scraper](https://media.wired.com/photos/5955ac6163d43b038e9bc529/3:2/w_1920,c_limit/2000px-Wikipedia-logo-v2-en-S.jpg)](https://www.wired.com/2015/12/wikipedia-is-using-ai-to-expand-the-ranks-of-human-editors/)
*Image source: [WIRED](https://www.wired.com/2015/12/wikipedia-is-using-ai-to-expand-the-ranks-of-human-editors/)*

## Project description

This project demonstrates the process of collecting and organizing structured data from multiple sources.

It involves:

- Setting up a self-contained development environment using a virtual environment.

- Querying an API to retrieve a list of countries and their past political leaders.

- Scraping Wikipedia to extract and clean short biographies of each leader.

- Saving the processed data.

The project highlights how data scraping and API querying form the initial step in a data science workflow, providing reusable techniques for future data collection tasks.


## Installation

1. **Clone the project:**

```
cmd git clone https://github.com/butkutez/Wikipedia-Scraper.git
```
2. **Navigate into the project folder**

```
cd Wikipedia-Scraper
```

3. **Run the script**

```
python main.py
```

## Repo structure

```
WIKIPEDIA-SCRAPER
├── scraper/
│   ├── __init__.py
│   └── leaders_scraper.py
├── .gitignore
├── main.py
└── leaders.json
```
## Usage

The script queries an API to retrieve a list of countries and their past political leaders, then scrapes Wikipedia to extract and clean their short biographies. The resulting dataset is displayed in the console and saved to a leaders.json file in your project directory.

```python
def main():

    # create instance
    scrapper = WikipediaScrapper()

    # fetch data         
    leaders_data = scrapper.get_leaders()   

    # save to file
    save(leaders_data)                      
    print("Leaders data fetched and saved successfully!")

if __name__ == "__main__":
    main()
```
## Timeline

This project took three days for completion.

## Personal Situation
This project was done as part of the AI & Data Science Bootcamp at BeCode.org. 

Connect with me on [LinkedIn](https://www.linkedin.com/in/zivile-butkute/).
## 

[![web_scraping_wikipedia](https://media.tenor.com/6WpI66bb6L4AAAAj/wikipedia-wikipedian.gif)](https://tenor.com/en-GB/view/wikipedia-wikipedian-knowledge-article-rabbit-gif-24558465)

*Image source: [Tenor](https://tenor.com/en-GB/view/wikipedia-wikipedian-knowledge-article-rabbit-gif-24558465)*