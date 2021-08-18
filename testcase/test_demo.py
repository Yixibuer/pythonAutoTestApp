import time
import unittest

from appium import webdriver

from common.Logger import Log
from pages.LoginPage import LoginPage
from pages.MyPage import MyPage



class MyTests(unittest.TestCase):


    # 测试开始前执行的方法
    def setUp(self):
        print('用例开始执行')

        # 测试结束后执行的方法

    def tearDown(self):
          print('jieshu')

    def test_01(self, t=500, n=4):
        """进入首页测试"""

        self.assertEqual(1, 1, '进入首页成功')

        print('进来了')

    def test_02(self, t=500, n=4):
        """进入首页测试"""
        self.assertEqual(1, 2, '进入首页成功')


    def test_03(self, t=500, n=4):
        """进入首页测试"""

        self.assertEqual(1, 1, '进入首页成功')

        print('进来了')

