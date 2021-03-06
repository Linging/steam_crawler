from steam import url_manager, html_downloader, html_parser, html_outputer
import time
class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self,root_url):
        count = 1
        timeout = 85
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print('craw %d : %s'%(count,new_url))
                html_cont = self.downloader.download(new_url)
                wanted_urls, new_data = self.parser.parse(new_url, html_cont)
                self.outputer.collect_data(new_data)

                count = count + 1

            except:
                print('craw failed!')
                self.urls.add_failed_url(new_url)
                count = count + 1

            if count == 26:
                time.sleep(timeout)
                count = 1


        self.outputer.output_html()


if __name__=="__main__":
    root_url = "http://steamcommunity.com/market/search?q=#p1_popular_desc"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)