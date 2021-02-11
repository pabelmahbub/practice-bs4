import requests
import urllib.request

from bs4 import BeautifulSoup

r = requests.get("https://search.rakuten.co.jp/search/mall/%E3%83%9E%E3%82%B9%E3%82%AF/402788/")
c = r.content
soup = BeautifulSoup(c,"html.parser")
all = soup.find_all("div",{"class","searchresultitem"})
print(all)

all1= all[0].find("data-shop-id",{"class","dui-item searchresultitem"})

print(all1)



#first_class=all.find_all("div",{"class","description tags"}[0].text)
#print(len(all))
#print(all[0]).find("title",{"class","description tags"}))
