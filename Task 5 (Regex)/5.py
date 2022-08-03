# 5. Re.start() & Re.end()

import re

string, sub_string = input(), input()
matches = re.finditer(r'(?=('+sub_string+'))', string)

match_1 = False
for match in matches:
    match_1 = True
    print((match.start(1), match.end(1) - 1))

if match_1 == False:
    print((-1, -1))