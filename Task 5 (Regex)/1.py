# 1. Detect Floating Point Number

import re
for i in range(int(input())):
    print(bool(re.search(r"^([-\+])?\d*\.\d+$", input())))