# 2. Find Angle MBC

import math

ab = int(input())
bc = int(input())
ac = math.sqrt((ab**2)+(bc**2))
mc = ac/2
bm = mc
print(round(math.degrees(math.atan(ab/bc))), chr(176), sep = '')