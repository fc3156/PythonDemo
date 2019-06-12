shoplist = ['apple', 'mango', 'carrot', 'banana']
name = 'Swaroop'

print('Item 0 is ', shoplist[0])
print('Item 1 is ', shoplist[1])
print('Item 2 is ', shoplist[2])
print('Item 3 is ', shoplist[3])
print('Item -1 is ', shoplist[-1])
print('Item -2 is ', shoplist[-2])
print('Charater 0 is', name[0])

# slicing on a list
print('Item 1 to 3 is', shoplist[1:3])
print('Item 2 to end is', shoplist[2:])
print('Item 1 to -1 is', shoplist[1:-1])

#从字符串中切片
print('Charater 1 to 3 is', name[1:3])
print('Charater 2 to end is', name[2:])
print('Charater 1 to -1 is', name[1:-1])
print('Charater start to end is', name[:])