#1 将list 拆分为奇偶,三等分亦然
a=[1,2,3,4]
b = a[::2]
c = a[1::2]

# 2多[]命名
a,b,c =[[]  for _ in range(3)]

#reduce list字符串合并
from functools import reduce
line = [str(i) for i in range(10)]
line[4] = reduce( lambda x,y: x+y , line[4:])
