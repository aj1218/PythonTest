#coding=utf-8
from selenium import webdriver
import time
import os
from base.find_element import FindElenment
class ActionMethod:
    # def __init__(self):
    #     pass
    #打开浏览器
    def open_browser(self,browser):
        if browser == "chrome":
            self.driver=webdriver.Chrome()
        elif browser == "firefox":
            self.driver=webdriver.Firefox()
        else:
            self.driver=webdriver.Edge()

#输入地址
    def get_url(self,url):
        self.driver.get(url)

#定位元素
    def get_element(self,key):
        find_elenment=FindElenment(self.driver)
        element=find_elenment.get_element(key)
        return element

#输入元素
    def element_send_keys(self,value,key):
        element=self.get_element(key)
        element.send_keys(value)

#点击元素
    def click_element(self,key):
        self.get_element(key).click()
#失败截图
    def failure_pro(self,driver):
        for method_name, error in self._outcome.errors:
            if error:
                case_name = self._testMethodName  # 拿到case的名字  如果没有拿到就是使用关闭的操作
                file_path = os.path.join(os.getcwd() + "/report" + case_name + ".png")
                self.driver.save_screenshot(file_path)
        self.driver.close()

#等待
    def sleep_time(self):
        time.sleep(4)

#关闭浏览器
    def close_browser(self):   #*args传多少个参数都可以匹配
        self.driver.close()

#获取title的数据
    def get_title(self):
        title=self.driver.title
        return title






