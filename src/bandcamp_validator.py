class BandcampValidator:
    @staticmethod
    def is_valid_bandcamp_url(url: str) -> bool:
        """
        Check if the URL is a valid Bandcamp URL.
        
        Args: url (str): The URL to validate
        
        Returns: bool: True if valid, False if invalid
        """

        if 'bandcamp.com' not in url:
            print("Invalid URL. Please enter a Bandcamp URL.")
            return False
        
        if not BandcampValidator.is_album_or_track(url):
            return False

        return True

    @staticmethod
    def is_album_or_track(url: str) -> bool:
        """
        Check if the URL is a valid Bandcamp album or track URL.

        Args: url (str): The URL to validate

        Returns: bool: True if valid, False if invalid
        """
        
        url_parts = url.split('/')
        if 'track' not in url_parts and 'album' not in url_parts:
            print("Invalid URL. Please enter a Bandcamp URL to an album or a track.")
            return False
        return True