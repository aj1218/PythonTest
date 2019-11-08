#coding=utf-8
import unittest
class FirstCase01(unittest.TestCase): #unntest 框架必须是以test开始
    @classmethod
    def setUpClass(cls):  #所有的case执行之前执行的东西
        print("所有case执行之前的前置")

    @classmethod
    def tearDownClass(cls):  #和self是没有区别的  建议按照课程来
        print("所有case执行之后的后置")
    def setUp(self):
        print("这个是case的前置条件") #每执行一次case就会执行一次前置条件和后置条件
    def tearDown(self):             #
        print("这是case的后置条件")  #

    @unittest.skip("不执行第一条")   #控制顺序看是否执行
    def testfirst01(self):
        print("这是第一个case")
    def testfirst02(self):
        print("这是第二个case")
    def testfirst3(self):
        print("这是第3个case")


if __name__ =='__main__':
    #unittest.main()
    suite=unittest.TestSuite()   #执行顺序和命名有关  第二和调用有关
    suite.addTest(FirstCase01('testfirst01'))
    suite.addTest(FirstCase01('testfirst02'))
    suite.addTest(FirstCase01('testfirst03'))
    unittest.TextTestRunner().run(suite)