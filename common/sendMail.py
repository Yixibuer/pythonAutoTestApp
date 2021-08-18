# -*- coding:utf-8 -*-
import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header

def sendmail(filename):
    # 发件人地址，通过控制台创建的发件人地址
    username = 'huangshaobo@codemao.cn'
    # 发件人密码，通过控制台创建的发件人密码
    password = ''
    # 自定义的回复地址
    replyto = '***'
    # 收件人地址或是地址列表，支持多个收件人，最多60个
    #rcptto = ['***', '***']
    rcptto = 'huangshaobo@codemao.cn'
    #邮件主题
    title='APP自动化邮件通知'
    # 构建alternative结构
    msg = MIMEMultipart('alternative')
    msg['Subject'] = title
    msg['From'] = '%s ' % Header('APP自动化报告')
    msg['To'] = rcptto
    # 构建alternative的text/plain部分
    textplain = MIMEText('自定义TEXT纯文本部分', _subtype='plain', _charset='UTF-8')
    msg.attach(textplain)
    # Attachement 附件
    att = MIMEApplication(open(filename,'rb').read())
    att.add_header('Content-Disposition', 'attachment', filename=filename)
    msg.attach(att)

    # 构建alternative的text/html部分
    f = open(filename, "rb")
    print(f)
    # 读取文件内容
    mail_body = f.read()
    # 关闭文件
    f.close()

    texthtml = MIMEText(mail_body, 'html','UTF-8')
    msg.attach(texthtml)
    # 发送邮件
    try:
        client = smtplib.SMTP_SSL('smtp.mxhichina.com', 465)
        #python 2.7以上版本，若需要使用SSL，可以这样创建client
        #client = smtplib.SMTP_SSL()
        #SMTP普通端口为25或80
        print('链接代理成功')
        client.login(username, password)
        #发件人和认证地址必须一致
        #备注：若想取到DATA命令返回值,可参考smtplib的sendmaili封装方法:
        #      使用SMTP.mail/SMTP.rcpt/SMTP.data方法
        client.sendmail(username, rcptto, msg.as_string())
        client.quit()
        print('邮件发送成功！')
    except smtplib.SMTPConnectError as e:
        print('邮件发送失败，连接失败:', e.smtp_code, e.smtp_error)
    except smtplib.SMTPAuthenticationError as e:
        print('邮件发送失败，认证错误:', e.smtp_code, e.smtp_error)
    except smtplib.SMTPSenderRefused as e:
        print('邮件发送失败，发件人被拒绝:', e.smtp_code, e.smtp_error)
    except smtplib.SMTPRecipientsRefused as e:
        print('邮件发送失败，收件人被拒绝:', e.smtp_code, e.smtp_error)
    except smtplib.SMTPDataError as e:
        print('邮件发送失败，数据接收拒绝:', e.smtp_code, e.smtp_error)
    except smtplib.SMTPException as e:
        print('邮件发送失败, ', str(e))
    except Exception as e:
        print('邮件发送异常, ', str(e))