from poium import Page, Element
from standard.tool.Tool import Tool


class StandardPageLogin(Page):
    #  中台登录界面
    search_account = Element(xpath='//*[@id="main"]/div/div/form/div[2]/div/div[1]/input')
    search_password = Element(xpath='//*[@id="main"]/div/div/form/div[3]/div/div[1]/input')
    search_certify = Element(xpath='//*[@id="main"]/div/div/form/div[4]/div/div[1]/div[1]/input')
    search_certify_graph = Element(xpath='//*[@id="main"]/div/div/form/div[4]/div/div/div[2]/img')
    search_button = Element(xpath='//*[@id="main"]/div/div/form/div[5]/div/button/span')

    def goto_login(self):
        # 跳转到登录页面并最大化
        self.wait()
        self.open(Tool.login_url)
        self.set_window_size()

    def input_account(self, account):
        # 输入账号
        self.wait()
        self.search_account.send_keys(account, clear=True)

    def input_password(self, password):
        # 输入密码
        self.wait()
        self.search_password.send_keys(password, clear=True)

    def input_certify(self):
        # 从图片中识别获取验证码并输入
        self.wait()
        Tool.get_graph(self.driver, Tool.filename)
        self.search_certify.send_keys(Tool.discern(Tool.filename), clear=True)

    def login(self):
        # 点击登录按钮
        self.search_button.click()
        self.sleep(3)


class StandardPageHost(Page):
    #  中台主界面
    search_setting = Element(xpath='//*[@id="main"]/div/div[2]/div[1]/div[4]/div[2]/div[1]')
    search_quit = Element(xpath='//*[@id="main"]/div/div[2]/div[1]/div[4]/div[2]/div[2]/ul/li[2]')

    def quit_page(self):
        # 退出主界面，返回登录界面
        self.search_setting.move_to_element()
        self.search_quit.click()
        self.sleep(3)
