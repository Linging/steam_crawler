from bs4 import BeautifulSoup
import re
import urllib.parse
class HtmlParser(object):

    def _get_wanted_urls(self, page_url, soup):
        pass
    #     wanted_urls = set()
    #     /market/listing/730(game_number)/item_name
    #     links = soup.find_all('a', href=re.compile(r"/market/listings/\d+/.+"))
    #     for link in links:
    #         wanted_url = link['href']
    #         wanted_full_url = urllib.parse.urljoin(page_url, wanted_url)
    #         wanted_urls.add(wanted_full_url)
    #     return wanted_urls

    def _get_new_data(self, page_url, soup):
        res_data = {}

        for x in range(100):
            record = {}

            item_name = soup.find('div', class_="market_listing_row market_recent_listing_row market_listing_searchresult",id="result_%s" % (x)).find('span', class_="market_listing_item_name")
            record['name'] = item_name.get_text()

            item_price = soup.find('div', class_="market_listing_row m"
                                                 "arket_recent_listing_row market_listing_searchresult",id="result_%s" % (x)).find('span', class_="sale_price")
            record['price'] = item_price.get_text()

            belongs_game = soup.find('div', class_="market_listing_row market_recent_listing_row market_listing_searchresult",id="result_%s" % (x)).find('span', class_="market_listing_game_name")
            record['game'] = belongs_game.get_text()

            item_quantity = soup.find('div', class_="market_listing_row market_recent_listing_row market_listing_searchresult",id="result_%s" % (x)).find('span', class_="market_listing_num_listings_qty")
            record['quantity'] = item_quantity.get_text()

            res_data['item%s' % (x)] = record

        print("-------------------------------------------")
        return res_data


    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont['results_html'], 'html.parser', from_encoding='utf-8')
        wanted_urls = self._get_wanted_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return wanted_urls, new_data
