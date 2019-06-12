print('Simple Assignment')
shoplist = ['apple', 'mago', 'carrot', 'banana']
# mylist只是指向同一个对象的另一个名称
mylist = shoplist
# 我购买了第一项的项目，所以我将从列表中删除
del shoplist[0]

print('shoplist is ', shoplist)
print('mylist is ', mylist)
# 由结果可以看出可以看出上面的两个list是同一个对象

# 通过生成一份完整的切片制作一份列表的副本
mylist = shoplist[:]
# 删除第一个项目
del mylist[0]

print('shoplist is ', shoplist)
print('mylist', mylist)
