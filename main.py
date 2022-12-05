import pytest
import os

from Common.handle_path import reports_dir
pytest.main(['-vs',"--alluredir","OutPuts/reports/temp",])
os.system('allure generate OutPuts/reports/temp -o OutPuts/reports/allure-report --clean')#生成测试报告，将json文件生成报告保存在指定目录(OutPuts/reports)下,allure generate 测试结果数据所在目录 -o 测试报告保存的目录   --clean
#--clean 目的是先清空测试报告目录，再生成新的测试报告
#os.system('allure serve OutPuts/reports')#打开测试报告


