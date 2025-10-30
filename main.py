from pathlib import Path
from scraper.leaders_scraper import get_leaders
from scraper.utils import save

if __name__ == "__main__":

    leaders_data = get_leaders()

    data_folder = Path("data")
    data_folder.mkdir(exist_ok=True)

    save(leaders_data)
    print("Leaders data fetched and saved successfully!")
