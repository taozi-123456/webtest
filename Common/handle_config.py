import os.path

from configparser import ConfigParser
import os
from Common.handle_path import conf_dir
class Handleconfig(ConfigParser):
    def __init__(self,file_path):
        super().__init__()
        self.read(file_path,encoding="utf-8")

file_path=os.path.join(conf_dir+"\\conf.ini")
conf=Handleconfig(file_path)


