# exam 2
import re

number = input()
result = re.sub('\d{4}$', '####', number)
print(result)