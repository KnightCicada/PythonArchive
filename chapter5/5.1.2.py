import json
import csv

# json编码
str = [{"username": "七夜", "age": 24}, (2, 3), 1]
json_str = json.dumps(str, ensure_ascii=False)
print(json_str)

with open('qiye.txt', 'w') as fp:
    json.dump(str, fp=fp, ensure_ascii=False)

# json解码
new_str = json.loads(json_str)
print(new_str)
with open('qiye.txt', 'r') as fp:
    print(json.load(fp))

# 存储为csv
headers = ['ID', 'UserName', 'Password', 'Age', 'Country']
rows = [(1001, "qiye", "qiye_pass", 24, "China"),
        (1002, "Mary", "Mary_pass", 20, "USA"),
        (1003, "Jack", "Jack_pass", 20, "USA"),
        ]

with open('qiye.csv', 'w') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headers)
    f_csv.writerows(rows)

# 读取csv
with open('qiye.csv', 'r') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    print(headers)
    for row in f_csv:
        print(row)

# 使用字典序列读取csv
with open('qiye.csv', 'r') as f:
    f_csv = csv.DictReader(f)
    for row in f_csv:
        print(row.get('UserName'), row.get('Password'))
