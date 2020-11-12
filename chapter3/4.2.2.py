import re
pattern = re.compile(r'\d+')
result1 = re.match(pattern, '192abc')

if result1:
    print(result1.group())
else:
    print('1:匹配失败')

result2 = re.match(pattern, '1a9b2')

if result2:
    print(result2.group())
else:
    print('2:匹配失败')

result3 = re.search(pattern, 'ab123ad')

if result3:
    print(result3.group())
else:
    print('3:匹配失败')

print('split', re.split(pattern, 'a1b2c3d4'))
print('findall', re.findall(pattern, 'a1b2c3d4'))
matchiter = re.finditer(pattern, 'a1b2c3d4')
for match in matchiter:
    print(match.group())
print('\n')

line = 'aaa bbb ccc;ddd eee,fff'
print('1:', re.split(r';', line))
print('2:', re.split(r'[;,]', line))
print('3:', re.split(r'[;,\s]', line))
print('4:', re.split(r'[;]', line))
print('5:', re.split(r'([;])', line))
print('6:', re.split(r'(?:[;])', line))
