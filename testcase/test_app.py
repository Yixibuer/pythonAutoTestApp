# import time
# import unittest
#
# from appium import webdriver
#
# from common.Logger import Log
# from pages.LoginPage import LoginPage
# from pages.MyPage import MyPage
#
# log=Log()
#
#
# class MyTests(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#
#         desired_caps = {'platformName': 'Android',  # 平台名称
#                         'platformVersion': '9',  # 系统版本号
#                         'deviceName': '00395cd40207',  # 设备名称。如果是真机，在'设置->关于手机->设备名称'里查看
#                         'appPackage': 'cn.codemao.android.kids.lite',  # apk的包名
#                         'appActivity': '.module.splash.SplashActivity',  # activity 名称
#                         'noReset': "True"
#                         }
#         cls.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)  # 连接Appium
#         cls.driver.implicitly_wait(8)
#         # 实例化对应页面的方法和对象
#         cls.login_page = LoginPage(cls.driver)
#         cls.my_page = MyPage(cls.driver)
#         cls.log=Log()
#
#         # cls.check_page=UICheck(cls.driver)
#
#     # 测试开始前执行的方法
#     def setUp(self):
#         print('用例开始执行')
#
#     def test_01(self, t=500, n=4):
#         """进入首页测试"""
#         time.sleep(8)
#         log.info('开始测试')
#         if self.driver.find_element_by_id('cn.codemao.android.kids.lite:id/iv_dialog_home_ads'):
#             log.info('出现首页广告弹框')
#             self.driver.find_element_by_id('cn.codemao.android.kids.lite:id/iv_dialog_home_ads_close').click()
#         time.sleep(2)
#         e = self.driver.find_element_by_id('cn.codemao.android.kids.lite:id/tv_mine')
#
#         self.assertEqual(1, 1, '进入首页成功')
#
#         print('进来了')
#
#     def test_02(self, t=500, n=4):
#         """进入首页测试"""
#         self.my_page.click_my_button()
#
#     # 测试结束后执行的方法
#     def tearDown(self):
#         self.driver.quit()
#
#     @classmethod
#     def tearDownClass(cls):
#         cls.driver.quit()
