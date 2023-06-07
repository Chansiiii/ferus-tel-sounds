
import csv
import re

def get_url(htmlString):
    # print(htmlString)
    return re.findall(r'(?<=&quot;).*?(?=.mp3&quot)', htmlString[0])[0]
    # return htmlString[0].findall("(?<=playx(&quot;).*?(?=mp3&quot)")

urls = []
with open('urls.csv', 'r') as f:
    reader = csv.reader(f)
    # elements = reader.lines
    # elements = list(reader)
    # print(elements)
    urls = list(map(get_url,reader))
    # print(urls)

            # map elements to a list
        # for each element in list
    # f.close()

# print(urls)

counts = {}
for url in urls:
    [name, number] = url.split('/')

    if name in counts:
        counts[name] += [number]
    else:
        counts[name] = [number]
    

for [name, count] in counts.items():
    print(name, sorted(count)[-1], len(count))
    print(sorted(count))