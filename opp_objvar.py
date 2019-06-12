# coding=UTF-8

class Robot:
    '''表示有一个带有名字的机器人'''
    # 一个类变量，用来统计机器人的数量
    population = 0

    # 当对象变量和类变量名称相同时，类变量会被隐藏
    # 就相当于构造函数,name变量属于对象，不属于类
    def __init__(self, name):
        self.name = name
        print("(Initializing {})".format(self.name))
        # 当有机器人被创建的时候机器人的数量会增加
        Robot.population += 1

    # 就相当于创建析构函数
    def die(self):
        print("{} is being destroyed!".format(self.name))
        Robot.population -= 1
        if Robot.population == 0:
            print("{} was the last one".format(self.name))
        else:
            print("There are still {:d} robots working.".format(Robot.population))
            #print("There are still {:d} robots working.".format(self.__class__.population))

    def say_hi(self):
        '''sasdlkjfksdjfkjksdlfj'''
        print("Greetings,my masters call me {}".format(self.name))
        # print('另外一种访问population的方式：self.__class__.polulation'.format(__class__.polulation))

    # 这就相当于静态方法
    @classmethod
    def how_many(cls):
        print("We have {:d} robots.".format(cls.population))


droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()

droid2 = Robot("c-3po")
droid2.say_hi()
Robot.how_many()

print("\nRobots can do some work here!\n")
print(Robot.say_hi.__doc__)

print("finished,destroy these robots")
droid1.die()
droid2.die()
