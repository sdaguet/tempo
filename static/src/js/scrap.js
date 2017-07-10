import requests
from lxml import html

#storing response
response = requests.get('http://pycoders.com/archive')
#creating lxml tree from response body
tree = html.fromstring(response.text)

#Finding all anchor tags in response
print tree.xpath('//divass="campaign"]/a/@href')