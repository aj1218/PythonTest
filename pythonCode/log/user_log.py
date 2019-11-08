#coding=utf-8
#输入的东西在java里面成为流媒体
import logging
import os
import datetime
class UserLog():
    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        # 控制台输入日志

        # consle=logging.StreamHandler()
        # logger.addHandler(consle)
        #
        # logger.debug("info")
        # 文件名字
        base_dir = os.path.dirname(os.path.abspath(__file__))  # 拿到文件的目录  然后在拿到文件的上一级路劲 方便拼接

        log_dir = os.path.join(base_dir, 'logs')  # 连接 成日志的路径  整个logs的路径
        data = datetime.datetime.now().strftime("%Y-%m-%d")+".log"  # 当前时间命名
        log_name = log_dir + '/' + data  # 进行拼接   就是整个文件的路径  当前时间开头的路径
        print(log_name)
        # 文件输出日志
        self.file_handle = logging.FileHandler(log_name, 'a', encoding='utf-8')  # 按照时间的日期排列
        self.file_handle.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            '%(asctime)s %(filename)s ===> %(funcName)s %(levelno)s: %(levelname)s ===>%(message)s')
        self.file_handle.setFormatter(formatter)
        self.logger.addHandler(self.file_handle)

        self.logger.debug("testasdf")


    def get_lof(self):
        return self.logger


    def close_handle(self):
        self.logger.removeHandler(self.file_handle)
        self.file_handle.close()


if __name__ == '__main__':
    user=UserLog()
    log=user.get_lof()
    log.debug("test")
    user.close_handle()


