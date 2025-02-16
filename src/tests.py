import unittest
from bandcamp_validator import BandcampValidator

class test_validator(unittest.TestCase):
    def setUp(self):
        """
        Set up test cases.
        """

        self.valid_album_urls = [
            "bandcamp.com/album/album-name",
            "artist.bandcamp.com//album/album-name",
            "https://artist.bandcamp.com/album/album-name",
            "https://artist.bandcamp.com/album/album-name-with-numbers1231",
        ]

        self.valid_track_urls = [
            "bandcamp.com/track/track-name",
            "artist.bandcamp.com//track/track-name",
            "https://artist.bandcamp.com/track/track-name",
            "https://artist.bandcamp.com/track/track-name-with-numbers1231",
        ]

        self.invalid_urls = [
            "",
            "artist.bandcamp.com",
            "bandcamp.com",
            "https://google.com",
            "https://artist.bandcamp.com",
            "https://bandcamp.com",
            "https://bandcamp.com/album",
            "https://bandcamp.com/track",
        ]

    def test_valid_album_urls(self):
        """Test that valid album URLs return True"""
        for url in self.valid_album_urls:
            with self.subTest(url=url):
                self.assertTrue(
                    BandcampValidator.is_album_or_track(url),
                    f"Failed to validate album URL: {url}"
                )

    def test_valid_track_urls(self):
        """Test that valid track URLs return True"""
        for url in self.valid_track_urls:
            with self.subTest(url=url):
                self.assertTrue(
                    BandcampValidator.is_album_or_track(url),
                    f"Failed to validate track URL: {url}"
                )

    def test_invalid_urls(self):
        """Test that invalid URLs return False"""
        for url in self.invalid_urls:
            with self.subTest(url=url):
                self.assertFalse(
                    BandcampValidator.is_album_or_track(url),
                    f"Failed to invalidate URL: {url}"
                )

    def test_none_input(self):
        """Test that None input raises TypeError"""
        with self.assertRaises(TypeError):
            BandcampValidator.is_album_or_track(None)

    def test_missing_content_after_identifier(self):
        """Test URLs that have album/track but no content after"""
        invalid_urls_missing_content = [
            "artist.bandcamp.com/album/",
            "artist.bandcamp.com/track/",
            "artist.bandcamp.com/album",
            "artist.bandcamp.com/track",
            "artist.bandcamp.com/album/ ",
            "artist.bandcamp.com/track/ ",
        ]
        for url in invalid_urls_missing_content:
            with self.subTest(url=url):
                self.assertFalse(
                    BandcampValidator.is_album_or_track(url),
                    f"Failed to invalidate URL with missing content: {url}"
                )

if __name__ == "__main__":
    unittest.main()