import os
import platform

from common.CreatePath import ModelsClass

"""
此模块存储项目所需的文件目录和文件 
"""
"""
项目的所有目录
"""
"""
os.path.abspath(__file__) 作用： 获取当前脚本的完整路径
os.path.dirname(path) 功能：去掉文件名，返回目录 
os.path.join(path1[, path2[, ...]]) 	功能：把目录和文件名合成一个路径
"""
PRO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_DIR = os.path.dirname(os.path.abspath(__file__))
CASE_DIR = os.path.join(PRO_DIR, 'cases')
DATA_DIR = os.path.join(PRO_DIR, 'data')
CONFIG_PATH = os.path.join(CONFIG_DIR, 'config.ini')
DATA_PATH = os.path.join(DATA_DIR, 'testcases.xlsx')
USER_PATH = os.path.join(CONFIG_DIR, 'userinfo.ini')
"""
日志&报告名称和目录
"""
LOG_NAME = ModelsClass.file_name('log')
LOG_DIR = os.path.join(PRO_DIR, 'log')  # 日志路径
CREATE_LOG_DIR = ModelsClass.create_dir(LOG_DIR)   #创建日志路径
LOG_PATH = os.path.join(LOG_DIR, LOG_NAME)   # 目录和名称进行拼接
REPORT_DIR = os.path.join(PRO_DIR, 'report')   # 报告路径

"""
测试环境信息 
"""
ENVIRONMENT = \
    "Windows Version:" + \
    platform.system() + \
    platform.version() + \
    platform.release() + \
    "Python Version" + \
    platform.python_build()[0]


if __name__ == '__main__':
    print('项目目录', PRO_DIR)
    print('配置文件目录', CONFIG_DIR)
    print('用例目录', CASE_DIR)
    print('测试数据目录', DATA_DIR)
    print('配置文件路径', CONFIG_PATH)
    print(LOG_DIR)
    print('日志配置文件路径', LOG_PATH)
    print(REPORT_DIR)
    print('测试数据文件路径', DATA_PATH)
    print('账户信息文件路径', USER_PATH)
