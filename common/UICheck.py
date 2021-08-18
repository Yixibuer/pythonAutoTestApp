import time

from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class UICheck(BasePage):
    def isExit_Element(self, el):
        source = self.driver.page_source
        if el in source:
             return True
        else:
            return False

    def is_element(self, *loc):  # 判断元素是否存在
        e = self.driver.find_elements(*loc) == []
        if e:
            return False  # 元素不存在返回False
        else:
            return True  # 元素存在返回True

    def dealPop(self):  # 判断元素是否存在
        if self.driver.find_elements(By.ID,'cn.codemao.android.kids.lite:id/iv_dialog_home_ads'):
            print('出现首页广告弹框')
            self.driver.find_element(By.ID,'cn.codemao.android.kids.lite:id/iv_dialog_home_ads_close').click()
        else:
            return