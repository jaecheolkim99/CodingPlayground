"""
https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/590/week-3-march-15th-march-21st/3673/

[BEST]
import random
class Codec:
    STRING = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    map = {}
    base = "http://tinyurl.com/"
    
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        rand_str = self.gen_tag()
        self.map[rand_str] = longUrl
        return self.base + rand_str

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.map[shortUrl[-6:]]
        
    def gen_tag(self):
        tag = self.gen_random_str()
        while tag in self.map:
            tag = self.gen_random_str()
        return tag

    def gen_random_str(self):
        result = ""
        for i in xrange(6):
            result += self.STRING[random.randint(0,61)]
        return result

"""
class Codec:
    def __init__(self):
        self.chars =  string.digits + string.ascii_letters
        self.urlDB = {}
    
    def getURL(self):
        return 'http://tinyurl.com/' + ''.join(random.choice(self.chars) for i in range(6))

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        shorturl = self.getURL()
        
        if shorturl not in self.urlDB:
            self.urlDB[shorturl] = longUrl
        
        return shorturl        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        if shortUrl in self.urlDB:
            return self.urlDB[shortUrl]
