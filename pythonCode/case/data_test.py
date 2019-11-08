#coding=utf-8
import ddt
import unittest
@ddt.ddt   #运用ddt
class DataTest(unittest.TestCase):
    def setUp(self):
        print("这是一个setup")
    def tearDown(self):
        print("这是teardown")
    @ddt.data(
        [1,2],   #字典的格式  python的写法
        [3,4],   #ddt的格式存下来   可以存在一个list里面也可以是字典
        ["5","6"]
    )
    @ddt.unpack   #解包
    def test_add(self,a,b):
        print(a+b)

if __name__ == '__main__':
    unittest.main()