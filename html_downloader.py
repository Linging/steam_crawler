from urllib import request
import http.cookiejar
import json

class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return None

        cj = http.cookiejar.CookieJar()
        opener = request.build_opener(request.HTTPCookieProcessor(cj))
        request.install_opener(opener)
        response = request.urlopen(url)
        print("Status Code:",response.getcode())
        if response.getcode() != 200:
            return None
        data = response.read().decode('UTF-8')
        fin_data = json.loads(data)
        return fin_data


