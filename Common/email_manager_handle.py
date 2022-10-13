import os.path
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from Common.handle_path import reports_dir


class EmailMange:
    """
    必备条件
    发件箱
    开通SMTP和POP3协议
    需要获取授权密码：ZTTJRFAMBRHZBBZI 用户名：hq18792950327@163.com

    """
    def send_email(self,report_name):
        """


        :return:
        """
        #定义SMTP服务器
        smtpserver="smtp.163.com"
        #发送邮件的用户名和客户端密码
        username="hq18792950327@163.com"
        password="ZTTJRFAMBRHZBBZI"#授权密码
        #接收邮件的邮箱
        receiver="18612785402@163.com"
        #创建邮件对象
        message=MIMEMultipart("related")#related这个参数时固定写法
        #设置邮件的标题
        suject="宠物采购自动化测试"
        #附件对象
        files=MIMEText(open(report_name).read(),'html','utf-8')#附件需要穿的参数：文件流。文件格式和编码格式
        #把邮件的信息组装到邮件对象里面
        message['from']=username #文件来自哪里
        message['to']=receiver   #文件的接收人
        message['suject']=suject #邮件的主题
        message.attach(files)#邮件的附件
        #登录服务器并发送邮件
        smtp=smtplib.SMTP()#获取服务器对象
        smtp.connect(smtpserver)#链接邮件
        smtp.login(username,password)#登录邮箱
        smtp.sendmail(username,receiver,message.as_string())#发送邮件message.as_string()转换成字符串
        smtp.quit()#退出


if __name__ == '__main__':
    reports_name=os.path.join(reports_dir,'reports.html')
    print(reports_name)
    EmailMange().send_email(reports_name)



