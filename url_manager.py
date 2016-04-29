class UrlManager(object):

    def __init__(self):
        self.new_urls = []

    def add_new_url(self, url):
        if url is None:
            return

        for x in range(29000,-100,-100):
            url = 'http://steamcommunity.com/market/search/render/?query=&start=%s&count=100&search_descriptions=0&sort_column=popular&sort_dir=desc' % (x)
            self.new_urls.append(url)

    def add_failed_url(self, url):
        self.new_urls.append(url)

    def has_new_url(self,):
        return len(self.new_urls) != 0

    def get_new_url(self):
        new_url = self.new_urls.pop()
        return new_url
