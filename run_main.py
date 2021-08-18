import os
import time
import unittest

import common
from HTMLTestRunner import HTMLTestRunner
from common import sendMail
from common.Logger import LogOutput


def all_case():
    #需要执行的测试用例文件夹
    case_dir = './testcase'
    #创建测试套件
    test_case=unittest.TestSuite() #此时是个空的套件

    discover = unittest.defaultTestLoader.discover(start_dir=case_dir, pattern="test*.py",top_level_dir=None)

    #将discover筛选出来的测试用例循环添加到测试套件里面
    for case in discover:
        test_case.addTest(case)
    return test_case

if __name__ == "__main__":
    report_dir = './test_report'
    logpath=os.getcwd()+'\logs\\'
    os.makedirs(report_dir, exist_ok=True)
    now = time.strftime("%Y-%m-%d %H-%M-%S")
    report_name = '{0}/{1}.html'.format(report_dir, now)
    logout=LogOutput().logOutput(logpath)
    with open(report_name, 'wb')as f:
        runner = HTMLTestRunner(stream=f, title="这是自动化任务的title", description="本测试报告内容包含超级计算器的简单测试")
        runner.run(all_case())
    # #sendMail.sendmail(report_name)



