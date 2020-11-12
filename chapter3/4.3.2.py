#coding:utf-8
import bs4
import re
from bs4 import BeautifulSoup
html_str = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2"><!-- Lacie --></a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
soup = BeautifulSoup(html_str, 'lxml')
print(soup.prettify())

print('soup.name:', soup.name)
print('soup.title.name:', soup.title.name)
print('soup.p.name:', soup.p.name)
print('soup.title.string:', soup.title.string)
print(soup.p['class'])
print('soup.p.attrs:', soup.p.attrs)
print('soup.p.string:', soup.p.string)

print('type(soup.name):', type(soup.name))
print('soup.name', soup.name)
print('soup.attrs', soup.attrs)

print('soup.a.string:', soup.a.string)
print('type(soup.a.string):', type(soup.a.string))
# if type(soup.a.string)==bs4.element.Comment:
#     print(soup.a.string)

print('-----------------------------------')
print('3.1子节点')
print('soup.head.contents:', soup.head.contents)

print('child')
for child in soup.head.children:
    print(child)

for child in soup.head.descendants:
    print(child)

print('string')
print('tag中包含多个字符串')
for string in soup.strings:
    print(repr(string))

print("\n")

print('tag中包含多个字符串，去除空格空行')
for string in soup.stripped_strings:
    print(repr(string))

print('-----------------------------------')
print('3.2父节点')
print('soup.title.parent', soup.title.parent)
print('遍历a的父节点')
for parent in soup.a.parents:
    if parent is None:
        #对于最后一个tag
        print(parent)
    else:
        print(parent.name)

print('-----------------------------------')
print('3.3兄弟节点')
print('soup.p.next_sibling:', soup.p.next_sibling)
print('soup.p.prev_sibling:', soup.p.prev_sibling)
print('soup.p.next_sibling.next_sibling:\n', soup.p.next_sibling.next_sibling)
print('迭代输出当期节点的兄弟节点')
for sibling in  soup.a.next_siblings:
    print(repr(sibling))

print('-----------------------------------')
print('3.4前后节点')
print('soup.head.next_element', soup.head.next_element)
print('\n')
print('遍历后节点')
for element in soup.a.next_elements:
    print(repr(element))

print('-----------------------------------')
print('4搜索文档树')
print('name参数')
print("soup.find_all('b'):", soup.find_all('b'))


for tag in soup.find_all(re.compile('^b')):
    print(tag.name)

print("soup.find_all(['a', 'b']):\n", soup.find_all(['a', 'b']))

print("soup.find_all(True):\n")
for tag in soup.find_all(True):
    print(tag.name)

print('自定义方法')
def hasClass_Id(tag):
    return tag.has_attr('class') and tag.has_attr('id')
print(soup.find_all(hasClass_Id))

print('kwargs参数')
print("soup.find_all(id='link2')\n", soup.find_all(id='link2'))
print("soup.find_all(href=re.compile('elsie'))\n", soup.find_all(href=re.compile('elsie')))
print("soup.find_all(id=True)\n", soup.find_all(id=True))
print("soup.find_all(class_='sister')\n", soup.find_all('a', class_='sister'))
print("soup.find_all(href=re.compile('elsie'), id='link1')\n", soup.find_all(href=re.compile('elsie'), id='link1'))

data_soup = BeautifulSoup('<div data-foo="value">foo!</div>', 'lxml')
print(data_soup.find_all(attrs={'data-foo': 'value'}))

print('text参数')
print(soup.find_all(text='Elsie'))
print(soup.find_all(text=['Elsie', 'Tillie', 'Lacie']))
print(soup.find_all(text=re.compile('Dormouse')))
print(soup.find_all("a", text="Elsie"))

print('limit参数')
print(soup.find_all('a', limit=2))

print('recursive参数')
print(soup.find_all('title'))
print(soup.find_all('title', recursive=False))


