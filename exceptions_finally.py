import sys
import time

f = None
try:
    f = open('poem.txt')
    # 我们常用的文件阅读风格
    while True:
        line = f.readline()
        if len(line) == 0:
            break
    print(line, end='')
    sys.stdout.flush()
    print("Press ctrl+d now")
    #为了确保它能够运行一段时间
    time.sleep(2)
except IOError:
    print("Could not find the file..")
except KeyboardInterrupt:
    print("!!You cancelled the reading from the file.")
finally:
    if f:
        f.close()
        print("Clean up!!")