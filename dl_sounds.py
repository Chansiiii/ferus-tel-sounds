import re
import csv
import urllib
import urllib.request

def dl(name,number):
    url = f"https://s3-us-west-1.amazonaws.com/vocs/Bursts/{name}/{number}.mp3"
    print(url)
    data = urllib.request.urlopen(url)

    f = open(f"${name}_${number}.mp3", 'wb')
    f.write(data.read())
    f.close()


def get_url(htmlString):
    # print(htmlString)
    return re.findall(r'(?<=&quot;).*?(?=.mp3&quot)', htmlString[0])[0]
    # return htmlString[0].findall("(?<=playx(&quot;).*?(?=mp3&quot)")


# dl("Adam", "001")
urls = []
with open('urls.csv', 'r') as f:
    reader = csv.reader(f)
    urls = list(map(get_url, reader))
counts = {}

for url in urls:
    [name, number] = url.split('/')
    print(name, number)
    dl(name,number)