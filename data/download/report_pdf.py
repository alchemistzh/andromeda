import requests

r = requests.get("http://disc.static.szse.cn/download/disc/disk01/finalpage/2018-03-31/41239c45-db7b-4aaf-a5be-dcd288d80bab.PDF")
open('300324.pdf', 'wb').write(r.content)
