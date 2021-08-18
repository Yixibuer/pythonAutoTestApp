from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class MyPage(BasePage):
    u'我的页面'

    #底部状态栏 我的 按钮
    my_button=(By.ID,'cn.codemao.android.kids.lite:id/tv_mine')

    #立即登录按钮 you text
    my_login_button=(By.ID,'cn.codemao.android.kids.lite:id/mine_login_text')

    #喵币商城
    my_coinstore=(By.ID,'cn.codemao.android.kids.lite:id/topBar_left_image')

    #小火箭商城
    my_rocketstore=(By.ID,'cn.codemao.android.kids.lite:id/topBar_right_image')

    #儿童锁
    my_childrenlock=(By.ID,'cn.codemao.android.kids.lite:id/img_children_lock_bg')

    #儿童锁关闭
    my_childrenlock_close=(By.ID,'cn.codemao.android.kids.lite:id/img_close_validator')

    #儿童锁答题区
    my_childrenlock_answer=(By.ID,'cn.codemao.android.kids.lite:id/img_close_validator')

    #我的任务
    my_work=(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/'
                      'android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/androidx.viewpager.widget.ViewPager/'
                      'android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout/android.view.ViewGroup[1]/'
                      'android.view.ViewGroup/android.widget.TextView')
    #切换到我的页面
    def click_my_button(self):
        self.find_element(*self.my_button).click()