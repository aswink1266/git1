import requests
from datetime import datetime
from urllib.parse import urlparse
# import requests
# r = requests.get('https://api.github.com/events')
# print(type(r.json()))
url1 = urlparse('//www.cwi.nl:80/%7Eguido/Python.html')
print(url1)

t = datetime.now()
print(t.strftime('%m/%d/%Y :%H:%M:%S'))


datetime_str = '09/19/18 13:55:26'

datetime_object = datetime.strptime(datetime_str, '%m/%d/%Y %H:%M:%S')

print(type(datetime_object))
print(datetime_object)


def list_of_swapi(site, name):
      request_site = requests.get(site + str(i))
#     results = request_site.json().get("results")
#     list1 = []
#     site_next = True
#     count = 0
#     while site_next:
#         for people2 in results:
#             v = people2[name]
#             list1.append(v)
#             count += 1
#         i += 1
#         site_next = request_site.json().get("next")
#         request_site = requests.get(site + str(i))
#         results = request_site.json().get("results")
#     print(count, i - 1)
#     return list1
      i=request_site.json().get("next")
      while i:

