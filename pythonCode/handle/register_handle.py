# coding=utf-8
from page.register_page import RegisterPage
 # from util.get_code import GetCode
import  sys
class RegisterHandle(object):  #输入的元素的操作   针对页面的所有输入 放的是case里面的操作流程
    def __init__(self,driver):  # 实例化前面的case里面的操作  一步一步的进行封装
        self.driver=driver
        self.register_p=RegisterPage(self.driver)
    #输入整个邮箱  这个里面对应的就是操作层
    def send_user_email(self,email):
        self.register_p.get_email_element().send_keys(email)
        # 输入用户名
    def send_user_name(self,username):
        self.register_p.get_username_element().send_keys(username)
        # 输入密码
    def send_user_pass(self,password):
        self.register_p.get_pass_element().send_keys(password)
        # 输入验证码
    def send_user_code(self,file_name):
        # get_code_text=GetCode(self.driver)
        # code=get_code_text.code_online(file_name)#这里可以写死但是在工作的时候尽量不写死
        self.register_p.get_coed_element().send_keys(file_name)
        #获取文字信息
    def get_user_text(self,info,user_info):
        try:
            if info == 'user_email_error':
                text = self.register_p.get_email_error_element().text  # 如果在页面的属性中又value就可以使用不然就找不到这个的属性的信息 所以我们可以直接使用test获取页面的信息
            elif info == 'user_name_error':
                text = self.register_p.get_name_error_element().text
            elif info == 'user_pass_error':
                text = self.register_p.get_pass_erroe_element().text
            else:
                text = self.register_p.get_code_erroe_element().text
        except:
            text=None
        return text
        #点击注册按钮
    def click_register_button(self):
        self.register_p.get_button_element().click()

    #获取注册按钮文字
    def get_register_text(self):
        return self.register_p.get_button_element().text


