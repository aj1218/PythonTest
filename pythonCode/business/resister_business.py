#coding=utf-8
from handle.register_handle import RegisterHandle
class ResisterBusiness(object):#  业务层   只是用来执行操作
    def __init__(self,driver):  #如果很多地方要使用它就开始使用实例化
        self.register_h =RegisterHandle(driver)

    def user_base(self,emali,username,password,file_name):
        self.register_h.send_user_email(emali)
        self.register_h.send_user_name(username)
        self.register_h.send_user_pass(password)
        self.register_h.send_user_code(file_name)
        self.register_h.click_register_button()

    def register_secces(self):
         if self.register_h.get_register_text()==None:
             return True
         else:
             return False

    #执行操作   去操作handle层
    def login_email_error(self,emali,username,password,file_name):
        self.user_base(emali,username,password,file_name)
        if self.register_h.get_user_text('user_email_error',"请输入有效的电子邮箱地址") == None:
            # print("邮箱检验不成功")
            return True
        else:
            return False

    def regieter_function(self,email, username, password, file_name, assertCode, assertText):
        self.user_base(email, username, password, file_name)
        #如果邮箱信息为空就使用assertCode去检验assertText
        if self.register_h.get_user_text(assertCode,assertText) == None:
            # print("邮箱检验不成功")
            return True
        else:
            return False

#用户名错误
    def login_name_error(self, emali, username, password, file_name):
        self.user_base(emali, username, password, file_name)
        if self.register_h.get_user_text('user_name_error', "字符长度必须大于等于4，一个中文字算2个字符") == None:
            # print("用户名检验不成功")
            return True
        else:
            return False

     # 密码错误
    def login_pass_error(self, emali, username, password, file_name):
            self.user_base(emali, username, password, file_name)
            if self.register_h.get_user_text('user_pass_error', "最少需要输入 5 个字符") == None:
                # print("密码检验不成功")
                return True
            else:
                return False

    #验证码错误
    def login_code_error(self, emali, username, password, file_name):
            self.user_base(emali, username, password, file_name)
            if self.register_h.get_user_text('code_text_error', "验证码错误") == None:
                # print("验证码检验不成功")
                return True
            else:
                return False





