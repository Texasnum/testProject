from selenium import webdriver
import ddddocr
import pytest
from selenium.webdriver.common.by import By
from StandardPage import StandardPageLogin, StandardPageHost

url = "http://scc-standard.itg.it.org.test/itg-web-admin/#/login"
filename = r"E:\各种学习资料\实习应聘\国贸实习\testGraph\image.png"


class TestPaper:
    driver = None
    page = None

    @classmethod
    def setup_class(cls):
        def get_graph():
            png = cls.driver.find_element(By.XPATH, '//*[@id="main"]/div/div/form/div[4]/div/div/div[2]/img')
            png.screenshot(filename)  # 将图片截屏并保存

        def discern():
            with open(filename, 'rb') as f:
                im = f.read()
            ocr = ddddocr.DdddOcr()
            res = ocr.classification(im)
            return res

        cls.driver = webdriver.Chrome(r"E:\Java\Maven\driver\chromedriver.exe")
        cls.page = StandardPageLogin(cls.driver)
        cls.page.open(url)
        cls.page.set_window_size()
        cls.page.search_account = "500117"
        cls.page.search_password = "500117"
        get_graph()
        cls.page.search_certify = discern()
        cls.page.search_button.click()
        cls.page.sleep(2)

    def test_quit(self):
        self.page = StandardPageHost(self.driver)
        self.page.search_setting.move_to_element()
        self.page.search_quit.click()
        self.page.sleep(2)
        assert self.page.get_url == url

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()


if __name__ == '__main__':
    pytest.main()
