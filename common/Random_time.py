import time
import random


class Random_time(object):
    def __init__(self):
        pass

    def get_random_time():
        """获取随机日期"""
        a1 = (2021, 10, 1, 0, 0, 0, 0, 0, 0)  # 设置开始日期时间元组（1976-01-01 00：00：00）
        a2 = (2021, 12, 31, 23, 59, 59, 0, 0, 0)  # 设置结束日期时间元组（1990-12-31 23：59：59）
        start = time.mktime(a1)  # 生成开始时间戳
        end = time.mktime(a2)  # 生成结束时间戳
        # 随机生成10个日期字符串
        t = random.randint(start, end)  # 在开始和结束时间戳中随机取出一个
        date_touple = time.localtime(t)  # 将时间戳生成时间元组
        date = time.strftime("%Y-%m-%d %H:%M:%S", date_touple)  # 将时间元组转成格式化字符串（1976-05-21）
        return date


if __name__ == '__main__':
    print(Random_time.get_random_time())
