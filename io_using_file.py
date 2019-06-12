poem = '''\
Programming is fun
when the work is done
'''

# 打开文件用来编辑
f = open('poem.txt', 'w')
# 向文件中写入文本
f.write(poem)
# 关闭文件
f.close()

# 如果没有特别指定
# 将默认启动read模式
f = open('poem.txt')
while True:
    line = f.readline()
    # 零长度只是EOF
    if len(line) == 0:
        break
    print(line, end='')

# 关闭文件
f.close()
