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
        if not isinstance(url, str):
            raise TypeError("URL must be a string.")
        
        if not url:
            print("No URL entered.")
            return False

        url_parts = url.split('/')
        for index, part in enumerate(url_parts):
            if part in ['album', 'track']:
                if index +1 < len(url_parts) and url_parts[index + 1].strip():
                    return True
                else:
                    print("Invalid URL. Missing album/track name.")
                    return False
        
        print("Invalid URL. Please enter a Bandcamp URL to an album or a track.")
        return False