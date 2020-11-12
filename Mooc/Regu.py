import re
pattern = re.compile(r'[1-9]{5}')
match = pattern.match('12345 54321')
print(match.group(0))
print(match.string)
print(match.re)
print(match.pos)
print(match.endpos)
print(match.start())
print(match.end())

match1 = re.search(r'PY.*?N', 'PYANBNCNDN')
print(match1.group(0))