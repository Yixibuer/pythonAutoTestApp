from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class LoginPage(BasePage):
    u'登录页面'

    # 微信登录
    login_type_wechat = (By.ID, 'cn.codemao.android.kids.lite:id/iv_we_chat')

    # 扫码登录
    login_type_scan = (By.ID, 'cn.codemao.android.kids.lite:id/iv_scan')

    # 编程猫账号登录
    login_type_codemao = (By.ID, 'cn.codemao.android.kids.lite:id/iv_account')

    # 同意协议按钮
    login_agree_button = (By.ID, 'cn.codemao.android.kids.lite:id/cb_agreement')

    # 同意协议文本
    login_agree_text = (By.ID, 'cn.codemao.android.kids.lite:id/tv_agreement')

    # 账户名
    login_username = (By.ID, 'cn.codemao.android.kids.lite:id/et_account')

    # 密码
    login_password = (By.ID, 'cn.codemao.android.kids.lite:id/et_pwd')

    '''
    以下所有发find_element方法均为继承父类使用父类的
    '''

    # 操作用户名输入框
    def input_username(self, user):
        return self.find_element(*self.login_username).send_keys(user)

    # 操作验证码输入框
    def input_pwd(self, psw):
        return self.find_element(*self.login_password).send_keys(psw)
