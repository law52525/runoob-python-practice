import requests
import re

with open("questions.md", "w", encoding="utf-8") as f:
    for i in range(1, 101):
        h = requests.get("http://www.runoob.com/python/python-exercise-example{}.html".format(str(i)))
        # 缺44题 两个 3 行 3 列的矩阵，实现其对应位置的数据相加，并返回一个新矩阵（不符合规则的例外）
        r = re.search(r'<p><strong>题目：</strong>(.*?)</p>', h.content.decode("utf-8"), re.S)
        if r:
            s = "{:>3}. {}\n".format(i, r.group(1).strip())
            f.write(s)
