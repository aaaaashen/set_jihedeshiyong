a = {1,2,3}#这是集合
print(type(a))
b = {}#这是字典
print(type(b))
c = {"甲","乙","丙","丁"}#这是集合，其与字典的区别是它只有key，而没有value值
print(type(c))
d = {'甲','乙','丙'}#同c
print(type(d))

#关于集合的操作

#1.添加key，无序
c.add("awa")
print(c)
#2.清空操作
c.clear()
print(c)

c = {"甲","乙","丙","丁"}
#3.取差集
print(c.difference(d))#与做减法等价,返回c有且d没有的
print(c-d)

#4.取交集
print(c.intersection(d))#返回两者都有的key,和&一样
print(c&d)
print(c and d)

#5.取并集
print(c.union(d))
print(c | d)
print(c or d)

#6.随机删除pop
print(c.pop())#c.pop获取了c中的一个key
print(c)

#7.移除指定数据discard
print(c.discard("丁"))

#8.更新\添加
c.update(a)
print(c)

