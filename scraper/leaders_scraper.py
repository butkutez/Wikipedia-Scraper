import requests
from bs4 import BeautifulSoup
import re
import json

class WikipediaScrapper:
    def __init__(self):

        """
        Initialize the WikipediaScrapper with API endpoints and empty storage.
        """   
        self.root_url = "https://country-leaders.onrender.com"
        self.cookie_url = "/cookie"    
        self.countries_url = "/countries"
        self.leaders_url = "/leaders"
        self.cookie = None
        self.leaders_per_country = {}

    def refresh_cookie(self) -> object:

        """
        Fetch a new cookie from the API and update self.cookie.
        
        Returns: The new cookie object.
        """
        self.cookie = requests.get(self.root_url + self.cookie_url).cookies
        return self.cookie
    
    def get_countries(self) -> list:

        """
        Fetch the list of supported countries from the API.
        
        Returns: List of country codes/names.
        """
        if self.cookie is None:
            self.refresh_cookie()
        countries_req = requests.get(self.root_url + self.countries_url, cookies=self.cookie).json()
        return countries_req

    def get_leaders(self):

        """
        Fetch leaders for all supported countries from the API.
        Adds the first paragraph from each leader's Wikipedia page.
        Populates self.leaders_per_country.
        
        Returns: Dictionary with countries as keys and lists of leaders as values.
        """
        if self.cookie is None:
            self.refresh_cookie()
        
        # use a session so all requests share the same cookies.
        session = requests.Session()
        countries_req = self.get_countries()

        # Loop through each country and fetch leaders.
        for country in countries_req:
            try:
                # [country] accesses the value associated with the key country. 
                self.leaders_per_country[country] = session.get(f"{self.root_url}{self.leaders_url}", params={"country": country}, cookies= self.cookie).json()
                
                # Add first paragraph from Wikipedia to each leader.
                for leader in self.leaders_per_country[country]:
                    try:
                        url = leader["wikipedia_url"]
                        print(url)
                        first_paragraph = self.get_first_paragraph(url, session)
                        leader["first_paragraph"] = first_paragraph
                    except Exception as exc:
                        # If fetching fails, refresh cookie and continue.
                        print(f"Error fetching leaders for {country}, exception= {exc}")
                        self.refresh_cookie()
                        continue
            except Exception as exc:
                print(f"Error fetching leaders for {country}: {exc}")
                self.refresh_cookie()
                # Optionally retry fetching this country here
                continue
        return self.leaders_per_country

    def get_first_paragraph(self, wikipedia_url, session):

        """
        Fetch the first paragraph from a leader's Wikipedia page.
        The first paragraph is defined as the first <p> tag that starts
        with bold text (<b>), which typically contains the main description.

        Args: URL of the leader's Wikipedia page ('wikipedia_url').
        session (requests.Session): Session object used to make the HTTP request.

        Returns: Cleaned first paragraph text, or empty string if no suitable paragraph is found.
        """
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)..."}
        html_text = session.get(wikipedia_url, headers = headers).text
        soup = BeautifulSoup(html_text, "html.parser")

        # Iterate through all paragraph tags
        for paragraph in soup.find_all("p"):
        # Check if the paragraph starts with bold text ("b"). 
            if paragraph.find("b") == paragraph.contents[0]:
                first_paragraph = paragraph.get_text(strip=True)
                # Remove citation numbers like [1], [2], etc.
                first_paragraph = re.sub(r'\[\d+\]', '', first_paragraph) 
                return first_paragraph
            
        # Return empty string if no suitable paragraph found
        return ""
            
    def save_to_json(self, filepath="leaders.json"):

        """
        Save the leaders_per_country dictionary to a JSON file.
        Args: filepath (str): Path to the JSON file. Defaults to 'leaders.json'.

        Returns:None
        """
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(self.leaders_per_country, f, ensure_ascii=False, indent=2)