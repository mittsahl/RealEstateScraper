#!/usr/bin/env python3

from bs4 import BeautifulSoup
import sys
import requests
import json
import time


class Scraper():
    results = []
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'cookie': 'zguid=23|%2472166284-0595-4707-9e2b-f666df25c28b; zgsession=1|f50d2ce1-42d7-4ab4-90c7-e0918a5eb7f7; _ga=GA1.2.1067094167.1607048079; _gid=GA1.2.1967567774.1607048079; zjs_anonymous_id=%2272166284-0595-4707-9e2b-f666df25c28b%22; _pxvid=773d17ee-35d6-11eb-abe6-0242ac12000e; _gcl_au=1.1.1945698939.1607048188; KruxPixel=true; DoubleClickSession=true; _fbp=fb.1.1607048188761.929980895; _pin_unauth=dWlkPU9XSmxNalZtT0dVdE5EQXdaaTAwT1dNd0xUZzVZVEF0T1RGaE56RTBaVGd4WWpZMQ; __gads=ID=0bbfa4ff5aa58fb1:T=1607048197:S=ALNI_Maypn5EQAKdqTRjGTDtVcDYs7kU6Q; KruxAddition=true; ki_r=; ki_s=; ki_t=1607048453777%3B1607048453777%3B1607048494747%3B1%3B17; G_ENABLED_IDPS=google; g_state={"i_p":1607058389941,"i_l":1}; loginmemento=1|50e99b173ebf09fb7bd1c7fba4fdff08419a30667ec555f21b0d51a7db5a8ae0; userid=X|3|29e1761cc3c3dafe%7C10%7CiK5mBzfGCC9xzM1wSNMig7K1HDCq3pAl; zjs_user_id=%22X1-ZU14t5dh5242byh_6ed95%22; ZILLOW_SSID=1|; JSESSIONID=8F81F5C7E65C6473F36411C2837B00B5; ZILLOW_SID=1|AAAAAVVbFRIBVVsVEjh6l%2B8Qns5UV%2Bul2YFW8ViYve%2FR2XurTaRqOfIrkdP7l1bU4tBhDf6H7T75MnyRRFaLYz4kO77a; _gat=1; _pxff_cc=U2FtZVNpdGU9TGF4Ow==; _pxff_bsco=1; _px3=e5ea9a4ff3bc282f8a93eaf10c63b5236bfd4278bf4a8309312ec996b381a940:MQHHLY/seLoZP3+flf98O5gMym81xfzYK70HybRHaHeKJ9PdEK7FDXGcB4Xw93GZqN2vYMtFm5uRtHc7bpWZ3Q==:1000:/QLus6TZFUCbtEO1uH+iIvyrkbPoRqRjaUmx1xqb6/veZF/3j3b8d2D8mu0DAu6XZ18N7XyLc3hQQlNowRSv5PdrwvZt02hJ/1jqK0v45SLjVCrhSGEZBcabXgqiqyA48gemYz6wOl5j851Mu2+uXSsHx14p8IDVypzXqdnVyU4=; _uetsid=b79058d035d611eba4c6b7f971edd880; _uetvid=b791248035d611ebacf4ab9bb675d373; AWSALB=GtQLq5rPs7pBC9X4+vVLJ+Fpsg6A0pdLW05P5M7vBvzvlsbtmz3ZdtwgNkWoXp+0cITsB8GKABneL3XqvlsZ+xAW3cMlaXpyYIcVWsh8hXi6fLcisEoQlK/ME2YU; search=6|1609676969090%7Crect%3D42.053038515082974%252C-71.625914203125%252C40.948449404088095%252C-73.889097796875%26rid%3D11%26disp%3Dmap%26mdm%3Dauto%26p%3D1%26z%3D1%26pt%3Dpmf%252Cpf%26fs%3D1%26fr%3D0%26mmm%3D1%26rs%3D0%26ah%3D0%26singlestory%3D0%26housing-connector%3D0%26abo%3D0%26garage%3D0%26pool%3D0%26ac%3D0%26waterfront%3D0%26finished%3D0%26unfinished%3D0%26cityview%3D0%26mountainview%3D0%26parkview%3D0%26waterview%3D0%26hoadata%3D1%26zillow-owned%3D0%263dhome%3D0%09%0911%09%09%09%09%09%09; AWSALBCORS=RygzhLx0nbmtZGYIyv4GesYCgifWAuslr1onZYtHDHMVsAeTdsK0zQDqccoDV7rrrNiVYLk23E8WSKghBPhGpbS+ZqUo1H4Y1OKX5lQBuNrYDyOmPkDrFPb7Dw1O',
        'pragma': 'no-cache',
        'referer': 'https://www.zillow.com/homes/{}_rb/'.format(sys.argv[1]),
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site' : 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36'
            }
    
    def fetch(self, url, params):
        response = requests.get(url, headers=self.headers)
        return response
    
    def run(self):
        params = {
                'searchQueryState': '{"pagination":{},"usersSearchTerm": "connecticut","mapBounds":{"west":-78.18475209375,"east":-69.96697865625,"south":39.4453917112731,"north":43.851041386889044},"mapZoom":7,"regionSelection":[{"regionId":11,"regionType":2}],"isMapVisible":false,"filterState":{"ah":{"value":true},"sort":{"value":"globalrelevanceex"}},"isListVisible":true}'
        }
        url = "https://www.zillow.com/homes/{}_rb/".format(sys.argv[1])
        response = self.fetch(url, params)
        self.parse(response.text)
    
    def parse(self, response):    
        content = BeautifulSoup(response, "html.parser")
        deck = content.find('ul', {'class': 'photo-cards photo-cards_wow photo-cards_short'})
        for card in deck.contents:
            script = card.find('script', {'type': 'application/ld+json'})
            if script:
                script_json = json.loads(script.contents[0])
                self.results.append({
                    'Address' : script_json['name'],
                    'SqFeet' : script_json['floorSize']['value'],
                    'Url' : script_json['url'],
                    'Price' : card.find('div', {'class': 'list-card-price'}).text
                    })
        for i in range(0, len(self.results)):
                print(self.results[i])
                print("\n\n")

                
if __name__ == '__main__':
    scraper = Scraper()
    scraper.run()
