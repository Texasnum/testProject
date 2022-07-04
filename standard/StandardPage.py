from poium import Page, Element


class StandardPageLogin(Page):
    #  中台登录界面
    search_account = Element(xpath='//*[@id="main"]/div/div/form/div[2]/div/div[1]/input')
    search_password = Element(xpath='//*[@id="main"]/div/div/form/div[3]/div/div[1]/input')
    search_certify = Element(xpath='//*[@id="main"]/div/div/form/div[4]/div/div[1]/div[1]/input')
    search_certify_graph = Element(xpath='//*[@id="main"]/div/div/form/div[4]/div/div/div[2]/img')
    search_button = Element(xpath='//*[@id="main"]/div/div/form/div[5]/div/button/span')


class StandardPageHost(Page):
    #  中台主界面
    search_setting = Element(xpath='//*[@id="main"]/div/div[2]/div[1]/div[4]/div[2]/div[1]')
    search_quit = Element(xpath='//*[@id="main"]/div/div[2]/div[1]/div[4]/div[2]/div[2]/ul/li[2]')
