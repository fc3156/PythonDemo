import os
import time

'''
需要备份的文件与目录将被指定在一个列表中
例如在windows下：
source=['"c:\\My Documents"','C:\\Code']
在linux中
source=['/home/jasonfeng/Downloads/swa']
在这里注意我们必须在字符串中使用双引号
用于括起其中包含空格的名称
'''
source = ['/home/jasonfeng/Downloads/swa/testFolder']
'''
备份文件必须存储在一个主备份目录中
例如在windows下：
target_dir='E:\\Backup'
在linux下：
target_dir=‘/home/jasonfeng/Downloads/swa’
'''
target_dir = '/home/jasonfeng/Downloads/swa'
# 如果目标目录不存在则进行创建
if not os.path.exists(target_dir):
    os.mkdir(target_dir)

# 将当前日期作为主备份目录下的子目录名称
today = target_dir + os.sep + time.strftime('%Y%m%d')  # os.sep指代的是斜杠
# 将当前时间作为tar文件的文件名
now = time.strftime('%H%M%S')
# 添加一条来自用户的注释当做文件名称
comment = input('Enter a comment--> ')
# 下面检查是否有评论输入
if len(comment) == 0:
    target = today + os.sep + now + '.tar'
else:
    target = today + os.sep + now + '_' + \
             comment.replace(' ', '_') + '.tar'

if not os.path.exists((today)):
    os.mkdir(today)
    print('Successfully created diredtory', today)
# 使用tar命令将文件进行打包
tar_command = 'tar -cvPf {0} {1}'.format(target, ' '.join(source))

# 运行备份
print('tar command is：')
print(tar_command)
print('Running:')
if os.system(tar_command) == 0:
    print('Successful backup to', target)
else:
    print('BackUp failed!!!')
