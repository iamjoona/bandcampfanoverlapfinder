class BandcampValidator:
    @staticmethod
    def is_valid_bandcamp_url(url: str) -> bool:
        # check that the url contains bandcamp.com
        if 'bandcamp.com' not in url:
            print("Invalid URL. Please enter a Bandcamp URL.")
            return False
        
        # check that the url contains either /track/ or /album/
        if not BandcampValidator.is_album_or_track(url):
            return False

        return True

    @staticmethod
    def is_album_or_track(url: str) -> bool:
        # check that the url contains either /track/ or /album/
        url_parts = url.split('/')
        if 'track' not in url_parts and 'album' not in url_parts:
            print("Invalid URL. Please enter a Bandcamp URL to an album or a track.")
            return False
        return True