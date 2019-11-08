#coding=utf-8
import unittest
import os
class RunCase(unittest.TestCase):
    def test_case01(self):
        case_path=os.path.join(os.getcwd())   #自动匹配当前目录的case   如果在文件的下一级就要在后面加上文件的名字   不然匹配不到  如果这个文件上没有下一级就不用写
        suite=unittest.defaultTestLoader.discover(case_path,'unttest_*.py')  #路径  匹配规则（匹配的类型）  第三个可以不写
        unittest.TextTestRunner().run(suite)

if __name__ =='__main__':
    unittest.main()
