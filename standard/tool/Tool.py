import ddddocr
from selenium.webdriver.common.by import By


class Tool:
    login_url = "http://scc-standard.itg.it.org.test/itg-web-admin/#/login"  # 登录页面url
    filename = "../tool/image.png"  # 截取的图片存放路径

    @classmethod
    def get_graph(cls, driver, filename):
        png = driver.find_element(By.XPATH, '//*[@id="main"]/div/div/form/div[4]/div/div/div[2]/img')
        png.screenshot(filename)  # 将验证码图片截屏并保存

    @classmethod
    def discern(cls, filename):
        # 识别出验证码，并返回
        with open(filename, 'rb') as f:
            im = f.read()
        ocr = ddddocr.DdddOcr()
        res = ocr.classification(im)
        return res
