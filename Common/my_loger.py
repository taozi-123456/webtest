import sys
import logging
import os
from Common.handle_config import conf
from Common.handle_path import log_dir
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
class My_Logger(logging.Logger):
    def __init__(self,file=None):
#设置输出级别，输出渠道 ，日志格式
        super().__init__(conf.get("log","name"),conf.get("log","level"))
#设置日志输出的内容格式
        fmt='%(asctime)s %(levelname)s %(filename)s-%(lineno)d行:%(message)s'
        formatter=logging.Formatter(fmt)
#控制台渠道
#设置日志输出的渠道
        handle1=logging.StreamHandler()
        handle1.setFormatter(formatter)
        self.addHandler(handle1)
#设置控制台渠道
        if file:
            handel2=logging.FileHandler(file,encoding="utf-8")
            handel2.setFormatter(formatter)
            self.addHandler(handel2)
#是否需要写入文件
if conf.get("log","file_ok"):
    filename=os.path.join(log_dir,conf.get("log","file_name"))
else:
    filename=None
logger=My_Logger(filename)
