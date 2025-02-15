from bandcamp_validator import BandcampValidator
import requests

class BandcampScraper:
    def __init__(self):
        self.session = None

    async def fetch_url(self, url: str) -> str:
        if not BandcampValidator.is_valid_bandcamp_url(url):
            return None


        # fetch HTML from the URL

        # strip possible parameters and whitespace
        url = url.split('?')[0].strip()
        
        response = requests.get(url)
        if response.status_code == requests.codes.ok:
            return response.text
        else:
            print("Error fetching URL. Please try again.")
            return None
        
    
    def starts_with_protocol(url: str) -> bool:
        # check if the URL starts with http:// or https://
        return url.startswith('http://') or url.startswith('https://')


    def append_https(url: str) -> str:
        # append https:// to otherwise valid Basecamp URL
        if not url.startswith('https://'):
            url = 'https://' + url

    def parse_fans():
        pass