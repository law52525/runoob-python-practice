import requests
import re

i = 1
with open("questions.md", "w", encoding="utf-8") as f:
    h = requests.get("http://www.runoob.com/python3/python3-examples.html")
    results = re.findall(r'<a href="(.*?)".*?</a>', h.content.decode("utf-8"), re.S)
    for result in filter(lambda t: t.startswith("python3"), results):
        h = requests.get("http://www.runoob.com/python3/{}".format(result))
        r = re.search(r'<p>[^<](.*?)</p>', h.content.decode("utf-8"), re.S)
        if r:
            f.write("{:>2}. {}\n".format(str(i), r.group(1).strip().replace("\r\n", '')))
            i += 1
