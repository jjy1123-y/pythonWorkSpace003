import urllib.request
import re

url = "http://finance.sina.com.cn/money/forex/hq/USDCNY.shtml"
response = urllib.request.urlopen(url)
print(response)
html = response.read().decode('gbk')
print(html)
pattern = re.compile('.*?.*?(.*?)')
rate = pattern.findall(html)[0]
print(rate)