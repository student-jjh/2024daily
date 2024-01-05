
from functools import reduce
a = reduce(lambda x,y : y+x ,'abcde')

print(a)