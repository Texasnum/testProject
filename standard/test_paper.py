from selenium import webdriver
import pytest
from StandardPage import StandardPageLogin, StandardPageHost, Tool

url = "http://scc-standard.itg.it.org.test/itg-web-admin/#/login"
filename = "image.png"


class TestPaper:
    driver = None
    page = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome("chromedriver.exe")
        cls.page = StandardPageLogin(cls.driver)
        cls.page.open(url)
        cls.page.set_window_size()
        cls.page.search_account = "500117"
        cls.page.search_password = "500117"
        Tool.get_graph(cls.driver, filename)
        cls.page.search_certify = Tool.discern(filename)
        cls.page.search_button.click()
        cls.page.sleep(2)

    def test_quit(self):
        self.page = StandardPageHost(self.driver)
        self.page.search_setting.move_to_element()
        self.page.sleep(1)
        self.page.search_quit.click()
        self.page.sleep(2)
        assert self.page.get_url == url

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()


if __name__ == '__main__':
    pytest.main()
