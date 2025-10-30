import requests
from bs4 import BeautifulSoup
import re

def get_leaders():
    leaders_per_country = {}
    # Defining the URLs
    root_url = "https://country-leaders.onrender.com"
    # Getting the cookies
    cookie_url = "/cookie"
    cookies_req = requests.get(root_url + cookie_url).cookies
    
    # Getting the countries
    countries_url = "/countries"
    # query the /countries endpoint using the get() method and store it in the req variable (1 line)
    countries_req = requests.get(root_url + countries_url, cookies=cookies_req).json()

    # To ensure that all requests will share the same session, 
    # therefore the same cookies.
    session = requests.Session()
    for country in countries_req:
        try: 
            leaders_per_country[country] = session.get(f"{root_url}/leaders", params={"country": country}, cookies= cookies_req).json()
            for leader in leaders_per_country[country]:
                # print(leader) to see what i get
                url = leader["wikipedia_url"]
                first_paragraph = get_first_paragraph(url, session)
                leader["first_paragraph"] = first_paragraph
        except Exception as exc:
            # new cookie + continue
            print(f"Error fetching leaders for {country}, exception= {exc}")
            cookies_req = requests.get(root_url + cookie_url).cookies  # new cookie
            continue
        
    return leaders_per_country

def get_first_paragraph(wikipedia_url, session):
    headers = {"user-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; )"}
    print(wikipedia_url)
    html_text = session.get(wikipedia_url, headers = headers).text
    soup = BeautifulSoup(html_text, "html.parser")
    for paragraph in soup.find_all("p"):
    # Finds <b> and checks if it starts with element <p>. 
        if paragraph.find("b") == paragraph.contents[0]:
            first_paragraph = paragraph.get_text(strip=True) # I used strip, to make the text cleaner.
            first_paragraph = re.sub(r'\[.*?\]', '', first_paragraph) # <- Added a line here
            return first_paragraph
        