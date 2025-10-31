from scraper.leaders_scraper import WikipediaScrapper

def main():

    """Fetch leaders data and save it to 'leaders.json'."""

    # create instance
    scrapper = WikipediaScrapper()
    # fetch data         
    scrapper.get_leaders()
    # save to file
    scrapper.save_to_json("leaders.json")                      
    
    print("Leaders data fetched and saved successfully!")

# run main() only if this script is executed directly
# and not when it is imported as a module in another script
if __name__ == "__main__":
    main()