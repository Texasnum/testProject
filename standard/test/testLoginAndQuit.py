import os
import allure
from selenium import webdriver
import pytest
from standard.page.StandardPage import StandardPageLogin, StandardPageHost
from standard.tool.Tool import Tool


class TestLoginAndQuit:
    driver = None
    loginPage = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome("../tool/chromedriver.exe")
        cls.loginPage = StandardPageLogin(cls.driver)
        cls.loginPage.goto_login()

    @pytest.mark.parametrize(
        ["account", "password", "page_url"],
        [["300472", "123456", 'http://scc-standard.itg.it.org.test/itg-web-admin/#/workbench-nq'],
         ["500117", "500117", 'http://scc-standard.itg.it.org.test/itg-web-admin/#/workbench-manager']],
        ids=["橡胶", "纸张"]
    )
    @allure.feature("测试登录和退出")
    def test_login_and_quit(self, account, password, page_url):
        self.loginPage.input_account(account)
        self.loginPage.input_password(password)
        self.loginPage.input_certify()
        self.loginPage.login()
        assert self.loginPage.get_url == page_url

        self.loginPage = StandardPageHost(self.driver)
        self.loginPage.quit_page()
        assert self.loginPage.get_url == Tool.login_url

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()


if __name__ == '__main__':
    # pytest.main()
    pytest.main(['-s', 'testLoginAndQuit.py', '--clean-alluredir', '--alluredir=../report/allure-results'])
    os.system(r"allure generate ../report/allure-results -o ../report/allure-report --clean")
