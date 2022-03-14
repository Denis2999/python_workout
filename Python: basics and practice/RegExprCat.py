import re
import sys

pattern = r"(\w)\1+"

for line in sys.stdin:
    line = line.rstrip()
    line = re.sub(pattern, r"\1", line)
    # print(line)
