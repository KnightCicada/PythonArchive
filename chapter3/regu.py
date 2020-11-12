import re
str = '<H1>Chapter 1 - 介绍正则表达式</H1>'
str1 = 'http://www.runoob.com:80/html/html-tutorial.html'


pattern = re.compile(r'<.*>')
pattern1 = re.compile(r'(\w+):\/\/([^/:]+)(:\d*)?([^# ]*)')


result1 = re.match(pattern, str)
if result1:
    print(result1.group())
else:
    print('1:匹配失败')

