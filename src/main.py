
from bandcamp_validator import BandcampValidator
from bandcamp_scraper import BandcampScraper
import asyncio

class BandcampFanFinder:
    def __init__(self):
        self.validator = BandcampValidator()
        self.scraper = BandcampScraper()
        # self.analyser = FanAnalyser()


async def main():
    print("Bandcamp Fan Overlap Finder")
    print("This is a simple Python program that will take in max 5 URLs and find fan overlap between them.")
    print("Please enter the URLs you would like to scrape one by one.")
    print("When you are finished, type 'done'. Exit at any time by pressing Ctrl+C.")

    scraper = BandcampScraper()
    
    # Ask for user input for upto 5 Bandcamp URLs
    urls = []
    for _ in range(0, 5):
        url = input("Enter a Bandcamp URL: ")

        if url == 'done' and len(urls) < 2:
            print("You need to enter at least 2 URLs to compare.")
            continue
        
        if url == 'done' and len(urls) >= 2:
            print(f"You've entered {len(urls)} URLs. Fetching data now.")
            await scraper.process_multiple_urls(urls)
            break

        if len(urls) == 5:
            print("You've added 5 URLs. Fetching data now.")

        # Validate the URL and then append it to the list
        if BandcampValidator.is_valid_bandcamp_url(url):
            urls.append(url)


# Run the main function
if __name__ == "__main__":
    asyncio.run(main())