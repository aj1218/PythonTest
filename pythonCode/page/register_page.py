#coding=utf-8
from base.find_element import FindElenment
#元素去拿elenment元素
class RegisterPage(object):  #将读取元素信息的数据放在这里  利用handle去调用page层

    def __init__(self,driver):  #现在为了把driver传进去
        self.fd=FindElenment(driver)
        #获取邮箱元素
    def get_email_element(self):
        return self.fd.get_element("user_email") #配置文件里面的信息
    #获取用户名元素
    def get_username_element(self):
        return self.fd.get_element("user_name")

    #获取密码元素
    def get_pass_element(self):
        return self.fd.get_element("user_pass")

    #获取验证码元素
    def get_coed_element(self):
        return self.fd.get_element("code_text")

        # 获取验证码元素
    def get_button_element(self):
        return self.fd.get_element("registr_button")

        #获取邮箱错误的信息
    def get_email_error_element(self):
        return self.fd.get_element("user_email_error")

        # 获取用户名错误的信息
    def get_name_error_element(self):
        return self.fd.get_element("user_name_error")

        #获取密码错误的信息
    def get_pass_erroe_element(self):
        return self.fd.get_element("user_pass_error")

        #获取验证码错误的信息
    def get_code_erroe_element(self):
        return self.fd.get_element("code_text_error")








