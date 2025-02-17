
from bs4 import BeautifulSoup
from curl_cffi.requests.exceptions import RequestException, HTTPError
import stealth_requests as requests
from typing import Optional

class BandcampScraper:
    def __init__(self):
        self.session = None

    async def fetch_url(self, url: str) -> str:
        """
        Fetch HTML content from a Bandcamp URL.
        
        Args:
            url (str): The URL to fetch
            
        Returns:
            Optional[str]: The HTML content if successful, None if failed
        """

        if not url:
            raise ValueError("No URL provided.")

        try: 
            # add https:// if not present
            if not url.startswith(('https://', 'http://')):
                url = 'https://' + url

            # strip possible parameters and whitespace
            url = url.split('?')[0].strip()
            
            response = requests.get(url)
            response.raise_for_status() # raise an exception for 4xx/5xx status codes
            return response.text
        
        except requests.exceptions.RequestException as e:
            print(f"Error fetching URL {url}: {str(e)}")
            raise  
        

    async def get_track_fans(self, url: str) -> Optional[list[dict[str, str]]]:
        """
        Get all fans for a specific track/album.
        
        Args:
            url (str): The track/album URL
            
        Returns:
            Optional[list[dict[str, str]]]: List of fan dictionaries if successful,
                                            None if failed
        """

        html = await self.fetch_url(url)
        if html:
            return self.parse_fans(html)
        return None

    def parse_fans(self, html: str) -> list[dict[str, str]]:
        """
        Parse fans from the HTML content.

        Args:
            html (str): The HTML content to parse

        Returns:
            list[dict[str, str]]: List of fans with their details
        """

        soup = BeautifulSoup(html, 'html.parser')
        fan_elements = soup.find_all('a', class_='fan pic')

        fans = []        
        for fan in fan_elements:
            profile_link = fan['href']
            username = fan.find('div', class_='name').text.strip()

            fans.append({
                'username': username,
                'profile_link': profile_link
            })

        return fans
    
    async def process_multiple_urls(self, urls: list) -> dict[str, list[dict[str, str]]]:
        """
        Process multiple URLs and get the fans for each.
        
        Args:
            urls (list): List of URLs to process
            
        Returns:
            list[dict[str, str]]: List of fans for each URL
        """

        results = {}
        for url in urls:
            fans = await self.get_track_fans(url)
            if fans:
                results[url] = fans

        return results