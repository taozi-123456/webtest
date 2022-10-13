import os
BaseDir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BaseDir)
#测试用例的路径
TestCase_Dir=os.path.join(BaseDir,"TestCases")

#测试数据路径
TestDatas_Dir=os.path.join(BaseDir,"TestDatas")
print(TestDatas_Dir)
#测试报告路径
reports_dir=os.path.join(BaseDir,"OutPuts","reports")
#测试日志路径
log_dir=os.path.join(BaseDir,"OutPuts\logs")
#测试失败截图日志
screenshots_dir=os.path.join(BaseDir,"OutPuts\Screenshots")
print(screenshots_dir)
#配置文件路径
conf_dir=os.path.join(BaseDir,"conf")
print(conf_dir)