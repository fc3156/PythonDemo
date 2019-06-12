import pickle

# 我们存储相关对象的文件的名称
shoplistfile = 'shoplist.data'
# 需要购买的物品清单
shoplist = ['apple', 'mango', 'carrot']

# 准备写入文件,二进制形式写入
f = open(shoplistfile, 'wb')
# 转储对象到文件
pickle.dump(shoplist, f)
f.close()

# 清除shoplist变量
del shoplist
# 重新打开存储文件，二进制形式读出
f = open(shoplistfile, 'rb')
# 从文件中载入对象
storelist = pickle.load(f)
print(storelist)
