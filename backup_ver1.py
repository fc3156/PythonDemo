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
'''
备份文件将被打包成zip文件
zip的文件名称由当前日期和时间组成
'''
target = target_dir + os.sep + \
         time.strftime('%Y%m%d%H%M%S') + '.tar'
# 如果目标目录不存在则进行创建
if not os.path.exists(target_dir):
    os.mkdir(target_dir)

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
