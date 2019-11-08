#coding=utf-8
# 邮箱 用户名 密码 验证码 错误信息定位元素  错误提示信息    实现数据驱动
import ddt
import unittest
from business.resister_business import ResisterBusiness
from selenium import webdriver
import time
import HTMLTestrunner
import os
from util.excel_util import ExcelUtil   #导入包  直接调用
ex = ExcelUtil()
data = ex.get_data()
@ddt.ddt
class FirstDdtCase(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.get("http://www.5itest.cn/register")
        # self.logger.info("this is chrome")
        self.login = ResisterBusiness(self.driver)

    def tearDown(self):
        # 后置条件
        time.sleep(2)
        #if sys.exc_info()[0]:
            # self._outcome.errors    这样的情况下拿到的是一个list    这时候一定要使用一个for循环
        #这里的method是一个类  用不用   只要判断error有没有  如果有我就使用截图
        # for method_name,error in self._outcome.errors:
        #     if error:
        #         case_name=self._testMethodName  #拿到case的名字  如果没有拿到就是使用关闭的操作
        #         file_path = os.path.join(os.getcwd() + "/report" + case_name+".png")
        #         self.driver.save_screenshot(file_path)
        self.driver.close()



    # @ddt.data(
    #     ['1123132', 'zhangsan', '111111', 'code', 'user_email_error', '请输入有效的电子邮箱地址'],  # 字典的格式  python的写法
    #     ['@qq.com', 'zhangsan', '111111', 'code', 'user_email_error', '请输入有效的电子邮箱地址'],
    #     ['1209876@qq.com', 'zhangsan', '111111', 'code', 'user_email_error', '请输入有效的电子邮箱地址']
    #
    # )
    # @ddt.unpack
    @ddt.data(*data)
    def test_register_case(self,data): #邮箱错误其他的正确  验证码除外 的测试用例
        email,username,password,file_name,assertCode,assertText=data
        email_erroer=self.login.regieter_function(email, username, password, file_name, assertCode, assertText)
        self.assertFalse(email_erroer,'case执行了')  #判断这个结果是否为false如果是就是成功的

if __name__ == '__main__':

    file_path = os.path.join(os.getcwd() + "/report" + "frist.html")
    f = open(file_path, 'wb')  # 读取文件的流媒体
    suite=unittest.TestLoader().loadTestsFromTestCase(FirstDdtCase)
    runner = HTMLTestrunner.HTMLTestRunner(stream=f, title="this is first report", description="这是我们第一次测试报告1", verbosity=2)
    runner.run(suite)


