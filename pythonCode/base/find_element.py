#coding=utf-8
#将定位元素的方法封装起来   那时候要使用的时候可以直接调用  调用read_ini的方法  将定位元素的一些东西封装起来
from util.read_inl import ReadIni
class FindElenment(object):
    def __init__(self,driver):  #利用构造函数的形式传入   因为下面要用这个方法
        self.driver=driver  #利用driver定位元素所以要使用

    def get_element(self,key):
        read_init=ReadIni()
        data=read_init.get_value(key)#这里的拿到的值就是id>register_nickname
        by=data.split('>')[0]#拆分   定位方式 可以进行剩下的操作
        value=data.split('>')[1]  #下标拿值
        try:  #try进行简单的容错处理   如果没有找到数值   就进行容错处理
            if by =='id ':  #定位方式的多种化
                return self.driver.find_element_by_id(value)
            elif by == 'name':
                return self.driver.find_element_by_name(value)
            elif by == 'className':
                return self.driver.find_element_by_class_name(value)
            else:
                return self.driver.find_element_by_xpath(value)
        except:
            # self.driver.save_screenshot('test.png'%value) #截图
            return None  #如果没有定位成功要么传回来的是元素   要就是一个none  传回来就是一个空值