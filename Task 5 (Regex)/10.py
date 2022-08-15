# 10. Hex Colour Code

import re

n = int(input())
css = False
for i in range(n):
    s = input()
    if '{' in s:
        css = True
    elif '}' in s:
        css = False
    elif css:
        for color in re.findall('#[0-9a-fA-F]{3,6}', s):
            print(color)