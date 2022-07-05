from selenium import webdriver
import pytest
from StandardPage import StandardPageLogin, StandardPageHost, Tool

url = "http://scc-standard.itg.it.org.test/itg-web-admin/#/login"
filename = "image.png"


class TestLogin:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome("chromedriver.exe")

    @pytest.mark.parametrize(
        ["account", "password", "page_url"],
        [["300472", "123456", 'http://scc-standard.itg.it.org.test/itg-web-admin/#/workbench-nq'],
         ["500117", "500117", 'http://scc-standard.itg.it.org.test/itg-web-admin/#/workbench-manager']],
        ids=["橡胶", "纸张"]
    )
    def test_login(self, account, password, page_url):
        page = StandardPageLogin(self.driver)
        page.open(url)
        page.set_window_size()
        page.search_account = account
        page.search_password = password
        Tool.get_graph(self.driver, filename)
        page.search_certify = Tool.discern(filename)
        page.search_button.click()
        page.sleep(2)
        assert page.get_url == page_url
        page.sleep(1)
        page = StandardPageHost(self.driver)
        page.search_setting.move_to_element()
        page.sleep(1)
        page.search_quit.click()
        page.sleep(2)
        assert page.get_url == url

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()


if __name__ == '__main__':
    pytest.main()
