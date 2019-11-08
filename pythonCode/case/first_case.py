# coding=utf-8    case文件夹放以后的case
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), "..")))
from business.resister_business import ResisterBusiness
from selenium import webdriver
import unittest
import time
from log.user_log import UserLog
import HTMLTestrunner
# log=UserLog()
# logger=log.get_lof()

#这里面写的是一条条的测试用例      在最后面的时候如果是要生生成测试报告  在代码里面就一定不能有打印的输入语句  不然就会报错
#从此之后如果在跑测试用例的时候出现了错误 要学会查看生成的测试报告里面的内容
class FirstCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.log=UserLog()
        cls.logger=cls.log.get_lof()
        # file_name="test.png"
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.get("http://www.5itest.cn/register")
        self.logger.info("this is chrome")
        self.login = ResisterBusiness(self.driver)

    def tearDown(self):
        # 后置条件
        time.sleep(2)
        #if sys.exc_info()[0]:
            # self._outcome.errors    这样的情况下拿到的是一个list    这时候一定要使用一个for循环
        #这里的method是一个类  用不用   只要判断error有没有  如果有我就使用截图
        for method_name,error in self._outcome.errors:
            if error:
                case_name=self._testMethodName  #拿到case的名字  如果没有拿到就是使用关闭的操作
                file_path = os.path.join(os.getcwd() + "/report" + case_name+".png")
                self.driver.save_screenshot(file_path)
        self.driver.close()

        #print("这是case的后置条件")  # 进行浏览器的关闭
        # self.driver.save_screenshot()
    @classmethod
    def tearDownClass(cls):
        cls.log.close_handle()

    def test_login_email_error(self): #邮箱错误其他的正确  验证码除外 的测试用例
        email_erroer=self.login.login_email_error('34','user111','11111111','test1')
        return self.assertTrue(email_erroer,'case执行了')  #判断这个结果是否为false如果是就是成功的

        # if email_erroer == True:
        #     print('注册成功，此条case执行失败')

       #通过 Assert  判断是否为error   检测输入的数据是否正确
    def test_login_username_error(self): #
        useranme_error=self.login.login_name_error('111@qq.com', 'ss','ccwcw','test1')
        self.assertTrue(useranme_error)  #判断这个结果是否为false如果是就是成功的
        # if useranme_error == True:
        #     print('注册成功，此条case执行失败')

    def test_login_code_error(self):
        code_error=self.login.login_code_error('111@qq.com', 'ss1','e2e2e2','test1')
        self.assertTrue(code_error)  #判断这个结果是否为false如果是就是成功的

        # if code_error == True:
        #     print('注册成功，此条case执行失败')

    def test_login_pass_error(self):
        pass_error = self.login.login_pass_error('111@qq.com', 'ss1', 'e2e2e2', 'test1')
        self.assertTrue(pass_error)  #判断这个结果是否为false如果是就是成功的

        # if pass_error == True:
        #     print('注册成功，此条case执行失败')

    def test_login_secces(self):
        login_secces = self.login.user_base('111@qq.com', 'ss1', 'e2e2e2', 'test1')
        self.assertTrue(login_secces)  #判断这个结果是否为false如果是就是成功的

        # if self.login.register_secces()==True:
        #     print("注册成功")

if __name__ == '__main__':
    file_path = os.path.join(os.getcwd() + "/report" +"frist_case.html")
    f=open(file_path,'wb') #读取文件的流媒体
    suite=unittest.TestSuite()
    suite.addTest(FirstCase('test_login_pass_error'))
    suite.addTest(FirstCase('test_login_username_error'))
    suite.addTest(FirstCase('test_login_code_error'))
    suite.addTest(FirstCase('test_login_secces'))
    suite.addTest(FirstCase('test_login_email_error'))
    # unittest.TextTestRunner().run(suite)
    runner=HTMLTestrunner.HTMLTestRunner(stream=f,title="this is first report",description=u"这是我们第一次测试报告",verbosity=2)
    runner.run(suite)





