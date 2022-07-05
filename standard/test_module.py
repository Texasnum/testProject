from selenium import webdriver
import ddddocr
import pytest
from selenium.webdriver.common.by import By
from StandardPage import StandardPageLogin, StandardPageHost

url = "http://scc-standard.itg.it.org.test/itg-web-admin/#/login"
filename = r"E:\各种学习资料\实习应聘\国贸实习\testGraph\image.png"


class TestLogin:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome(r"E:\Java\Maven\driver\chromedriver.exe")

    @pytest.mark.parametrize(
        ["account", "password", "page_url"],
        [["300472", "123456", 'http://scc-standard.itg.it.org.test/itg-web-admin/#/workbench-nq'],
         ["500117", "500117", 'http://scc-standard.itg.it.org.test/itg-web-admin/#/workbench-manager']],
        ids=["橡胶", "纸张"]
    )
    def test_login(self, account, password, page_url):
        def get_graph():
            png = self.driver.find_element(By.XPATH, '//*[@id="main"]/div/div/form/div[4]/div/div/div[2]/img')
            png.screenshot(filename)  # 将图片截屏并保存

        def discern():
            with open(filename, 'rb') as f:
                im = f.read()
            ocr = ddddocr.DdddOcr()
            res = ocr.classification(im)
            return res

        page = StandardPageLogin(self.driver)
        page.open(url)
        page.set_window_size()
        page.search_account = account
        page.sleep(1)
        page.search_password = password
        page.sleep(1)
        get_graph()
        page.search_certify = discern()
        page.sleep(1)
        page.search_button.click()
        page.sleep(3)
        assert page.get_url == page_url

        page = StandardPageHost(self.driver)
        page.search_setting.move_to_element()
        page.search_quit.click()
        page.sleep(2)
        assert page.get_url == url

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()


if __name__ == '__main__':
    pytest.main()
