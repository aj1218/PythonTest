#coding=utf-8
import configparser   #导入第三方的包 用于对文件的读写   方便在自动化的过程   不改脚本修改配置文件
class ReadIni(object):
        def __init__(self,file_name=None,node=None):
            if file_name ==None:
                file_name=r"D:\pythonCode\congif\LocalElement.inl"
            if node==None:
                self.node="RegisterElement"
            else:
                self.node=node
            self.cf=self.load_ini(file_name)
#加载函数文件
        def load_ini(self,file_name):
            cf = configparser.ConfigParser()  # 调用读取的方法
            cf.read(file_name)  # 写的配置文件
            return cf
#创建函数读取内容 获取value值
        def get_value(self,key):
            data=self.cf.get(self.node,key)  # 第一个拿到他的节点   第二个就是节点里面的元素 以此外推
            return data
if __name__ == '__main__':
#if __name__=='_main_':
    print(1111111)
    read_init=ReadIni()
    print(read_init.get_value('user_name'))

