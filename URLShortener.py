import string
import random

class URLShortener:
    def __init__(self):
        self.url_mapping = {}  # Our secret map of shortened URLs and their original long counterparts
        self.base_url = "http://short.url/"  # Our kingdom of shortness, where all URLs aspire to be

    def generate_short_url(self):
        """Generate a random short URL. Because why have a long URL when you can have a short one, am I right?"""
        characters = string.ascii_letters + string.digits
        short_url = ''.join(random.choice(characters) for _ in range(6))
        return short_url

    def shorten_url(self, long_url):
        """Shorten a long URL. We're trimming the fat off these URLs faster than a dieting trend!"""
        if long_url in self.url_mapping.values():
            # URL already shortened, return existing short URL
            for short_url, original_url in self.url_mapping.items():
                if original_url == long_url:
                    return self.base_url + short_url
        else:
            # Generate a new short URL
            short_url = self.generate_short_url()
            self.url_mapping[short_url] = long_url
            return self.base_url + short_url

    def expand_url(self, short_url):
        """Expand a short URL to its original long URL. Sometimes it's nice to stretch out and see the full picture!"""
        short_url = short_url.replace(self.base_url, '')
        if short_url in self.url_mapping:
            return self.url_mapping[short_url]
        else:
            return "Short URL not found. Like a needle in a haystack, but with fewer cows."

shortener = URLShortener()
long_url = input("Enter the long URL to shorten: ")
short_url = shortener.shorten_url(long_url)
print("Shortened URL:", short_url)

expanded_url = shortener.expand_url(short_url)
print("Expanded URL:", expanded_url)
